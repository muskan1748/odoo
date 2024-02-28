{
    'name': 'hospital management',
    'author': 'odoo16',
    'website': 'www.google.com',
    'summary': 'hospital management',
    'depends':['mail'],
    'data': [
            'security/ir.model.access.csv',
            'views/menu.xml',
            'views/patient.xml'
            ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}