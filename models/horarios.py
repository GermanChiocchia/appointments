# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class asw_horarios(models.Model):
    _name = 'asw.horario'
    _description = 'Horarios'

    company_id = fields.Mani2one(
        string=u'Compania',
        comodel_name='res.company',
        ondelete='set null',
        default='self.env.user.company_id',
    )

    day = fields.Char(
        string=u'Dia',
    )

    enabled = fields.Boolean(
        string=u'Habilitado',
    )

    