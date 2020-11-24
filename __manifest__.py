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
        'views/dia_no_laboral_view.xml',
        'views/generador_turnos_view.xml',
        'views/turno_view.xml',
        'views/res_company_view.xml',
        'views/kine_menu_view.xml',
        'security/ir.model.access.csv',
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
