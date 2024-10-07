# -*- coding: utf-8 -*-

from odoo import fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'
    instructor  = fields.Char(String="Test",default="Hello")
    ppsn  = fields.Char(String="PPSN")
    nationality  = fields.Char(String="Nationality")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')
    residential_status = fields.Char(String="Residential Status")
    years_living_current_address = fields.Char(String="Years living at current address")
    years_residence_ireland = fields.Char(String="Years resident in Ireland")
    emp_status = fields.Char(string="Employment Status")
    emp_sector = fields.Char(string="Employment Sector")
    occupation = fields.Char(string="Occupation")
    emp_industry = fields.Char(string="Employment Industry")
    length_emp = fields.Char(string="Length of time employed in current job or self-employed")
    emp_name = fields.Char(string="Employer’s name")