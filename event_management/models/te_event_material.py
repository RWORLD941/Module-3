from odoo import models, fields, api
import datetime

class TeEventMaterial(models.Model):
    _name = "te.event.material"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection([('handout', 'Handout'), ('brochure', 'Brochure'), ('tech', 'Tech Equipment')],
                                     string='Material Type', required=True)
    quantity = fields.Integer(string='Quantity')
    notes = fields.Text(string='Notes')

    # event_id = fields.Many2one('event.management', string='Event', required=True)
