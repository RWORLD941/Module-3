from odoo import models, fields, api
import datetime

class TeEventBudget(models.Model):
    _name = "te.event.budget"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Budget Name', required=True)
    total_budget = fields.Float(string='Total Budget', required=True)

    # spent_amount = fields.Float(string='Spent Amount', compute='_compute_spent_amount', store=True)
    # remaining_amount = fields.Float(string='Remaining Amount', compute='_compute_remaining_amount', store=True)

    # event_id = fields.Many2one('event.management', string='Event', required=True)

    # @api.depends('spent_amount')
    # def _compute_remaining_amount(self):
    #     for record in self:
    #         record.remaining_amount = record.total_budget - record.spent_amount
    #
    # @api.depends('total_budget')
    # def _compute_spent_amount(self):
    #     for record in self:
    #         # Implement logic to calculate the spent amount based on related records or expenses
    #         pass