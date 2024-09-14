from odoo import models, fields, api
import datetime

class TeEventSponsor(models.Model):
    _name = "te.event.sponsor"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Sponsor Name', required=True)
    amount = fields.Integer(string='Amount')

    # event_id = fields.Many2one('event.management', string='Event', required=True)
