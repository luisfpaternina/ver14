###############################################################################################
#
# Luis Felipe Paternina  - Julian Bocanegra                                
# Odoo Dev                 Odoo Consulting
# 
# Bogotá,Colombia
#
#
###############################################################################################

{
    'name': 'co customer reports',

    'version': '13.0.0.0',

    'author': "Coondev S.A.S",

    'contributors': ['Luis Felipe Paternina'],

    'website': "www.coodev.com",

    'category': 'reports',

    'depends': [

        'account_accountant',
        'base',
    ],

    'data': [
    
        'reports/invoice_report.xml',      
    ],
    'installable': True
}
