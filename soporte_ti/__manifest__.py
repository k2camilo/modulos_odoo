# -*- coding: utf-8 -*-
{
    'name': 'Soporte TI',
    'summary': 'Creacion de tickets de soporte',
    'description': """
        Sistema de gestión de tickets para el área de soporte TI.

        Permite gestionar:
        - Tickets de soporte
        - Categorías
        - Técnicos
        - Clientes
        - Prioridades
        - Estados
    """,
    'author': 'Camilo Gutierrez',
    'category': 'Technical',
    'version': '17.0.0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/soporte_sequence.xml',
        'views/soporte_categoria_views.xml',
        'views/soporte_actions.xml',
        'views/menu.xml',
    ],
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
}