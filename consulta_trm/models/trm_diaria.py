from odoo import models, fields, api
import requests
from datetime import date
import logging

_logger = logging.getLogger(__name__)

class TrmDiaria(models.Model):
    _name = 'trm.diaria'
    _description = 'TRM diaria en Colombia'
    _rec_name = 'fecha'
    _order = 'fecha desc'
    _sql_constraints = [("fecha_unique",
                        "unique(fecha)",
                        "Ya existe un registro de TRM para esta fecha")]

    fecha = fields.Date(string="Fecha", required=True, index=True)
    valor_cop = fields.Float(string="TRM (COP)", required=True, digits=(12, 4))

    API_URL = "https://www.datos.gov.co/resource/32sa-8pi3.json"

    @api.model
    def obtener_trm_api(self):
        """Obtiene la TRM del día desde la API."""

        try:
            response = requests.get(
                self.API_URL,
                timeout=10
            )
            response.raise_for_status()

        except requests.exceptions.RequestException as error:
            _logger.error("Error consultando API TRM: %s", error)
            return False

        data = response.json()

        if not data:
            return False

        trm_hoy = data[0]

        valor_cop = float(trm_hoy["valor"])
        fecha = date.fromisoformat(trm_hoy["vigenciadesde"][:10])

        registro = self.search(
            [('fecha', '=', fecha)],
            limit=1
        )

        if registro:
            registro.write({
                'valor_cop': valor_cop,
            })
        else:
            self.create({
                'fecha': fecha,
                'valor_cop': valor_cop,
            })

        _logger.info("TRM actualizada correctamente: %s - %s",fecha,valor_cop)

        return True


