# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class ResCompany(models.Model):
    _inherit = 'res.company'

    timeframes_ids = fields.One2many(string=u'Horarios',comodel_name='appointments.appointment',inverse_name='company_id')

class AppointmentsAppointment(models.Model):
    _name = 'appointments.appointment'
    _description = 'Horarios'

    company_id = fields.Many2one(string=u'Compania',comodel_name='res.company',ondelete='set null',default='self.env.user.company_id')
    day = fields.Char(string=u'Dia')
    enabled = fields.Boolean(string=u'Habilitado')

class AppointmentsCambioCompania(models.Model):
    _name = 'appointments.cambio.compania'
    _description = 'Cambios compania'

    appointment_qty = fields.Integer(string=u'Cantidad de turnos')
    appointment_duration = fields.Integer(string=u'Duración del turno')
    start_time = fields.Float(string=u'Hora de inicio')
    end_time = fields.Float(string=u'Hora de fin')