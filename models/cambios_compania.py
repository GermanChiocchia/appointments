# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class asw_cambios_compania(models.Model):
    _name = 'asw.cambio_compania'
    _description = 'Cambios compania'

    appointment_qty = fields.Integer(
        string=u'Cantidad de turnos',
    )

    appointment_duration = fields.Integer(
        string=u'Duración del turno',
    )

    start_time = fields.Float(
        string=u'Hora de inicio',
    )

    end_time = fields.Float(
        string=u'Hora de fin',
    )