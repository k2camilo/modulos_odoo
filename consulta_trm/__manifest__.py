# -*- coding: utf-8 -*-
{
    'name': 'TRM Colombia',
    'summary': 'Consulta de la TRM desde una API externa',
    'description': 'Modulo para consulta de intercambio de moneda USD a COP',
    'author': 'Camilo Gutierrez',
    'category': 'Accounting',
    'version': '17.0.0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/trm_dashboard_data.xml',
        'data/trm_cron.xml',
        'views/trm_diaria_views.xml',
        'views/trm_dashboard_views.xml',
        'views/trm_actions.xml',
        'views/trm_consulta_views.xml',
        'views/menu.xml',
    ],
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
}