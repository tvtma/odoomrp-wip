# -*- coding: utf-8 -*-
# (c) 2015 Daniel Campos <danielcampos@avanzosc.es> - Avanzosc S.L.
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields


class MrpRepair(models.Model):
    _inherit = 'mrp.repair'

    preventive_operations = fields.Many2many('preventive.machine.operation')
    idmachine = fields.Many2one('machinery', 'Machine')
    preventive = fields.Boolean('Is preventive')
