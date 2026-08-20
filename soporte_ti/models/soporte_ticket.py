from odoo import models, fields, api

class SoporteTicket(models.Model):
    _name = 'soporte.ticket'
    _description = 'Ticket para soporte TI'
    _order = 'name desc'

    name=fields.Char(string='Referencia', required=True, copy=False, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('soporte.ticket') or 'Nuevo')
    titulo=fields.Char(string="Título", required=True)
    descripcion=fields.Text(string='Descripción')
    solicitante_id=fields.Many2one('res.users', string='Solicitante', required=True, default=lambda self: self.env.user,)
    tecnico_id=fields.Many2one('res.users', string='Técnico asignado')
    cliente_id=fields.Many2one('res.partner', string='Cliente', required=True)
    categoria_id=fields.Many2one('soporte.categoria', string='Categoria')
    prioridad=fields.Selection([('baja', 'Baja'),('media','Media'),('alta','Alta'),('urgente','Urgente')], string='Prioridad', default='media', required=True)
    fecha_creacion=fields.Datetime(string='Fecha de Creación', default=fields.Datetime.now, readonly=True)
    fecha_limite=fields.Datetime(string='Fecha Limite', required=True)
    diagnostico=fields.Text(string='Diagnostico')
    fecha_cierre=fields.Datetime(string='Fecha de cierre', required=True)
    solucion=fields.Text(string='Solucion')
    estado=fields.Selection([
        ('nuevo', 'Nuevo'),
        ('asignado', 'Asignado'),
        ('en_progreso', 'En Progreso'),
        ('resuelto', 'Resuelto'),
        ('cerrado', 'Cerrado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', default='nuevo', required=True)


