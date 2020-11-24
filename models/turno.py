# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


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

    date_start = fields.Datetime(
        string=u'Fecha de inicio',
    )

    date_end = fields.Datetime(
        string=u'Fecha de fin',
    )

    partner_id = fields.Many2one(
        string=u'Cliente',
        comodel_name='res.partner',
        ondelete='set null',
    )

    state = fields.Selection(
        string='Estado',
        selection=[('borrador', 'Borrador'),('asignado', 'Asignado'),('cancelado', 'Cancelado'),('finalizado', 'Finalizado')],
        default='borrador',
    )

    generator_id = fields.Many2one(
        string=u'Generador',
        comodel_name='asw.generador_turno',
    )