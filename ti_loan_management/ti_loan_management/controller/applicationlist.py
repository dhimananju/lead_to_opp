# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.http import request

class ApplicationList(http.Controller):


    # thankyou page
    @http.route('/list_mortgage_loan', type='http',website=True, auth='user')
    def list_mortgage_loan(self, **kw):
        #return "Hello, world"
        return http.request.render("ti_loan_management.list_mortgage_loan", {})
    
    
     # application list page page
    @http.route('/get_applications_list', type='json',website=True, auth='public')
    def get_applications_list(self, **kw):
        #get user id
        user = request.env.user
        userid = user.id
        # get application list by assignee id
        applist = request.env['application'].search([('assignee', '=', userid)])

        # Prepare the list of countries and their codes
        applicationlist = []
        for applists in applist:
            applicationlist.append({
                'id': applists.id,
                'first_time_buyer': applists.first_time_buyer,
                'mortgage_product_id': applists.mortgage_product_id,
                'livein': applists.livein,
                'selfbuild': applists.selfbuild,
                'application_count': applists.application_count,
                'property_in_mind': applists.property_in_mind,
                'property_value': applists.property_value,
                'current_fund': applists.current_fund,
                'average_savings': applists.average_savings,
                'total_basic_income_1': applists.total_basic_income_1,
                'total_other_income_1': applists.total_other_income_1,
                'total_basic_income_2': applists.total_basic_income_2,
                'total_other_income_2': applists.total_other_income_2,
            })

        return applicationlist
    
    @http.route('/get_application_by_id', type='json', website=True, auth='public')
    def get_application_by_id(self, **kw):
        #return kw.get("id")
        if kw.get("id"):
            # get application list by assignee id
            applists = request.env['application'].search([('id', '=', kw.get("id"))])
            #return appid
            if applists.exists():
                    applicationlist = {
                        'id': applists.id,
                        'first_time_buyer': applists.first_time_buyer,
                        'mortgage_product_id': applists.mortgage_product_id,
                        'livein': applists.livein,
                        'selfbuild': applists.selfbuild,
                        'application_count': applists.application_count,
                        'property_in_mind': applists.property_in_mind,
                        'property_value': applists.property_value,
                        'current_fund': applists.current_fund,
                        'average_savings': applists.average_savings,
                        'total_basic_income_1': applists.total_basic_income_1,
                        'total_other_income_1': applists.total_other_income_1,
                        'total_basic_income_2': applists.total_basic_income_2,
                        'total_other_income_2': applists.total_other_income_2,
                    }

                    return applicationlist
            else:
                return False
        else:
             return False