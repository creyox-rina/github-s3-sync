# -*- coding: utf-8 -*-
# Part of Creyox Technologies
{
    'name': 'Generate Excel & PDF Report of Activity for Specific Users',
    "author": "Creyox Technologies",
    "website": "https://www.creyox.com",
    "support": "support@creyox.com",
    'category': 'Extra Tools',
    'summary': """
                    Generate Excel & PDF Report For Activity Of Users will allow to generate the PDF and Excel Report of user 
                    activity on bases of activity type like Email, Call, etc, Due date and Range like less-then, grater-then, 
                    equal-to the due date added.
                    
                    Activity Insights Report,
                    User Activity Tracker,
                    Follow-Up Activity Summary,
                    Activity Report Generator,
                    User Activity Dashboard,
                    Action Tracker Report,
                    Activity Data Export (PDF/Excel),
                    Activity Follow-Up Monitor,
                    Activity Overview Report,
                    Task & Activity Report,
                    What is the Activity Report app in Odoo?
                    How to generate user activity reports in Odoo?
                    Can I track all user activities in one place?
                    How does the Activity Report help monitor team performance?
                  """,
    'license': 'LGPL-3',
    'version': '19.0.0.0',
    'description': """
                    Generate Excel & PDF Report For Activity Of Users will allow to generate the PDF and Excel Report of user 
                    activity on bases of activity type like Email, Call, etc, Due date and Range like less-then, grater-then, 
                    equal-to the due date added.
                    
                    Activity Insights Report,
                    User Activity Tracker,
                    Follow-Up Activity Summary,
                    Activity Report Generator,
                    User Activity Dashboard,
                    Action Tracker Report,
                    Activity Data Export (PDF/Excel),
                    Activity Follow-Up Monitor,
                    Activity Overview Report,
                    Task & Activity Report,
                    What is the Activity Report app in Odoo?
                    How to generate user activity reports in Odoo?
                    Can I track all user activities in one place?
                    How does the Activity Report help monitor team performance?
                  """,
    'depends': ["base", "sale_management"],
    'data': [
        "security/ir.model.access.csv",
        "wizard/activity_report_wizard_views.xml",
        "report/activity_report.xml",
        "report/activity_template.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    "images": ["static/description/banner.png", ],
    "price": 0,
    "currency": "USD"
}
