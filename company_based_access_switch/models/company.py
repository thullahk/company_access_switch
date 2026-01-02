from odoo import models,fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    is_company_b = fields.Boolean('Is Company B?')