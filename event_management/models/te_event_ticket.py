from odoo import models, fields, api
import datetime

class TeEventTicket(models.Model):
    _name = "te.event.ticket"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Ticket Name', required=True)
    price = fields.Integer(string='Price')

    # event_id = fields.Many2one('event.management', string='Event', required=True)
