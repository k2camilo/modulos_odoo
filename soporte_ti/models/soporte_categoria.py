from odoo import models, fields

class SoporteCategoria(models.Model):
    _name = 'soporte.categoria'
    _description = 'Categoría de Soporte TI'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')