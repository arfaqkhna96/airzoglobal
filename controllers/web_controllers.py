from odoo import http

class Airzoglobal(http.Controller):
    @http.route('/', auth='public', website=True)
    def home(self, **kwargs):
        return http.request.render('airzoglobal.home_page')

    @http.route('/about', auth='public', website=True)
    def about(self, **kwargs):
        return http.request.render('airzoglobal.about_page')

    @http.route('/careers', auth='public', website=True)
    def careers(self, **kwargs):
        return http.request.render('airzoglobal.careers_page')

    @http.route('/news', auth='public', website=True)
    def news(self, **kwargs):
        return http.request.render('airzoglobal.news_page')

    @http.route('/contact', auth='public', website=True)
    def contact(self, **kwargs):
        return http.request.render('airzoglobal.contact_page')

    @http.route('/enquiry-now', auth='public', website=True)
    def enquiry(self, **kwargs):
        return http.request.render('airzoglobal.enquiry_form')