# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class AutoClean(models.Model):
    _name = 'auto.clean'
    _description = 'Auto Clean'
    _rec_name = 'cleanup_type'

    notification_cleanup = fields.Boolean(help='Allow notification cleanups.')
    followers_cleanup = fields.Boolean(help='Allow followers cleanups.')
    mail_cleanup = fields.Boolean(help='Allow mail cleanups.')
    sms_cleanup = fields.Boolean(help='Allow SMS cleanups.')
    cleanup_type = fields.Selection([('number', 'Based on Numbers'), ('date', 'Based on Date')], default='number',
                                    help="Based on Numbers: It deletes the record which are greater than entered digits. EX. If user enter 500 and records are 600 then old 100 records are deleted when scheduler runs.\nBased on Date: It deletes the record which are older than entered date.")
    notification_no = fields.Integer(help='It deletes the record which is greater than entered number.')
    followers_no = fields.Integer(help='It deletes the record which is greater than entered number.')
    mail_no = fields.Integer(help='It deletes the record which is greater than entered number.')
    sms_no = fields.Integer(help='It deletes the record which is greater than entered number.')
    mail_date = fields.Datetime(help='It deletes the record which is older than entered date.')
    sms_date = fields.Datetime(help='It deletes the record which is older than entered date.')

    def number_cleanup_type(self):
        if self.notification_cleanup and self.notification_no > 0:
            notification = self.env['mail.notification'].search_count([])
            if notification > self.notification_no:
                limit = notification - self.notification_no
                notification_ids = self.env['mail.notification'].search([], limit=limit, order='id asc')
                notification_ids.sudo().unlink()
        if self.mail_cleanup and self.mail_no > 0:
            mail = self.env['mail.mail'].search_count([])
            if mail > self.mail_no:
                limit = mail - self.mail_no
                mail_ids = self.env['mail.mail'].search([], limit=limit, order='id asc')
                mail_ids.sudo().unlink()
        if self.followers_cleanup and self.followers_no > 0:
            followers = self.env['mail.followers'].search_count([])
            if followers > self.followers_no:
                limit = followers - self.followers_no
                followers_ids = self.env['mail.followers'].search([], limit=limit, order='id asc')
                followers_ids.sudo().unlink()
        if self.sms_cleanup and self.sms_no > 0:
            sms = self.env['sms.sms'].search_count([])
            if sms > self.sms_no:
                limit = sms - self.sms_no
                sms_ids = self.env['sms.sms'].search([], limit=limit, order='id asc')
                sms_ids.sudo().unlink()

    def date_cleanup_type(self):
        if self.mail_cleanup and self.mail_date:
            mail_ids = self.env['mail.mail'].search([('create_date', '<=', self.mail_date)])
            if mail_ids:
                mail_ids.sudo().unlink()
        if self.sms_cleanup and self.sms_date:
            sms_ids = self.env['sms.sms'].search([('create_date', '<=', self.sms_date)])
            if sms_ids:
                sms_ids.sudo().unlink()

    def _auto_cleanup(self):
        cleanup_id = self.env['auto.clean'].search([], limit=1)
        if cleanup_id and cleanup_id.cleanup_type == 'number':
            cleanup_id.number_cleanup_type()
        elif cleanup_id and cleanup_id.cleanup_type == 'date':
            cleanup_id.date_cleanup_type()
