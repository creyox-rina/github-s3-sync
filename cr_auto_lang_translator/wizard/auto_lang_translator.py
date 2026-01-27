# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.modules import get_module_path
from odoo.exceptions import ValidationError
from odoo.tools.translate import TranslationModuleReader, TranslationRecordReader
from googletrans import Translator, LANGUAGES
from translate import Translator as translate

import os
import polib
import datetime
import logging

_logger = logging.getLogger(__name__)
NEW_LANG_KEY = '__new__'


class AutoLangTranslator(models.TransientModel):
    _name = 'auto.lang.translator'
    _description = 'Auto Language Translator'

    @api.model
    def _lang_get(self):
        return self.env['res.lang'].get_installed()

    module_id = fields.Many2one('ir.module.module', string='App To Translate',
                            help='Select the module that you want to translate.')
    lang = fields.Selection(_lang_get, string='Language',
                            help="Select the language in that you want to translate the terms.")
    is_allow_override = fields.Boolean(string='If Exists then overwrite it',
                            help="It will override the translated po files if it exists in selected module.")
    is_existing_po_file = fields.Boolean()

    def check_i18n_exists(self):
        """This method checks if i18n folder is already exists or not."""
        module_name = self.module_id.name
        folder_name = 'i18n'
        module = self.env['ir.module.module'].search([('name', '=', module_name)], limit=1)
        module_path = get_module_path(module_name)
        i18n_folder_path = os.path.join(module_path, folder_name)
        if module:
            if os.path.exists(i18n_folder_path):
                return i18n_folder_path
            else:
                try:
                    os.makedirs(i18n_folder_path, exist_ok=True)
                    _logger.info(f"- - directory i18n created successfully in {module_name} module!")
                    return i18n_folder_path
                except OSError as error:
                    raise ValidationError(
                        _("System faced following error while creating a i18n folder inside the %s module!\n%s" %(module_name, error)))

    def create_po_file(self, i18n_path=False):
        """This method create a .po file of selected language"""
        if i18n_path:
            lang_id = self.env['res.lang'].sudo().search([('code', '=', self.lang)], limit=1)
            po_file_name = f'{lang_id.iso_code}.po'
            po_file_path = os.path.join(i18n_path, po_file_name)
            if os.path.exists(po_file_path) and not self.is_allow_override:
                po_file = polib.pofile(po_file_path)
                self.is_existing_po_file = True
            else:
                po_file = polib.POFile()
                _logger.info(f"- - PO file created successfully {po_file_path}!")
            return po_file, po_file_path

    def is_language_supported(self, language_code=False):
        """This method checks if google translator is support destination language or not."""
        if language_code in LANGUAGES:
            return language_code
        else:
            if language_code in ['zh_HK', 'zh_CN']:
                return 'zh-cn'
            elif language_code in ['zh_TW']:
                return 'zh-tw'
            else:
                new_lang_code = ''
                if language_code.__contains__('_'):
                    new_lang_code = language_code.split("_")[0]
                    if new_lang_code in LANGUAGES:
                        return new_lang_code
                lang_codes = f"{language_code}"
                if new_lang_code:
                    lang_codes += f" or {new_lang_code}"
                raise ValidationError(
                    _(f"{language_code} or {new_lang_code} language code not found in google translation library!"))

    def translated_term_writer(self, po_file, po_file_path):
        """This method writes the translated terms in .po file"""
        lang = self.lang if self.lang != NEW_LANG_KEY else False
        lang_id = self.env['res.lang'].sudo().search([('code', '=', self.lang)], limit=1)
        cr = self.env.cr
        module = [self.module_id.name]
        raw_data_for_translation = {}
        reader = TranslationModuleReader(cr, modules=module, lang=lang)
        for module, type, name, res_id, src, trad, comments in reader:
            vals = {
                'module': module,
                'type': type,
                'name': name,
                'res_id': res_id,
                'src': src,
                'trad': trad,
                'comments': comments,
            }
            key = src
            if key in raw_data_for_translation:
                raw_data_for_translation[key].append(vals)
            else:
                raw_data_for_translation.update({key: [vals]})
        # Add translations to the PO file
        lang_code_from_py_lib = self.is_language_supported(lang_id.iso_code)
        from_lang_code = False
        for src, translations in raw_data_for_translation.items():
            flag_list = []
            tcomment_list = []
            comment = f"module: {self.module_id.name}"
            msgid = src
            try:
                google_translator = Translator()
                translated_result = google_translator.translate(src, dest=lang_code_from_py_lib)
                translated_term = translated_result.text
            except Exception as e:
                try:
                    _logger.warning("google translator faced some issue during translation: {}".format(e))
                    if not from_lang_code:
                        from_lang_code = self.is_language_supported(self.env.user.lang)
                    translator = translate(from_lang=from_lang_code, to_lang=lang_code_from_py_lib)
                    translated_term = translator.translate(src)
                except Exception as e:
                    _logger.warning("translate lib faced some issue during translation: {}".format(e))
                    raise ValidationError(
                        _("Auto translator faced some issue to translate the following term.\n{}\n\nError:{}".format(src, e)))

            msgstr = translated_term
            try:
                for translation in translations:
                    if translation.get('comments'):
                        flag_list.append(translation.get('comments')[0])
                    tcomment = f"{translation.get('type')}:{translation.get('name')}:{translation.get('res_id')}"
                    if tcomment:
                        tcomment_list.append(tcomment)
                entry = polib.POEntry(
                    comment=comment,
                    flags=flag_list,
                    occurrences=[(rec, '') for rec in tcomment_list],
                    msgid=msgid,
                    msgstr=msgstr
                )
                po_file.append(entry)
            except Exception as e:
                raise ValidationError(
                    _("Some issue is facing while write translated terms in PO file.\nError:{}".format(e)))
        po_file.save(po_file_path)
        _logger.info(f" - - {po_file_path} file saved successfully!")

    def po_file_writer(self, po_file, po_file_path):
        """This method write the translated terms in po file."""
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        lang_id = self.env['res.lang'].sudo().search([('code', '=', self.lang)], limit=1)
        if not self.is_existing_po_file:
            po_file.header = (
                "Translated by Auto Language Translation Tool of Creyox Technologies.\n"
                "his file contains the translation of the following module:\n"
                f"\t* {self.module_id.name}\n"
                "\n"
                "Translator:\n"
                f"Auto Language Translator Tool, {datetime.datetime.now().year}\n"
            )
            po_file.metadata = {
                'Project-Id-Version': self.module_id.name,
                'Report-Msgid-Bugs-To': '',
                'POT-Creation-Date': current_date,
                'PO-Revision-Date': current_date,
                'Last-Translator': 'Auto Translated Terms by App',
                'Language-Team': f'{lang_id.name}',
                'Language': lang_id.iso_code,
                'MIME-Version': '1.0',
                'Content-Type': 'text/plain; charset=UTF-8',
                'Content-Transfer-Encoding': '8bit',
            }
            po_file.save(po_file_path)

            # write translated terms in po file
        self.translated_term_writer(po_file, po_file_path)
        return True

    def action_translate(self):
        """This method process the auto translation for selected language and module."""
        i18n_path = self.check_i18n_exists()
        if i18n_path:
            po_file, po_file_path = self.create_po_file(i18n_path=i18n_path)
            if po_file_path:
                po_file_writer = self.po_file_writer(po_file, po_file_path)
                if po_file_writer:
                    return {
                        'type': 'ir.actions.client',
                        'tag': 'display_notification',
                        'params': {
                            'title': 'Auto Language Translation',
                            'message': "Translation process completed successfully!",
                            'type': 'success',
                            'sticky': False,
                        }
                    }
