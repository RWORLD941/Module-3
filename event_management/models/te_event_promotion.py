from odoo import models, fields, api
import datetime

class TeEventPromotion(models.Model):
    _name = "te.event.promotion"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Promotion Name', required=True)
    promotion_type = fields.Selection(
        [('campaign', 'Campaign'), ('advertisement', 'Advertisement'), ('social_media', 'Social Media')],
        string='Promotion Type', required=True)
    details = fields.Text(string='Details')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    # event_id = fields.Many2one('event.management', string='Event', required=True)
