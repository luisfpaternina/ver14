from odoo import models, fields, api, _
from datetime import datetime, date
import logging


class QualityAlert(models.Model):
    _inherit = 'quality.alert'

    nonconformity_date = fields.Date(
        string="Nonconformity date")
    nonconformity_number = fields.Char(
        string="Nonconformity number")
    is_audit = fields.Boolean(
        string="Is audit")
    is_process = fields.Boolean(
        string="Is process")
    is_documentary = fields.Boolean(
        string="Is documentary")
    is_purchases_suppliers = fields.Boolean(
        string="Purchases and suppliers")
    is_complaints = fields.Boolean(
        string="Is complaints")
    nonconformity_description = fields.Text(
        string="Description")
    nonconformity_causes = fields.Text(
        string="Causes")
    detected_by = fields.Char(
        string="Detected by")
    detected_date = fields.Date(
        string="Detected date")
    immediate_solution = fields.Text(
        string="Immediate solution")
    is_indicators = fields.Boolean(
        string="Is indicators")
