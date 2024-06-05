# -*- coding: utf-8 -*-

from odoo import models, fields, api


class car(models.Model):
    _name = 'responsivecars.car'
    _description = 'responsivecars.car'

    brand = fields.Char()
    model = fields.Char()
    registration_date = fields.Date(string="Registration Date")
    motor = fields.Boolean(string="Electric", default=False)
    price = fields.Float()
    

    client_id = fields.Many2one('responsivecars.client', string='Client')


