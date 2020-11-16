# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class asw_dia_no_laboral(models.Model):
    _name = 'asw.dia_no_laboral'
    _description = 'Dia no laboral'

    date_start = fields.Date(
        string=u'Fecha desde',
    )

    date_end = fields.Date(
        string=u'Fecha hasta',
    )

    name = fields.Char(
        string=u'Motivo',
    )