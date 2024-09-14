from odoo import models, fields, api
import datetime

class TeEventSpeaker(models.Model):
    _name = "te.event.speaker"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Speaker Name', required=True)
    charges = fields.Integer(string='Charges')

    # event_id = fields.Many2one('event.management', string='Event', required=True)
