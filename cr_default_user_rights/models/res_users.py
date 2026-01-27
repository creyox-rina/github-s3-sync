# -*- coding: utf-8 -*-
from odoo import models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class ResUsers(models.Model):
    _inherit = 'res.users'

    def reset_default_access_rights(self):
        """This method assign the default user access rights to the current user."""
        self.ensure_one()

        default_groups = [
            'base.group_user',
        ]

        group_ids = []
        for group_xml_id in default_groups:
            try:
                group = self.env.ref(group_xml_id)
                if group:
                    group_ids.append(group.id)
            except:
                continue

        if not group_ids:
            raise UserError(_("No default groups found. Please check your installation."))

        self.env.cr.execute("""
            DELETE FROM res_groups_users_rel 
            WHERE uid = %s
        """, (self.id,))

        for gid in group_ids:
            self.env.cr.execute("""
                INSERT INTO res_groups_users_rel (uid, gid)
                VALUES (%s, %s)
            """, (self.id, gid))

        self.env.cr.commit()

        self.env.invalidate_all()

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }