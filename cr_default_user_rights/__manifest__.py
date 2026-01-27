# -*- coding: utf-8 -*-
{
    'name': 'Reset Default Access Rights of User | Reset Default User Rights | Set default rights to the user',
    'description': """
                The cr_default_user_rights module for Odoo lets administrators reset a user’s permissions to the default settings 
                with one click. It adds a “Reset Default Access Rights” button in the user form view, so custom modifications to access 
                rights can be undone and restored to the original defaults.
 
                Reset the default access rights to any user,
                Reset Default User Rights,
                Reset Default User Rights in Odoo,
                Reset default user rights to the current user,
                Set default rights to the user,
                Assign default access rights to the user,
                Set default access right to the user,
                Reset access rights of the user,
                Assign default user rights to the user,
                What is the cr_default_user_rights module in Odoo?
                How to reset user access rights to default in Odoo?
                Why use the Default User Rights app?
                Can this app restore original permissions automatically?
                How does cr_default_user_rights improve user management?
    """,
    'sequence': '1',
    'summary': """
                The cr_default_user_rights module for Odoo lets administrators reset a user’s permissions to the default settings 
                with one click. It adds a “Reset Default Access Rights” button in the user form view, so custom modifications to access 
                rights can be undone and restored to the original defaults.
 
                Reset the default access rights to any user,
                Reset Default User Rights,
                Reset Default User Rights in Odoo,
                Reset default user rights to the current user,
                Set default rights to the user,
                Assign default access rights to the user,
                Set default access right to the user,
                Reset access rights of the user,
                Assign default user rights to the user,
                What is the cr_default_user_rights module in Odoo?
                How to reset user access rights to default in Odoo?
                Why use the Default User Rights app?
                Can this app restore original permissions automatically?
                How does cr_default_user_rights improve user management?
    """,
    'version': '19.0.0.0',
    "license": "OPL-1",
    'price': '20.0',
    'currency': 'USD',
    'author': 'Creyox Technologies',
    'website': 'https://creyox.com',
    "category": "Extra Tools",
    'depends': ['base'],
    'data': [
        'views/res_users_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
