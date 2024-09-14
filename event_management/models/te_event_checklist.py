from odoo import models, fields, api
import datetime

class TeEventChecklist(models.Model):
    _name = "te.event.checklist"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Checklist Item', required=True)
    is_done = fields.Boolean(string='Completed', default=False)
    due_date = fields.Date(string='Due Date')

    # event_id = fields.Many2one('event.management', string='Event', required=True)
