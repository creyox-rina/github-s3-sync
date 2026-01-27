# -*- coding: utf-8 -*-
{
    'name': 'Auto Cleanup',
    'version': '19.0.0.0',
    'sequence': '1',
    'description': """
                    The Auto Cleanup module for Odoo automates the process of deleting outdated records from your system, 
                    including expired sessions, old logs, and temporary data. By configuring cleanup schedules, businesses 
                    can maintain optimal system performance and reduce manual maintenance efforts. This module is particularly 
                    useful for organizations seeking to streamline data management and ensure that their Odoo environment 
                    remains efficient and clutter-free.
                    
                    Automatic Cleanup,
                    Auto Purge,
                    Auto Maintenance,
                    Scheduled Cleanup,
                    System Cleanup,
                    Automatic Data Removal,
                    Auto Clear,
                    Data Cleanup,
                    Auto Optimization,
                    Cleanup Automation,
                    What is the Auto Cleanup app in Odoo?
                    How does Auto Cleanup work in Odoo?
                    Why use Auto Cleanup for Odoo?
                    Can Auto Cleanup improve system performance?
                    How to set up Auto Cleanup schedules in Odoo?

                   """,
    'summary': """The Auto Cleanup module for Odoo automates the process of deleting outdated records from your system, 
                    including expired sessions, old logs, and temporary data. By configuring cleanup schedules, businesses 
                    can maintain optimal system performance and reduce manual maintenance efforts. This module is particularly 
                    useful for organizations seeking to streamline data management and ensure that their Odoo environment 
                    remains efficient and clutter-free.
                    
                    Automatic Cleanup,
                    Auto Purge,
                    Auto Maintenance,
                    Scheduled Cleanup,
                    System Cleanup,
                    Automatic Data Removal,
                    Auto Clear,
                    Data Cleanup,
                    Auto Optimization,
                    Cleanup Automation,
                    What is the Auto Cleanup app in Odoo?
                    How does Auto Cleanup work in Odoo?
                    Why use Auto Cleanup for Odoo?
                    Can Auto Cleanup improve system performance?
                    How to set up Auto Cleanup schedules in Odoo?""",
    "category": "Extra Tools",
    'author': 'Creyox Technologies',
    'price': 0,
    'currency': 'USD',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'data/auto_clean_data.xml',
        'security/ir.model.access.csv',
        'views/auto_clean_view.xml',
    ],
    'qweb': [],
    'images': ['static/description/banner.png'],
    'application': True,
    'installable': True,
    'auto_install': False,
}
