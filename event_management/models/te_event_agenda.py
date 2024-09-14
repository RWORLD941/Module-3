from odoo import models, fields, api
import datetime

class TeEventAgenda(models.Model):
    _name = "te.event.agenda"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Agenda Title', required=True)
    start_time = fields.Datetime(string='Start Time', required=True)
    end_time = fields.Datetime(string='End Time', required=True)
    description = fields.Text(string='Description')

    # session_ids = fields.One2many('event.session', 'agenda_id', string='Sessions')
    # event_id = fields.Many2one('event.management', string='Event', required=True)
