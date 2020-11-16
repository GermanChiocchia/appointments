# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class asw_turno(models.Model):
    _name = 'asw.turno'
    _description = 'Turno'

    company_id = fields.Many2one(
        string=u'Compania',
        comodel_name='res.company',
        ondelete='set null',
    )

    date = fields.Date(
        string=u'Fecha',
    )

    date_start = fields.DateTime(
        string=u'Fecha de inicio',
    )

    date_end = fields.DateTime(
        string=u'Fecha de fin',
    )

    partner_id = fields.Many2one(
        string=u'Cliente',
        comodel_name='',
        ondelete='set null',
    )

    state = fields.Selection(
        selection=[('Borrador','Asignado','Cancelado','Finalizado')],
    )

    generator_id = fields.Many2one(
        string=u'Generador',
        comodel_name='generator',
    )