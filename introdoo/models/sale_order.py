# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime, date
import base64
import logging

class SaleOrder(models.Model):
    _inherit = 'sale.order'
