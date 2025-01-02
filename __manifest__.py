{
    'name': 'AIRZO GLOBAL',
    'description': 'Arizo Global is a dynamic and dependable metal trading corporation headquartered in the exciting city of the United Arab Emirates. We have quickly emerged as a prominent player in the global metal market in various fields such as auto parts, lawn equipment, cable wires, electrical wiring, and plumbing fixtures and pipe, known for our unwavering commitment to excellence, integrity, and customer satisfaction, with a strong foundation in the industry.',
    'depends': ['base', 'web', 'website'],
    'author': 'Neeraj M',
    'category': 'Bussiness',
    'data': [
        'security/ir.model.access.csv',
        'views/navbar_template.xml',
        'views/home_page_template.xml',
        'views/about_us_template.xml',
        'views/careers_page_template.xml',
        'views/contact_page_template.xml',
        'views/news_page_template.xml',
        'views/enquiry_form_template.xml',
        'views/footer_view_template.xml',
        'views/enquiry_success_template.xml',
        'views/metal_page_template.xml',
        'views/metal_page_individual_card_templates.xml',
        'views/individual_card_display_template.xml',
        'views/products_view_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'airzoglobal/static/css/custom_design.scss',
            'airzoglobal/static/src/js/web_page.js',
        ],
    },
}
