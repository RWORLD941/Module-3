from odoo import models, fields, api
import datetime

class TeEventVenue(models.Model):
    _name = "te.event.venue"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Venue Name', required=True)
    location = fields.Char(string='Location')
    capacity = fields.Integer(string='Capacity')

    # available_dates = fields.Many2many('event.venue.date', string='Available Dates')
