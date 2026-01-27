# -*- coding: utf-8 -*-
# Part of Creyox Technologies
{
    "name": "Auto Language Translator | Language Translation Tool | Automatic Translation Tool",
    "author": "Creyox Technologies",
    "website": "https://www.creyox.com",
    "support": "support@creyox.com",
    "category": "Extra Tools",
    "summary": """
                The auto language translator tool in Odoo enables seamless and real-time translation of content within the Odoo platform, 
            supporting multiple languages to enhance global communication. It integrates with Google translator to provide accurate 
            translations, ensuring that users can effortlessly manage and interact with multilingual data. This tool helps businesses 
            expand their reach and improve user experience across different regions.
            
            Auto language translator in odoo,
            Automatic language translation,
            Real-time language translator,
            
            Language translation tool in odoo,
            Instant translation service,
            Multilingual translator,
        
            Best auto language translator in odoo,
            Real-time translation for businesses,
            Free online language translator,
            Google translation tool in odoo,
            Google language translation tool in odoo,
            Translate website content automatically,
        
            Spanish to English translator,
            French to German translation tool,
            Chinese real-time translator,
            Translate Japanese to English online,
            Arabic language translation software,
        
            Auto language translator in [City/Region],
            Localized translation service in [Language],
               """,
    "license": "OPL-1",
    "version": "19.0.0.0",
    "description":
        """
            The auto language translator tool in Odoo enables seamless and real-time translation of content within the Odoo platform, 
            supporting multiple languages to enhance global communication. It integrates with Google translator to provide accurate 
            translations, ensuring that users can effortlessly manage and interact with multilingual data. This tool helps businesses 
            expand their reach and improve user experience across different regions.
            
            Auto language translator in odoo,
            Automatic language translation,
            Real-time language translator,
            
            Language translation tool in odoo,
            Instant translation service,
            Multilingual translator,
        
            Best auto language translator in odoo,
            Real-time translation for businesses,
            Free online language translator,
            Google translation tool in odoo,
            Google language translation tool in odoo,
            Translate website content automatically,
        
            Spanish to English translator,
            French to German translation tool,
            Chinese real-time translator,
            Translate Japanese to English online,
            Arabic language translation software,
        
            Auto language translator in [City/Region],
            Localized translation service in [Language],
        """,
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/auto_lang_translator.xml",
    ],
    'external_dependencies': {
        'python': ['googletrans', 'translate'],
    },
    "installable": True,
    "auto_install": False,
    "application": True,
    "images": ["static/description/banner.png"],
    "price": "199",
    "currency": "USD",
}
