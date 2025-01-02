from odoo import http
from odoo.http import request

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

    @http.route('/contact', auth='public', website=True)
    def contact(self, **kwargs):
        return http.request.render('airzoglobal.contact_page')

    @http.route('/enquiry-now', auth='public', website=True)
    def enquiry(self, **kwargs):
        return http.request.render('airzoglobal.enquiry_form')

    @http.route('/tradingcategory/metal', auth='public', website=True)
    def metal(self, **kwargs):
        return http.request.render('airzoglobal.metal_category_cards')

    @http.route('/whatwetrading/any-type-of-metal', type='http', auth='public', website=True)
    def any_type_of_metal(self, **kwargs):
        return request.render('airzoglobal.card_any_type_of_metal_details')

    @http.route('/whatwetrading/auto-parts', type='http', auth='public', website=True)
    def auto_parts(self, **kwargs):
        return request.render('airzoglobal.card_auto_parts_details')

    @http.route('/whatwetrading/lawn-equipment', type='http', auth='public', website=True)
    def lawn_equipment(self, **kwargs):
        return request.render('airzoglobal.card_lawn_equipment_details')

    @http.route('/whatwetrading/aluminium-cans', type='http', auth='public', website=True)
    def aluminium_cans(self, **kwargs):
        return request.render('airzoglobal.card_aluminium_cans_details')

    @http.route('/whatwetrading/cable-wires', type='http', auth='public', website=True)
    def cable_wires(self, **kwargs):
        return request.render('airzoglobal.card_cable_wires_details')

    @http.route('/whatwetrading/plumbing-fixtures-and-pipe', type='http', auth='public', website=True)
    def plumbing_fixtures_and_pipe(self, **kwargs):
        return request.render('airzoglobal.card_plumbing_fixtures_details')

    @http.route('/whatwetrading/electrical-wiring', type='http', auth='public', website=True)
    def electrical_wiring(self, **kwargs):
        return request.render('airzoglobal.card_electrical_wiring_details')

    @http.route('/tradingcategory/ferrous-metal', type='http', auth='public', website=True)
    def ferrous_metal(self, **kwargs):
        return request.render('airzoglobal.ferrous_metal_cards')


    @http.route('/whatwetrading/iron', type='http', auth='public', website=True)
    def iron(self, **kwargs):
        return request.render('airzoglobal.card_iron_details')


    @http.route('/whatwetrading/steel', type='http', auth='public', website=True)
    def steel(self, **kwargs):
        return request.render('airzoglobal.card_steel_details')


    @http.route('/whatwetrading/aluminium', type='http', auth='public', website=True)
    def aluminium(self, **kwargs):
        return request.render('airzoglobal.card_aluminium_details')


    @http.route('/whatwetrading/copper', type='http', auth='public', website=True)
    def copper(self, **kwargs):
        return request.render('airzoglobal.card_copper_details')


    @http.route('/whatwetrading/brass', type='http', auth='public', website=True)
    def brass(self, **kwargs):
        return request.render('airzoglobal.card_brass_details')


    @http.route('/whatwetrading/nickel', type='http', auth='public', website=True)
    def nickel(self, **kwargs):
        return request.render('airzoglobal.card_nickel_details')


    @http.route('/whatwetrading/titanium', type='http', auth='public', website=True)
    def titanium(self, **kwargs):
        return request.render('airzoglobal.card_titanium_details')

    @http.route('/tradingcategory/non-ferrous-metal', type='http', auth='public', website=True)
    def non_ferrous_metal_category(self, **kwargs):
        return request.render('airzoglobal.non_ferrous_metal_category')

    @http.route('/whatwetrading/zinc', type='http', auth='public', website=True)
    def zinc(self, **kwargs):
        return request.render('airzoglobal.card_zinc_details')  # Zinc detail page without "Read More"

    @http.route('/whatwetrading/tungsten', type='http', auth='public', website=True)
    def tungsten(self, **kwargs):
        return request.render('airzoglobal.card_tungsten_details')  # Tungsten detail page without "Read More"

    @http.route('/whatwetrading/tin', type='http', auth='public', website=True)
    def tin(self, **kwargs):
        return request.render('airzoglobal.card_tin_details')  # Tin detail page without "Read More"

    @http.route('/whatwetrading/cars', type='http', auth='public', website=True)
    def cars(self, **kwargs):
        return request.render('airzoglobal.card_cars_details')  # Cars detail page without "Read More"

    @http.route('/whatwetrading/turnings', type='http', auth='public', website=True)
    def turnings(self, **kwargs):
        return request.render('airzoglobal.card_turnings_details')  # Turnings detail page without "Read More"

    @http.route('/whatwetrading/appliances', type='http', auth='public', website=True)
    def appliances(self, **kwargs):
        return request.render('airzoglobal.card_appliances_details')  # Appliances detail page without "Read More"

    @http.route('/whatwetrading/cans', type='http', auth='public', website=True)
    def cans(self, **kwargs):
        return request.render('airzoglobal.card_cans_details')  # Cans detail page without "Read More"

    @http.route('/whatwetrading/radiators', type='http', auth='public', website=True)
    def radiators(self, **kwargs):
        return request.render('airzoglobal.card_radiators_details')

    @http.route('/product/carbon-steel-sheets-coil', type='http', auth='public', website=True)
    def carbon_steel_sheets_coil(self, **kwargs):
        return request.render('airzoglobal.carbon_steel_sheets_coil_template')

    @http.route('/product/pipe-made-of-stainless-steel', type='http', auth='public', website=True)
    def pipe_made_of_stainless_steel(self):
        return request.render('airzoglobal.pipe_made_of_stainless_steel_template')

    @http.route('/product/round-bars-of-stainless-steel', type='http', auth='public', website=True)
    def round_bars_of_stainless_steel(self):
        return request.render('airzoglobal.round_bars_of_stainless_steel_template')

    @http.route('/product/shapes-of-steel-i-beam', type='http', auth='public', website=True)
    def shapes_of_steel_i_beam(self):
        return request.render('airzoglobal.shapes_of_steel_i_beam_template')
    
    @http.route('/product/silicon-steels', type='http', auth='public', website=True)
    def silicon_steels(self):
        return request.render('airzoglobal.silicon_steels_template')

    @http.route('/product/stainless-steel-coils', type='http', auth='public', website=True)
    def stainless_steel_coils(self):
        return request.render('airzoglobal.stainless_steel_coils_template')

    @http.route('/product/stainless-steel-h-beams', type='http', auth='public', website=True)
    def stainless_steel_h_beams(self):
        return request.render('airzoglobal.stainless_steel_h_beams_template')
