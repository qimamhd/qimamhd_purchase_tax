# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime, date
import datetime

class journal_closed(models.Model):
    _inherit = 'account.move'

    tax_expense_flag = fields.Boolean(string="مصاريف ضريبية",copy=False,)

    
   
    @api.onchange('tax_expense_flag')
    def set_domain_purchase_journal(self):
        if self.type in ('in_refund','in_invoice') :
            if self.tax_expense_flag:
                journals = self.env['account.journal'].search([('tax_expense_journal_id','=', True)])
                if journals:
                    return {'domain': {'journal_id': [('id', 'in', journals.ids)]}}
            else:

                journals = self.env['account.journal'].search([('type','=','purchase')])

                return {'domain': {'journal_id':  [('id', 'in', journals.ids)]}}


        
    @api.onchange('tax_expense_flag')
    def _default_values(self):
        # vals = super(purchase_order_getDefault, self)._default_values()
        if self.type in ('in_refund','in_invoice'):
            if self.tax_expense_flag:
                journals = self.env['account.journal'].search([('tax_expense_journal_id','=', True)],limit=1)
                
                self.update({'journal_id':journals.id}) 
            else:
                journals = self.env['account.journal'].search([('type','=','purchase')],limit=1)
                
                self.update({'journal_id':journals.id}) 

        