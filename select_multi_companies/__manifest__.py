# -*- coding: utf-8 -*-
{
    'name': "select_multi_companies",
    'category': 'Odoo Plugin/Select Multi Companies',
    'summary': """
       The module will select all companies by default and disable the company selector 
       """,
    'description': """
        The module will select all companies by default and disable the company selector 
    """,

    'author': "Oliver",
    'version': '0.1',
    'license': 'OPL-1',
    'depends': ['base','web'],
    'installable': True,
    'application': True,
    'price': 10,
    'currency': 'USD',
    'assets': {
        'web.assets_backend': [
            "hh_select_all_companies/static/src/js/company_service.js"
        ],

        'web.assets_qweb': [
            "hh_select_all_companies/static/src/xml/switch_company_menu.xml"
        ],
    },
}
