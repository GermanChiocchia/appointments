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
    cambio_compania_ids = fields.One2many(string=u'Cambios compania',comodel_name='appointments.cambio.compania',inverse_name='company_id')
    timeframes_ids = fields.One2many(string=u'Horarios',comodel_name='appointments.timeframe',inverse_name='company_id')
    appointment_qty = fields.Integer(string=u'Cantidad de turnos Simultaneos')
    appointment_duration = fields.Integer(string=u'Duración del turno')
    start_time = fields.Float(string=u'Hora de inicio')
    end_time = fields.Float(string=u'Hora de fin')

class AppointmentsTimeFrames(models.Model):
    _name = 'appointments.timeframe'
    _description = 'Horarios'

    company_id = fields.Many2one(string=u'Compania',comodel_name='res.company',ondelete='set null')
    day = fields.Char(string=u'Dia')
    enabled = fields.Boolean(string=u'Habilitado')

class AppointmentsCambioCompania(models.Model):
    _name = 'appointments.cambio.compania'
    _description = 'Cambios compania'

    company_id = fields.Many2one(string=u'Compania',comodel_name='res.company',ondelete='set null',default='self.env.user.company_id')
    appointment_qty = fields.Integer(string=u'Cantidad de turnos')
    appointment_duration = fields.Integer(string=u'Duración del turno')
    start_time = fields.Float(string=u'Hora de inicio')
    end_time = fields.Float(string=u'Hora de fin')
    enabled = fields.Boolean(string=u'Habilitado')
