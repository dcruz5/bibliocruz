# -*- coding: utf-8 -*-
# from odoo import http


# class Bibliocruz(http.Controller):
#     @http.route('/bibliocruz/bibliocruz', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bibliocruz/bibliocruz/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bibliocruz.listing', {
#             'root': '/bibliocruz/bibliocruz',
#             'objects': http.request.env['bibliocruz.bibliocruz'].search([]),
#         })

#     @http.route('/bibliocruz/bibliocruz/objects/<model("bibliocruz.bibliocruz"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bibliocruz.object', {
#             'object': obj
#         })

