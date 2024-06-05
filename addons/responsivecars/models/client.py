# -*- coding: utf-8 -*-

from odoo import models, fields, api


class client(models.Model):
    _name = 'responsivecars.client'
    _description = 'responsivecars.client'

    name = fields.Char()
    age = fields.Integer()
    phone_number = fields.Char()
    cars_ids = fields.One2many('responsivecars.car', 'client_id' ,string='Cars' )
    country_id = fields.Many2one('res.country', string='Country')


