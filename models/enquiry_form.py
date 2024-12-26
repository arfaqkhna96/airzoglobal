from odoo import http, models, fields
from odoo.http import request

class EnquiryForm(models.Model):
    _name = 'enquiry.form'
    _description = 'Enquiry Form'

    fullname = fields.Char(string="Full Name", required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone Number", required=True)
    organization = fields.Char(string="Organization")
    enquiry = fields.Selection([
        ('buyscrap', 'Buy Scrap'),
        ('sellscrap', 'Sell Scrap'),
        ('buyalloy', 'Buy Alloy'),
        ('buyaluminiumbillets', 'Buy Aluminium Billets')
    ], string="Enquiry Type", required=True)
    help = fields.Text(string="How can we help you?", required=True)


class EnquiryFormController(http.Controller):

    @http.route('/enquiry/submit', type='http', auth='public', website=True, csrf=True)
    def submit_enquiry(self, **post):
        # Validate and create a new record in enquiry.form
        if post:
            request.env['enquiry.form'].sudo().create({
                'fullname': post.get('fullname'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'organization': post.get('organization'),
                'enquiry': post.get('enquiry'),
                'help': post.get('help'),
            })
        return request.render("airzoglobal.enquiry_success_page")  # Replace with your success page template
