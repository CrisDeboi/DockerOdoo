# -*- coding: utf-8 -*-

from odoo import models, fields, api


class equipo(models.Model):
    _name = 'jugador.equipo'
    _description = 'jugador.equipo'

    name = fields.Char()
    category = fields.Char()
    jugadores_ids = fields.One2many('jugador.jugador', 'equipo_id' ,string='Players' )
    country_id = fields.Many2one('res.country', string='country')


#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

