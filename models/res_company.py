# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class res_company(models.Model):
    _inherit = 'res.company'

    timeframes_ids = fields.One2many(
        string=u'Horarios',
        comodel_name='asw.horario',
        inverse_name='company_id',
    )