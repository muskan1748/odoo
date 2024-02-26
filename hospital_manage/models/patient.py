from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'  # using this model creating a table in postgres Hospital_patient
    _inherit = 'mail.thread'    # inherited to add chatter after form view sheet
    _description = 'Hospital Records'

    name = fields.Char(string="name", required=True)
    age = fields.Integer(string="age")
    is_child = fields.Boolean(string="is_child?")
    notes = fields.Text(string="notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="gender")

    @api.model
    def create(self, vals):
        res = super(HospitalPatient, self).create(vals)
        return res
