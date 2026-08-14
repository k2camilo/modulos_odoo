from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class TrmDashboard(models.Model):
    _name = 'trm.dashboard'
    _description = 'Dashboard TRM Colombiana'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', default='Dashboard TRM')

    trm_actual =fields.Float(string='TRM Actual', compute='_compute_trm_actual', store=False)
    fecha_actualizacion = fields.Date(string='Fecha', compute='_compute_trm_actual', store=False)

    @api.depends_context('uid')
    def _compute_trm_actual(self):

        ultima_trm =self.env['trm.diaria'].search(
            [],
            order='fecha desc',
            limit=1
        )

        _logger.info("DASHBOARD - Ultima TRM encontrada: %s", ultima_trm)

        for record in self:
            if ultima_trm:
                record.trm_actual = ultima_trm.valor_cop
                record.fecha_actualizacion = ultima_trm.fecha
            else:
                record.trm_actual = 0.0
                record.fecha_actualizacion = False

