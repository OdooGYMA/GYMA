# -*- coding: utf-8 -*-
{
    'name': "Gyma",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "iNBest",
    'website': "inbest.enterprises",

    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml'],
    'qweb':['static/src/xml/client_name.xml']
}
