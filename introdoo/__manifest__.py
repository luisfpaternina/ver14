###############################################################################################
#
# Luis Felipe Paternina  
# Ing.Sistemas                                
# Odoo Dev
# 
# Cel: 3215062353
#
#
# Bogotá,Colombia
#
#
###############################################################################################

{
    'name': 'Introdoo',

    'version': '13.1',

    'author': "Luis Felipe Paternina",

    'contributors': ['Luis Felipe Paternina'],

    'website': "",

    'category': 'Trainning',

    'depends': [

        'sale_management',
        'contacts'
    ],

    'data': [
    
        'security/ir.model.access.csv',
        'views/res_company.xml',
        'views/sale_order.xml',
        'views/res_config_settings.xml',
        'wizard/wizard.xml',
        'reports/sale_order.xml',
        'data/base_automatization.xml',           
    ],
    'installable': True
}

