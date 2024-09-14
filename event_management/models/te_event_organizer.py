from odoo import models, fields, api
import datetime


class TeEventOrganizer(models.Model):
    _name = "te.event.organizer"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Organizer Name', required=True)
    organizer_type = fields.Selection(
        [('individual', 'Individual'), ('corporate', 'Corporate'), ('community', 'Community'), ('npo', 'NPO')],
        string='Organizer Type', required=True)
    commission = fields.Float(string='Commission')

    # event_id = fields.Many2one('event.management', string='Event', required=True)
