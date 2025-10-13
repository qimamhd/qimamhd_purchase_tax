# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime, date
import datetime

class journal_closed(models.Model):
    _inherit = 'account.move'

    tax_expense_flag = fields.Boolean(string="مصاريف ضريبية",copy=False,)

    
   
    @api.onchange('company_id')
    def set_domain_purchase_journal(self):
        if self.type in ('in_refund','in_invoice') and self.tax_expense_flag:
            journals = self.env['account.journal'].search([('tax_expense_journal_id','=', True)])
            if journals:
                return {'domain': {'journal_id': [('id', 'in', journals.ids)]}}
            else:
                return {'domain': {'journal_id': False}}


        
    @api.onchange('company_id')
    def _default_values(self):
        # vals = super(purchase_order_getDefault, self)._default_values()
        if self.type in ('in_refund','in_invoice') and self.tax_expense_flag:
            journals = self.env['account.journal'].search([('tax_expense_journal_id','=', True)],limit=1)
             
            self.update({'journal_id':journals.id}) 
            
       