{
    'name': "Loan  Management System",
    'version': '1.0',
    'author': "Anju Dhiman",
    'category': 'Loan Management System',
    'description': """Loan Management System""",
    'sequence':-9999,
    'depends':["website","base","contacts",'appsmod2'],
    'data':[
        'views/respartner.xml',
        'views/template.xml',
        'views/uploaddocument.xml',
        'views/editmortgageloan.xml',
        'views/edit_aboutus.xml',
        'views/loan_application.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'ti_loan_management/static/img/*',
            'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css',  # Include Bootstrap Icons
            'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap',  # Include Poppins font from Google Fonts
            'ti_loan_management/static/css/style.css',
            'ti_loan_management/static/src/xml/manage/edit_expenses.xml',
            'ti_loan_management/static/src/xml/manage/edit_job.xml',
            'ti_loan_management/static/src/xml/manage/edit_live_page.xml',
            'ti_loan_management/static/src/xml/manage/edit_aboutus.xml',
            'ti_loan_management/static/src/xml/manage/editapplication.xml',
            'ti_loan_management/static/src/xml/manage/list_mortgage_loan.xml',
            'ti_loan_management/static/src/xml/thankyou.xml',
            'ti_loan_management/static/src/xml/MortgageLoan.xml',
            'ti_loan_management/static/src/xml/aboutme.xml',
            'ti_loan_management/static/src/xml/aboutmesummary.xml',
            'ti_loan_management/static/src/xml/whereilive.xml',
            'ti_loan_management/static/src/xml/whereilivesummary.xml',
            'ti_loan_management/static/src/xml/myjob.xml',
            'ti_loan_management/static/src/xml/jobsummary.xml',
            'ti_loan_management/static/src/xml/mortgageexpenses.xml',
            'ti_loan_management/static/src/xml/mortgageexpensessummary.xml',
            'ti_loan_management/static/src/xml/CreateApplication.xml',

            'ti_loan_management/static/src/js/EditExpense.js',
            'ti_loan_management/static/src/js/EditApplication.js',
            'ti_loan_management/static/src/js/ListMortgageLoan.js',
            'ti_loan_management/static/src/js/ThankYou.js',
            'ti_loan_management/static/src/js/CreateApplication.js',
            'ti_loan_management/static/src/js/MortgageLoan.js',
        ],

    },

    'installable':True,
    'auto_install': False,
    'application':True,
    'license':'LGPL-3',
}