{
    'name': 'Responsive Cars',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Módulo para gestionar coches responsives',
    'description': """
        Descripción detallada del módulo de coches responsivos.
    """,
    'author': 'Tu Nombre',
    'website': 'http://www.tusitio.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/car.xml',
        'views/client.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
