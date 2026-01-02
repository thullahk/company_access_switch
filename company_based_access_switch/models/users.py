from odoo import models, api, http


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def run_action_on_company_change(self, new_company_id):
        """
        Called by JS before the page reload to swap groups.
        """
        user = self.env.user

        target_company = self.env['res.company'].browse(int(new_company_id))

        # Get group XML IDs
        a_group = self.env.ref('company_based_access_switch.company_a_group', raise_if_not_found=False)
        b_group = self.env.ref('company_based_access_switch.company_b_group', raise_if_not_found=False)

        if not a_group or not b_group:
            return True

        # LOGIC: Use the 'new_company_id' passed from JS, not self.env.company

        # If switching TO Company A
        if not target_company.is_company_b:
            if a_group not in user.groups_id:
                user.write({'groups_id': [(4, a_group.id)]})
            if b_group in user.groups_id:
                user.write({'groups_id': [(3, b_group.id)]})

        # If switching TO Company B
        else:
            if b_group not in user.groups_id:
                user.write({'groups_id': [(4, b_group.id)]})
            if a_group in user.groups_id:
                user.write({'groups_id': [(3, a_group.id)]})

        return True

