{
    'name': "bibliocruz",
    'summary': "Sistema de gestió de biblioteca",
    'description': "Pt10 Projecte Biblioteca",
    'author': "Daiana Cruz",
    'website': "https://github.com/dcruz5/bibliocruz",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base','product','mail', 'sale'],   
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/llibre.xml',
        'views/soci.xml',
        'views/registre.xml',
    ],
    'demo': [
        'demo/soci_demo.xml',
        'demo/llibre_demo.xml', # not working...
        #'demo/registre_demo.xml',
    ]
}

