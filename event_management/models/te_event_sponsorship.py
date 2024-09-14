from odoo import models, fields, api
import datetime

class TeEventSponsorship(models.Model):
    _name = "te.event.sponsorship"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Sponsorship Name', required=True)
    contribution_amount = fields.Float(string='Contribution Amount', required=True)
    contribution_date = fields.Date(string='Contribution Date', required=True)

    # event_id = fields.Many2one('event.management', string='Event', required=True)
    # sponsor_id = fields.Many2one('res.partner', string='Sponsor', required=True)
