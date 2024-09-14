from odoo import models, fields, api
import datetime

class TeEventVenueDate(models.Model):
    _name = "te.event.venue.date"
    _rec_name = "id"
    _order = "date"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    date = fields.Date(string='Date', required=True)
    is_available = fields.Boolean(string='Is Available', default=True)

    # venue_id = fields.Many2one('event.venue', string='Venue', required=True)
