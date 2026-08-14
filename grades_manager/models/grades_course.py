from odoo import models, fields, api
from odoo.exceptions import ValidationError


class GradesCourse(models.Model):
    _name = 'grades.course' #nombre del modelo
    _description = 'Grades Course'
    _order = 'name'

    def _default_teacher_id(self):
        teacher = self.env['res.partner'].search([('is_teacher','=',True), ('email','=','k2camilo@gmail.com')], limit=1)
        return teacher.id

    name = fields.Char(string='Name')
    student_qty = fields.Integer(string='Student quantity')
    grades_average = fields.Float(string='Grades average')
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Is Active')
    course_start = fields.Date(string='Course Start', default=fields.Date.today())
    course_end = fields.Date(string='Course End')
    last_evaluation_date = fields.Date(string='Last Evaluation Date')
    course_icon = fields.Binary(string='Course Icon')
    course_shift = fields.Selection([('day','Day'),('night','Night')],string='Course Shift')
    teacher_id = fields.Many2one('res.partner', string='Teacher', default=_default_teacher_id)
    evaluation_ids = fields.One2many('grades.evaluation', 'course_id', string='Evaluations')
    student_ids = fields.Many2many('res.partner', 'grades_corse_students_rel',string='Students')
    state = fields.Selection([('register','Register'),('in_progrese','In Progress'),('done','Done')],
                             string='State', default='register')
    invalid_date = fields.Boolean(string='Invalid Date')

    def write(self, vals):
        if vals and 'evaluation_ids' in vals and not self.student_ids:
            raise ValidationError('Students not registered')
        result = super(GradesCourse, self).write(vals)
        return result
