from odoo import models, fields, api
import datetime

class TeEventSession(models.Model):
    _name = "te.event.session"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Session Title', required=True)
    start_time = fields.Datetime(string='Start Time', required=True)
    end_time = fields.Datetime(string='End Time', required=True)
    description = fields.Text(string='Description')

    # event_id = fields.Many2one('event.management', string='Event', required=True)
    # speaker_id = fields.Many2one('res.partner', string='Speaker')
    # agenda_id = fields.Many2one('event.agenda', string='Agenda')

