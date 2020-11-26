# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class AppointmentsGeneradorTurno(models.Model):
    _name = 'appointments.generador.turno'
    _description = 'Generador de turnos'

    company_id = fields.Many2one(string=u'Compania',comodel_name='res.company',ondelete='set null')
    date_start = fields.Date(string=u'Fecha desde')
    date_end = fields.Date(string=u'Fecha hasta')
    state = fields.Selection(string='Estado',selection=[('borrador','Borrador'), ('procesado', 'Procesado')])
    turnos_ids = fields.One2many(string=u'Turnos generados',comodel_name='appointments.turno',inverse_name='generator_id')

    def generate_appointment(self, date, date_start, date_end):
        self.env['appointments.turno'].create({
            'company_id' : self.env.user.company_id.id,
            'date' : date,
            'generator_id' : self.id,
            # 'date_start' : date_start,
            # 'date_end' : date_end
        })