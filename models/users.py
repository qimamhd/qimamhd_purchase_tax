from odoo.exceptions import UserError
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class company(models.Model):
    _inherit = 'res.users'
    
    increase_po_cost = fields.Boolean(string="نسبة زيادة التكلفة في امر الشراء")
    