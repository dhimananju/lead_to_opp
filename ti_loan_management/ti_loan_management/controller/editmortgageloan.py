# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.http import request
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta

class UploadDocument(http.Controller):

    
    # edit application page load
    @http.route('/editapplication',type="http" , website=True,auth="user")
    def editapplication(self,**kw):
        #check if application with id exit or not
        appinfo = request.env['application'].search([('id', '=', kw.get("id"))])
        if appinfo:
            return http.request.render("ti_loan_management.edit_mortgage_loan",{})
        else:
            raise UserError("404 not found")
        #print(kw)
        #get application data

    
    # deleteapplication page load
    @http.route('/deleteapplication',type="json" , website=True,auth="user")
    def deleteapplication(self,**kw):
        #check if application with id exit or not
        if kw.get('id'):
            appinfo = request.env['application'].search([('id', '=', kw.get("id"))])
            if appinfo:
                #delete
                 # Retrieve data to be deleted based on kwargs
                if appinfo.sudo().unlink():
                    return {
                            'success': True,
                            'message': ' Application deleted successfully.',
                        }
                else:
                    return {
                            'error': True,
                            'message': ' Error occured',
                        }
                
        else:
            raise UserError("404 not found")
        #print(kw)
        #get application data

    # edit application page load
    @http.route('/editaccount',type="http" , website=True,auth="user")
    def editaccount(self,**kw):
        #check if application with id exit or not
        getContactID = self.checkifuserexist()
        if getContactID:
            return http.request.render("ti_loan_management.edit_account",{})
        else:
            raise UserError("404 not found")
        #print(kw)
        #get application data

        
    
    #get contact id from user id
    def checkifuserexist(self):
        user = request.env.user
        userid = user.id
        userinfo = request.env['res.users'].sudo().browse(userid)
        if userinfo:
            partner_id = userinfo.partner_id
            return partner_id
        else:
            return False
    
    #concatenate perfix and number to make a perfect number
    def getphonenumber(self,perfix,numbner):
        # Concatenate the first letters
        number = perfix + " "+ numbner
        return number

    # function to add data from about us page to DB also apply validations here for mendatory fields
    @http.route('/updatedata', type='json', auth='user', methods=['POST'], website=True, csrf=False)
    def updatedata(self, **kwargs):
        # Define required fields
        required_fields = []
        required_fields = ['title','first_name', 'last_name','perfix','local_number','perfix_personal', 'local_number_personal',
                            'date_of_birth', 'ppsn','nationality'
                          ]
        
        # Check if all required fields are present and not empty
        if required_fields:
            missing_fields = [field.replace('_', ' ') for field in required_fields if not kwargs.get(field)]
            if missing_fields:
                # Return validation error as JSON
                raise ValidationError(f"The following fields are required: {', '.join(missing_fields)}")

        user = request.env.user
        loginemail = user.login

        #get contactid
        getContactID = self.checkifuserexist()
        if getContactID:
            if isinstance(getContactID.id, int):
                partner_record = request.env['res.partner'].sudo().browse(getContactID.id)
                #return partner_record
                if partner_record.exists():
                    
                    phonenumber = self.getphonenumber(kwargs.get('perfix'),kwargs.get('local_number'))
                    mobilenumber = self.getphonenumber(kwargs.get('perfix_personal'),kwargs.get('local_number_personal'))
                    # return kwargs.get('gender')
                    partner_record.write({
                        'title': kwargs.get('title'),
                        'first_name': kwargs.get('first_name'),
                        'last_name': kwargs.get('last_name'),
                        'DOB': kwargs.get('date_of_birth'),
                        'phone': phonenumber,
                        'mobile': mobilenumber,
                        'email': loginemail,
                        'ppsn': kwargs.get('ppsn'),
                        'nationality': kwargs.get('nationality'),
                        'gender': kwargs.get('gender'),
                    })
                    return {
                        'success': True,
                        'message': ' Information updated successfully',
                    }
            else:
                return {
                        'error ': True,
                        'message': 'Error occured please contact admin',
                       }
        else:
            return {
                    'error ': True,
                    'message': 'Error occured please contact admin',
                }
            

    # function to add data from about us page to DB also apply validations here for mendatory fields
    @http.route('/submitlive', type='json', auth='user', methods=['POST'], website=True, csrf=False)
    def submitlive(self, **kwargs):
        # Define required fields
        required_fields = []
        required_fields = ['address_line1','address_line2','country','eircode','residential_status','years_living_current_address',
                           'years_resident'
                           ]
        
        # Check if all required fields are present and not empty
        if required_fields:
            missing_fields = [field.replace('_', ' ') for field in required_fields if not kwargs.get(field)]
            if missing_fields:
                # Return validation error as JSON
                raise ValidationError(f"The following fields are required: {', '.join(missing_fields)}")

        user = request.env.user
        loginemail = user.login

        #get contactid
        getContactID = self.checkifuserexist()
        if getContactID:
            if isinstance(getContactID.id, int):
                partner_record = request.env['res.partner'].sudo().browse(getContactID.id)
                #return partner_record
                if partner_record.exists():
                    
                    partner_record.write({
                            'street': kwargs.get('address_line1'),
                            'street2': kwargs.get('address_line2'),
                            'zip': kwargs.get('eircode'),
                            # 'country_id ': 101,
                            'residential_status': kwargs.get('residential_status'),
                            'years_living_current_address': kwargs.get('years_living_current_address'),
                            'years_residence_ireland': kwargs.get('years_resident'),
                        })
                    return {
                        'success': True,
                        'message': 'About me information updated successfully',
                    }
            else:
                return {
                        'error ': True,
                        'message': 'Error occured please contact admin',
                       }
        else:
            return {
                    'error ': True,
                    'message': 'Error occured please contact admin',
                }
        

    # function to add data from about us page to DB also apply validations here for mendatory fields
    @http.route('/submitmyjob', type='json', auth='user', methods=['POST'], website=True, csrf=False)
    def submitmyjob(self, **kwargs):
        # Define required fields
        required_fields = []
        required_fields = ['employment_status','employment_sector','occupation','employment_industry','lenght_of_current_job',
                               'employer_name'
                           ]
        
        # Check if all required fields are present and not empty
        if required_fields:
            missing_fields = [field.replace('_', ' ') for field in required_fields if not kwargs.get(field)]
            if missing_fields:
                # Return validation error as JSON
                raise ValidationError(f"The following fields are required: {', '.join(missing_fields)}")

        user = request.env.user
        loginemail = user.login

        #get contactid
        getContactID = self.checkifuserexist()
        if getContactID:
            if isinstance(getContactID.id, int):
                partner_record = request.env['res.partner'].sudo().browse(getContactID.id)
                #return partner_record
                if partner_record.exists():
                    
                    partner_record.write({
                            'emp_status': kwargs.get('employment_status'),
                            'emp_sector': kwargs.get('employment_sector'),
                            'occupation': kwargs.get('occupation'),
                            'emp_industry': kwargs.get('employment_industry'),
                            'length_emp': kwargs.get('lenght_of_current_job'),
                            'emp_name': kwargs.get('employer_name'),
                        })
                    return {
                        'success': True,
                        'message': 'My Job information updated successfully',
                    }
            else:
                return {
                        'error ': True,
                        'message': 'Error occured please contact admin',
                       }
        else:
            return {
                    'error ': True,
                    'message': 'Error occured please contact admin',
                }
            
    # calculate DOB
    def calculate_age(self, dob):
        # Convert dob string to datetime object (assuming input format is 'YYYY-MM-DD')
        dob = datetime.strptime(dob, '%Y-%m-%d')
        # Get today's date
        today = datetime.today()
        # Calculate the difference in years
        age = today.year - dob.year
        # Adjust if the birthday has not occurred this year yet
        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1
        
        return age

    @http.route('/submitapplictaion', type='json', auth='user', methods=['POST'], website=True, csrf=False)
    def submitapplictaion(self, **kwargs):
        #get contactid
        update = request.env['application'].sudo().write({
                'livein':kwargs.get("livein"),
                'selfbuild':kwargs.get("selfbuild"),
                'application_count':kwargs.get("application_count"),
                'property_in_mind':kwargs.get("property_in_mind"),
                'property_value':kwargs.get("estimate"),
                'current_fund':kwargs.get("current_fund"),
                'average_savings':kwargs.get("average_savings"),
                'total_basic_income_1':kwargs.get("anual_gross_income"),
                'total_other_income_1':kwargs.get("variable_income"),
                'total_basic_income_2':kwargs.get("applicant2_gross_income"),
                'total_other_income_2':kwargs.get("applicant2_variable_income"),
            })
        if update:
            return {
                'success': True,
                'message': 'Application updated successfully',
            }
        else:
            return {
                'error': True,
                'message': 'Error occured please contact admin',
            }
            