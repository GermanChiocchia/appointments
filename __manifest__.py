{
    'name': 'appointments',
    'summary': 'appointments Module Project',
    'version': '1.0',

    'description': """
appointments Module Project.
==============================================


    """,

    'author': 'Adrian Borella',
    'website': 'https://github.com/adriannborella',
    'license': 'AGPL-3',
    
    'category': 'Uncategorized',

    'depends': [
        'base',
    ],
    'external_dependencies': {
        'python': [
        ],
    },
    'data': [
        'views/appointments_dia_no_laboral_views.xml',
        'views/appointments_generador_turno_views.xml',
        'views/appointments_turno_views.xml',
        'views/res_company_views.xml',
        'views/appointments_menu_views.xml',
        'security/ir.model.access.csv',
        'data/timeframe_data.xml',
    ],
    'demo': [
    ],
    'js': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'images': [
    ],
    'test': [
    ],

    'installable': True
}
