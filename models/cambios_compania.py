# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class asw_cambios_compania(models.Model):
    _name = 'asw.cambio_compania'
    _description = 'Cambios compania'

    appointment_qty = fields.Integer(
        string=u'Cantidad de turnos',
        #compute='_compute_appointment_qty',
    )

    appointment_duration = fields.Integer(
        string=u'Duración del turno',
        compute='_compute_appointment_duration',
    )

    start_time = fields.Float(
        string=u'Hora de inicio',
        required='True',            #depende de que campos son calculados!
    )

    end_time = fields.Float(
        string=u'Hora de fin',
    )

    @api.depends('start_time','end_time')
    def _compute_appointment_duration(self):
        for record in self:
            duration = record.end_time - record.start_time
            record.appointment_duration = duration