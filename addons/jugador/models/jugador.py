# -*- coding: utf-8 -*-

from odoo import models, fields, api


class jugador(models.Model):
    _name = 'jugador.jugador'
    _description = 'jugador.jugador'

    name = fields.Char()
    age = fields.Integer()
    equipo_id = fields.Many2one('jugador.equipo', string='team')
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
