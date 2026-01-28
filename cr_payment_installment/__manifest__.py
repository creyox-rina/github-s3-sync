# -*- coding: utf-8 -*-
# Part of Creyox technologies.
{
    "name": "Payment Installments | Sale Installments | Invoice Installments",
    "category": "Sales",
    "author": "Creyox Technologies",
    "website": "https://creyox.com",
    "summary": """
    The Sale & Invoice Installment Payment Odoo app allows businesses to manage customer payments 
    in flexible installments. Users can set the tenure in months, define installment amounts, apply 
    multiple down payments, and generate detailed installment reports for sales orders and invoices. 
    This module simplifies payment tracking, improves cash flow management, and provides transparent 
    reporting for customers and accounting teams.
    Installment,
        Payment Installments,
        Installment in sale,
        Installment in invoice,
        Sale Installment,
        Invoice Installment,
        Installment wise payment in sale,
        Installment wise payment in invoice,
        Make Installment payment in sale,
        Make Installment payment in invoice
        Payment Installment in odoo
        Installment Payment in odoo
        Installment in odoo
        Odoo Installment Payment Module,
        Sale and Invoice Installment Odoo,
        Odoo Payment in Multiple Installments,
        Odoo Customer Installment Management,
        Manage Down Payments and Installments Odoo,
        Odoo Installment Reports for Sales and Invoices,
        Odoo Recurring Payment Schedule,
        Odoo Tenure Based Installments,
        Flexible Payment Terms Odoo,
        Odoo Sales and Invoice Installment Tracking,
        How to manage installment payments for sales orders in Odoo?
        Can Odoo handle multiple down payments for invoices?
        How to set installment tenure and amounts in Odoo?
        Does Odoo generate installment reports for sales and invoices?
        How to track customer payments in installments in Odoo?
        Can Odoo split invoice payments into monthly installments?
        How to manage flexible payment terms for customers in Odoo?
        How does the Installment Payment module improve cash flow in Odoo?
        Can I print installment schedules for sales orders and invoices in Odoo?
        How to configure recurring or partial payments in Odoo?
    """,
    "depends": ["base", "account", "sale_management"],
    "vesion": "19.0.0.0",
    "price": 50,
    "currency": "USD",
    "license": "OPL-1",
    "description": """
        The Sale & Invoice Installment Payment Odoo app allows businesses to manage customer payments 
    in flexible installments. Users can set the tenure in months, define installment amounts, apply 
    multiple down payments, and generate detailed installment reports for sales orders and invoices. 
    This module simplifies payment tracking, improves cash flow management, and provides transparent 
    reporting for customers and accounting teams.
    Installment,
        Payment Installments,
        Installment in sale,
        Installment in invoice,
        Sale Installment,
        Invoice Installment,
        Installment wise payment in sale,
        Installment wise payment in invoice,
        Make Installment payment in sale,
        Make Installment payment in invoice
        Payment Installment in odoo
        Installment Payment in odoo
        Installment in odoo
        Odoo Installment Payment Module,
        Sale and Invoice Installment Odoo,
        Odoo Payment in Multiple Installments,
        Odoo Customer Installment Management,
        Manage Down Payments and Installments Odoo,
        Odoo Installment Reports for Sales and Invoices,
        Odoo Recurring Payment Schedule,
        Odoo Tenure Based Installments,
        Flexible Payment Terms Odoo,
        Odoo Sales and Invoice Installment Tracking,
        How to manage installment payments for sales orders in Odoo?
        Can Odoo handle multiple down payments for invoices?
        How to set installment tenure and amounts in Odoo?
        Does Odoo generate installment reports for sales and invoices?
        How to track customer payments in installments in Odoo?
        Can Odoo split invoice payments into monthly installments?
        How to manage flexible payment terms for customers in Odoo?
        How does the Installment Payment module improve cash flow in Odoo?
        Can I print installment schedules for sales orders and invoices in Odoo?
        How to configure recurring or partial payments in Odoo?
    """,
    "images": ["static/description/banner.png"],
    "data": [
        "data/cron.xml",
        "data/data.xml",
        "security/ir.model.access.csv",
        "security/access.xml",
        "wizard/create_part_payment.xml",
        "views/account_payment_installment_view.xml",
        "views/sale_payment_installment_view.xml",
        "report/report_action.xml",
        "report/report_installment.xml",
        "report/report_invoice_installment.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
