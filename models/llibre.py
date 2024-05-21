from odoo import models, fields, api

class llibre(models.Model):
    _description = 'bibliocruz.llibre'
    _inherit ='product.product'
        
    _sql_constraints = [
        ('isbn_uniq', 'unique(isbn)', 'El codi ISBN és únic.')
    ]

    name = fields.Char(string='Titol', required=True)
    # sinopsis -> camp product.product.description
    disponible = fields.Boolean(string="Disponible", default=True) # camp actiu
    autor_ids = fields.Many2many('res.partner', string='Autors')
    editor = fields.Char(string='Editor')
    data_publicacio = fields.Date(string="Data de publucació")
    isbn = fields.Char(string="ISBN", required=True)
    genero = fields.Selection([('misteri', 'Misteri'),('fantasia', 'Fantasia'), ('romantic', 'Romàntic'),('aventura', 'Aventura'), ('altre', 'Altre'),], string='Gènere')
    registre_ids = fields.Many2many('bibliocruz.registre', string='Registres')

    @api.constrains('isbn')
    def _check_isbn(self):
        for llibre in self:
            if llibre.isbn:
                isbn = llibre.isbn.replace('-', '').replace(' ', '')
                if len(isbn) != 13 or not isbn.isdigit():
                    raise ValueError("El formato del ISBN es incorrecto. Debe contenir 13 caracteres.")
