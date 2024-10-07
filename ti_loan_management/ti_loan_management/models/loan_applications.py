from odoo import api, fields, models


class loan_application(models.Model):
    _inherit = 'application'


    livein = fields.Selection([
        ('livein', 'Live In'),
        ('letout', 'Let Out')
    ], string='Are you planning to live in this property or let it out?')

    selfbuild = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string='Are you looking to do a self-build?')

    application_count = fields.Selection([
        ('yourself', 'By Yourself'),
        ('somebody', 'With someone else')
    ], string='Mortgage by yourself or with somebody?')


    property_in_mind = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string='Do you currently have a property in mind?')

    current_fund = fields.Char("How much funds do you currently have available?(in Euro)")
    average_savings = fields.Char("How much on average is the total savings each month?(in Euro)")



