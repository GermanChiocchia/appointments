# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class asw_generador_turnos(models.Model):
    _name = 'asw.generador_turno'
    _description = 'Generador de turnos'

    company_id = fields.Many2one(
        string=u'Compania',
        comodel_name='res.company',
        ondelete='set null',
    )

    date_start = fields.Date(
        string=u'Fecha desde',
    )

    date_end = fields.Date(
        string=u'Fecha hasta',
    )

    state = fields.Selection(
        string='Estado',
        selection=[('borrador','Borrador'), ('procesado', 'Procesado')],
    )

    turnos_ids = fields.One2many(
        string=u'Turnos generados',
        comodel_name='asw.turno',
        inverse_name='generator_id',
    )
