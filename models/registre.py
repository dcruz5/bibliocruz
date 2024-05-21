from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class registre(models.Model):
    _name = 'bibliocruz.registre'
    _description = 'bibliocruz.registre'
    
    name = fields.Char(string='Nom registre')
    soci_id = fields.Many2one('res.users', string='Usuario', domain=[('es_soci', '=', True)], required=True)
    llibre_ids = fields.Many2many('product.product', string='Llibre', domain=[('disponible', '=', True)], required=True)
    num_llibres = fields.Integer(string="Nº de llibres", compute='_compute_num_llibres', store=True)
    data_registre = fields.Date(string='Data registre', default=fields.Date.today, required=True)
    data_retorn = fields.Date(string='Data de devolució', compute='_compute_data_retorn', store=True)
    estat = fields.Selection([('disponible', 'Disponible'),('prestat', 'Prestat'), ('retornat', 'Retornat')], string='Estat', default='disponible')
    observacions =  fields.Text(string='Observacions')
    
    @api.constrains('soci_id')
    def _check_prestec_max_llibres(self):
        for record in self:
            llibres_prestecs = self.env['bibliocruz.registre'].search_count([('soci_id', '=', record.soci_id.id), ('estat', '=', 'prestat')])
            if llibres_prestecs > 3:
                raise ValidationError(f"El soci {record.soci_id.name} no puc prestar més de 3 llibres.")
    
    @api.depends('llibre_ids')
    def _compute_num_llibres(self):
        for record in self:
            record.num_llibres = len(record.llibre_ids)
    
    @api.depends('data_registre')
    def _compute_data_retorn(self):
        for record in self:
            if record.data_registre:
                record.data_retorn = record.data_registre + timedelta(days=30)

    # def return_book(self):
    #     for loan in self:
    #         loan.state = 'returned'
    #         loan.book_id.borrowed = False

