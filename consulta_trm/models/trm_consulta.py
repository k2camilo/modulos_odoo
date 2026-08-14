from odoo import models, fields, api
import requests
import logging

_logger = logging.getLogger(__name__)


class TrmConsulta(models.Model):
    _name = 'trm.consulta'
    _description = 'Consulta TRM en Colombia'
    _rec_name = 'fecha'

    fecha = fields.Date(
        string='Fecha de consulta',
        required=True
    )

    valor_cop = fields.Float(
        string='TRM',
        compute='_compute_trm',
        digits=(12, 2)
    )

    @api.depends('fecha')
    def _compute_trm(self):

        for record in self:

            record.valor_cop = 0.0

            if not record.fecha:
                continue

            try:
                response = requests.get(
                    'https://www.datos.gov.co/resource/32sa-8pi3.json',
                    timeout=10
                )

                response.raise_for_status()

                data = response.json()

                for item in data:

                    vigencia_desde = fields.Date.to_date(
                        item['vigenciadesde'][:10]
                    )

                    vigencia_hasta = fields.Date.to_date(
                        item['vigenciahasta'][:10]
                    )

                    if vigencia_desde <= record.fecha <= vigencia_hasta:

                        record.valor_cop = float(item['valor'])

                        _logger.info(
                            "Consulta TRM: %s - %s",
                            record.fecha,
                            record.valor_cop
                        )

                        break

            except requests.exceptions.RequestException as error:

                _logger.error(
                    "Error consultando API TRM: %s",
                    error
                )