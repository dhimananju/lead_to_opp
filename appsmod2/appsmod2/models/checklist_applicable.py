# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ChecklistApplicableApplicant1(models.Model):
    _name = "checklist.applicable.applicant1"
    _description = "Applicant 1 Applicable Checklist"

    name = fields.Char("Checklist")
    provided = fields.Boolean("Provided")
    acceptable = fields.Boolean("Acceptable")
    notes = fields.Char("Notes")
    application_id = fields.Many2one("application", "Applicant", help="Application ID")
    sequence = fields.Integer("Sequence")
    state = fields.Char("State")


class ChecklistApplicableApplicant2(models.Model):
    _name = "checklist.applicable.applicant2"
    _description = "Applicant 2 Applicable Checklist"

    name = fields.Char("Checklist")
    provided = fields.Boolean("Provided")
    acceptable = fields.Boolean("Acceptable")
    notes = fields.Char("Notes")
    application_id = fields.Many2one("application", "Applicant", help="Application ID")
    sequence = fields.Integer("Sequence")
    state = fields.Char("State")

class ChecklistSelfApplicableApplicant1(models.Model):
    _name = "checklist.self.applicable.applicant1"
    _description = "Applicant 1 Self Applicable Checklist"

    name = fields.Char("Checklist")
    provided = fields.Boolean("Provided")
    acceptable = fields.Boolean("Acceptable")
    notes = fields.Char("Notes")
    application_id = fields.Many2one("application", "Applicant", help="Application ID")
    sequence = fields.Integer("Sequence")
    state = fields.Char("State")

class ChecklistSelfApplicableApplicant2(models.Model):
    _name = "checklist.self.applicable.applicant2"
    _description = "Applicant 2 Self Applicable Checklist"

    name = fields.Char("Checklist")
    provided = fields.Boolean("Provided")
    acceptable = fields.Boolean("Acceptable")
    notes = fields.Char("Notes")
    application_id = fields.Many2one("application", "Applicant", help="Application ID")
    sequence = fields.Integer("Sequence")
    state = fields.Char("State")

class ChecklistPayeApplicableApplicant1(models.Model):
    _name = "checklist.paye.applicable.applicant1"
    _description = "Applicant 1 Paye Applicable Checklist"

    name = fields.Char("Checklist")
    provided = fields.Boolean("Provided")
    acceptable = fields.Boolean("Acceptable")
    notes = fields.Char("Notes")
    application_id = fields.Many2one("application", "Applicant", help="Application ID")
    sequence = fields.Integer("Sequence")
    state = fields.Char("State")    


class ChecklistPayeApplicableApplicant2(models.Model):
    _name = "checklist.paye.applicable.applicant2"
    _description = "Applicant 2 Paye Applicable Checklist"

    name = fields.Char("Checklist")
    provided = fields.Boolean("Provided")
    acceptable = fields.Boolean("Acceptable")
    notes = fields.Char("Notes")
    application_id = fields.Many2one("application", "Applicant", help="Application ID")
    sequence = fields.Integer("Sequence")
    state = fields.Char("State")