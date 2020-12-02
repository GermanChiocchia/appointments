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
    
    def get_day(self,dey,days_offset):
        dia = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        ref = datetime.strptime('01012018', '%d%m%Y').date()
        return dia[abs(dey - ref).days % 7]

    def valida_no_laboral(self,dey):
        recs_dnl = self.env['appointments.dia.no.laboral'].search([])
        for r_dnl in range(len(recs_dnl)):
            dif_lab = abs(recs_dnl[r_dnl].date_start - recs_dnl[r_dnl].date_end + timedelta(days=1))
            for offset_dnl in range(dif_lab.days):
                dnl = recs_dnl[r_dnl].date_start + timedelta(days=offset_dnl)
                if dnl != dey:
                    return True
    
    def appointment_generator(self):
        dif = abs(self.date_start - self.date_end) + timedelta(days=1)
        recs_tf = self.env['appointments.timeframe'].search([])
        for days_offset in range(dif.days):
            dey = self.date_start + timedelta(days=days_offset)
            for i in range(len(recs_tf)):
                if (recs_tf[i].day == self.get_day(dey,days_offset)) and (recs_tf[i].enabled):
                    if self.valida_no_laboral(dey):
                        self.generate_appointment(dey)