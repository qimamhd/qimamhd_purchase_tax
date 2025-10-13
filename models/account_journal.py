# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
 


class xx_account_journal(models.Model):
    _inherit = 'account.journal'
    
    
    tax_expense_journal_id = fields.Boolean(string="مصاريف ضريبية",copy=False,)
