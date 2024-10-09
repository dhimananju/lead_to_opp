# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.exceptions import UserError, ValidationError
import werkzeug.utils
from datetime import datetime, timedelta

class MortgageLoan(http.Controller):

    # function to loan initial page for mortgage loan, loan template_id1 from owl component
    @http.route('/mortgage_loan', type='http',website=True, auth='public')
    def mortgage_loan(self, **kw):
        #return "Hello, world"
        return http.request.render("ti_loan_management.template_id1", {})
    
    # page to open page for user information after login, it load owl component template create_application_page
    @http.route('/create_application', type='http',website=True,  auth='user',csrf=False)
    def create_application(self, **kw):
        return http.request.render("ti_loan_management.create_application_page", {})
    
    #get country codes
    @http.route('/get_country_codes', type='json', auth='public')
    def get_country_codes(self):
        # Query the res.country model to get all country names and ISO codes
        countries = request.env['res.country'].search([])

        # Prepare the list of countries and their codes
        country_list = []
        for country in countries:
            country_list.append({
                'name': country.name,
                'code': country.id  # ISO country code
            })

        return country_list
    
    #get userinfo
    @http.route('/getUserInfo', type='json', auth='public')
    def getUserInfo(self):
        result = self.checkifuserexist()
        if result:
            #fetch contact information
            #contactInfo = request.env['res.partner'].sudo().browse(result.id)
            contactInfo = request.env['res.partner'].sudo().browse(result.id)
            if contactInfo.exists():
                    #return contactInfo.street
                    contacts = {
                        'name' : contactInfo.name,
                        'first_name':contactInfo.first_name,
                        'last_name':contactInfo.last_name,
                        'email':contactInfo.email,
                        'date_of_birth':contactInfo.DOB,
                        'title':contactInfo.title.name,
                        'ppsn':contactInfo.ppsn,
                        'nationality':contactInfo.nationality,
                        'phone':contactInfo.phone,
                        'mobile':contactInfo.mobile,
                        'address_line1':contactInfo.street,
                        'address_line2':contactInfo.street2,
                        'eircode':contactInfo.zip,
                        'country':contactInfo.country_id.id,
                        'county':contactInfo.state_id.name,
                        'gender':contactInfo.gender,
                        'residential_status':contactInfo.residential_status,
                        'years_living_current_address':contactInfo.years_living_current_address,
                        'years_resident':contactInfo.years_residence_ireland,

                        'employment_status':contactInfo.emp_status,
                        'employment_sector':contactInfo.emp_sector,
                        'occupation':contactInfo.occupation,
                        'employment_industry':contactInfo.emp_industry,
                        'lenght_of_current_job':contactInfo.length_emp,
                        'employer_name':contactInfo.emp_name,

                    }
                    return contacts
        else:
            return False
        
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
    
     # thankyou page
    @http.route('/thankyou', type='http',website=True, auth='user')
    def thankyou(self, **kw):
        #return "Hello, world"
        return http.request.render("ti_loan_management.thankyou", {})
    
    # redirect suer to create application page after login
    @http.route('/web/login', type='http', auth='public', website=True)
    def web_login(self, redirect=None, **kwargs):
        # Call the original login method from the web controller
        if request.httprequest.method == 'POST':
            login = request.params.get('login')
            password = request.params.get('password')
            db = request.session.db
            
            # Authenticate the user
            uid = request.session.authenticate(db, login, password)

            if uid:
                # Redirect to your specific page upon successful login
                return request.redirect('/create_application')

        # If login failed or the method is not POST, return the login page
        return request.render('web.login', {'error': 'Invalid login credentials'})

    # create user account
    @http.route('/register', type='http', auth='public', website=True)
    def register(self, **kwargs):
        if request.httprequest.method == 'POST':
            name = kwargs.get('name')
            email = kwargs.get('email')
            password = kwargs.get('password')
            
            
            if not name or not email or not password:
                custom_context = {
                    'error_message': 'All fields are required',
                }
                return request.render('ti_loan_management.template_id1', custom_context)
            
            try:
                # Check if the email already exists
                existing_user = request.env['res.users'].sudo().search([('login', '=', email)], limit=1)
                if existing_user:
                    custom_context = {
                        'error_message': 'This Email already registered.',
                    }
                    return request.render('ti_loan_management.template_id1', custom_context)
                
                # Create the user/contact
                group1_id = request.env.ref('appsmod2.group_appsmod2_external_user')
                user = request.env['res.users'].sudo().create({
                    'name': name,
                    'login': email,
                    'email' :email,
                    'password': password,
                    'active': True,  # Activate the user by default
                    'groups_id': [(59, 0, group1_id),(6, 0, [request.env.ref('base.group_user').id])]  # Regular user group to retsrict odoo backend access
                })
                
                # redirect to login
                return request.redirect('/web/login')
            except Exception as e:
                custom_context = {
                        'error_message': str(e),
                }
                return request.render('ti_loan_management.template_id1', custom_context)
        
        return request.render('ti_loan_management.template_id1')
    
    # to get member id
    def getmemberid(self,str1, str2):
        # Get the first letters of both strings
        first_letter_str1 = str1[0] if str1 else ''
        first_letter_str2 = str2[0] if str2 else ''
        
        # Concatenate the first letters
        twostring = first_letter_str1 + first_letter_str2
        #concatenate user id 
        user = request.env.user
        userid = user.id

        result = twostring + str(userid)
        return result

    #concatenate perfix and number to make a perfect number
    def getphonenumber(self,perfix,numbner):
        # Concatenate the first letters
        number = perfix + " "+ numbner
        return number
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


    # function to add data from about us page to DB also apply validations here for mendatory fields
    @http.route('/submit_form', type='json', auth='user', methods=['POST'], website=True, csrf=False)
    def submit_form(self, **kwargs):
        # Define required fields
        if(kwargs.get('page')=='aboutus'):
            required_fields = ['title','first_name', 'last_name','perfix','local_number','perfix_personal', 'local_number_personal',
                           'date_of_birth', 'ppsn','nationality', 'terms_and_condition'
                           ]
        elif(kwargs.get('page')=="live"):
            required_fields = ['address_line1','address_line2','country','eircode','residential_status','years_living_current_address',
                           'years_resident'
                           ]
        elif(kwargs.get('page')=="job"):
            required_fields = ['employment_status','employment_sector','occupation','employment_industry','lenght_of_current_job',
                               'employer_name'
                           ]
        else:
            required_fields = []
        
        # Check if all required fields are present and not empty
        if required_fields:
            missing_fields = [field.replace('_', ' ') for field in required_fields if not kwargs.get(field)]
            if missing_fields:
                # Return validation error as JSON
                return {
                    'error': True,
                    'message': f"The following fields are required: {', '.join(missing_fields)}"
                }
        if(kwargs.get('page')=="aboutus"):
            #save this data in contact us
            #print(kwargs.get('first_name'))
            # Use Odoo's ORM to create a new record
            user = request.env.user
            loginemail = user.login

            #get contactid
            getContactID = self.checkifuserexist()
            if getContactID:
                if isinstance(getContactID.id, int):
                    partner_record = request.env['res.partner'].sudo().browse(getContactID.id)
                    if partner_record.exists():
                       
                        #get member id
                        memberid = self.getmemberid(kwargs.get('first_name'),kwargs.get('last_name'))
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
                            'member_id':memberid,
                            'email': loginemail,
                            'ppsn': kwargs.get('ppsn'),
                            'nationality': kwargs.get('nationality'),
                            'gender': kwargs.get('gender'),
                        })
                    return {
                        'success': True,
                        'message': 'Submitted successfully',
                    }
                else:
                    return {
                        'error ': True,
                        'message': 'Error occured please contact admin',
                    }
        elif(kwargs.get('page')=="live"):
                user = request.env.user
                loginemail = user.login

                #get contactid
                getContactID = self.checkifuserexist()
                if getContactID:
                    if isinstance(getContactID.id, int):
                        partner_record = request.env['res.partner'].sudo().browse(getContactID.id)
                        if partner_record.exists():
                            #return kwargs.get('country')
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
                            'message': 'Submitted successfully',
                        }
                    else:
                        return {
                            'error ': True,
                            'message': 'Error occured please contact admin',
                        }

        elif(kwargs.get('page')=="job"):
                user = request.env.user
                loginemail = user.login

                #get contactid
                getContactID = self.checkifuserexist()
                if getContactID:
                    if isinstance(getContactID.id, int):
                        partner_record = request.env['res.partner'].sudo().browse(getContactID.id)
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
                            'message': 'Submitted successfully',
                        }
                    else:
                        return {
                            'error ': True,
                            'message': 'Error occured please contact admin',
                        }

        elif(kwargs.get('page')=="finish"):
            #get contact id
            getContactID = self.checkifuserexist()
            if getContactID:
                #calculate DOB 
                dob =  self.calculate_age(kwargs.get('date_of_birth'))
                # Get data from the POST request 
                #return kwargs.get("first_time_buyer")
                record_data = {
                    'mortgage_product_id': 1,
                    'applicant_1': getContactID.id,
                    'applicant_1_age' : dob,
                    'applicant_2_age_end_of_term':dob,
                    'first_time_buyer':kwargs.get("first_time_buyer"),
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
                    
                }

                # Create the record in the custom model
                new_record = request.env['application'].sudo().create(record_data)
                if new_record:
                    return {'success': True, 'message': 'thankyou',"id":new_record.id}
                else:
                    return {'error': True, 'message': 'Error occured please contact admin',"id":""}
            else:
                return {
                            'error ': True,
                            'message': 'Error occured please contact admin',
                        } 
        else:
            return {'success': True, 'message': 'submitted successfully!'}

        
       
