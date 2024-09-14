from odoo import models, fields, api
import datetime

class TeEventParticipant(models.Model):
    _name = "te.event.participant"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Participant Name', required=True)

    # event_id = fields.Many2one('event.management', string='Event', required=True)
