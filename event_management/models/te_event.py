from odoo import models, fields, api
import datetime

class TeEvent(models.Model):
    _name = "te.event"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Event Name', required=True)
    event_type = fields.Selection(
        [('conference', 'Conference'), ('meeting', 'Meeting'), ('workshop', 'Workshop'), ('webinar', 'Webinar')],
        string='Event Type', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    location = fields.Char(string='Location')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('completed', 'Completed')],
                             string='Status', default='draft', required=True)

    # organizer_id = fields.Many2one('res.partner', string='Organizer')
    # attendee_ids = fields.Many2many('res.partner', string='Attendees')
    # venue_id = fields.Many2one('event.venue', string='Venue')
