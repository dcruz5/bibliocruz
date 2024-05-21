from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class soci(models.Model):
    _inherit ='res.users'
    _description = 'bibliocruz.soci'
    
    _sql_constraints = [
        ('email_uniq', 'unique(email)', 'El correu d\'un soci no es pot repetir.')
    ]

    name= fields.Char(string='Nom')
    cognoms= fields.Char(string='Cognoms')
    data_naixement = fields.Date(string='Data de naixement')
    edat = fields.Integer(string="Edat", compute="_compute_edat")
    es_soci = fields.Boolean(string="És soci", default=False) 
    num_carnet = fields.Char(string='Número del carnet', required=True)
    registre_ids = fields.One2many('bibliocruz.registre', 'soci_id', string="Registres")
    
    @api.depends('data_naixement')
    def _compute_edat(self):
        for estudiant in self:
            if estudiant.data_naixement:
                estudiant.edat = relativedelta(datetime.today(), estudiant.data_naixement).years

