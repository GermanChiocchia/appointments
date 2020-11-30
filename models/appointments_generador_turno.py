# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models

from datetime import date, datetime
from datetime import timedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT



class AppointmentsGeneradorTurno(models.Model):
    _name = 'appointments.generador.turno'
    _description = 'Generador de turnos'

    company_id = fields.Many2one(string=u'Compania',comodel_name='res.company',ondelete='set null')
    date_start = fields.Date(string=u'Fecha desde')
    date_end = fields.Date(string=u'Fecha hasta')
    state = fields.Selection(string='Estado',selection=[('borrador','Borrador'), ('procesado', 'Procesado')])
    turnos_ids = fields.One2many(string=u'Turnos generados',comodel_name='appointments.turno',inverse_name='generator_id')

    @api.onchange('date_start')
    def onchange_date_start(self):
        if self.date_start:
            self.date_end = self.date_start

    def generate_appointment(self, date):
        self.env['appointments.turno'].create({
            'company_id' : self.env.user.company_id.id,
            'date' : date,
            'generator_id' : self.id,
            # 'date_start' : date_start,
            # 'date_end' : date_end
        })

    def appointment_generator(self):
        dif = abs(self.date_start - self.date_end) + timedelta(days=1)

        for days_offset in range(dif.days):
            day = self.date_start + timedelta(days=days_offset)        
            self.generate_appointment(day)