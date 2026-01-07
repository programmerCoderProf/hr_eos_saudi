from odoo import api, models, fields


class HRPayslipLine(models.Model):
    _inherit = "hr.payslip.line"

    work_permit_expiration_date = fields.Date(
        related="employee_id.work_permit_expiration_date",
        string="Work Permit Expiration Date",
    )
    first_contract_date = fields.Date(
        related="employee_id.first_contract_date", string="First Contract Date"
    )
    service_days = fields.Integer(
        string="Service Days", compute="_compute_service_days"
    )

    @api.depends("work_permit_expiration_date", "first_contract_date")
    def _compute_service_days(self):
        for line in self:
            end=line.work_permit_expiration_date or fields.Date.today()
            line.service_days = (end - line.first_contract_date).days+1 if line.first_contract_date else 0
   