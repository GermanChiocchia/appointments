# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models

class AppointmentsDiaNoLaboral(models.Model):
    _name = 'appointments.dia.no.laboral'
    _description = 'Dia no laboral'

    date_start = fields.Date(string=u'Fecha desde')
    date_end = fields.Date(string=u'Fecha hasta')
    name = fields.Char(string=u'Motivo')