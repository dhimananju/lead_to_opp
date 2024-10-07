/** @odoo-module */

import { useState, xml ,onWillStart, onMounted} from "@odoo/owl";
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { session } from "@web/session";

class EditApplication extends Component {

    //set states for countries
    state = useState({
        countries: [],
        appid:'',
        userindfo:[],
        applicationInfo:[],
    });
    
    //initial setup
    async setup() {
        //service for notification
        this.notification = useService("notification");
        //service for rpc call
        this.rpc = useService("rpc");
        console.log("Message from backend:", this.props.first_name);
        //set states
        this.state = useState({ userid : "", 
                                activeTab:"tab1",
                                perfix:"",              //about me form field
                                local_number:"",        //about me form field
                                // countrycode_personal:"",    //about me form field
                                perfix_personal:"",         //about me form field
                                local_number_personal:"",  
                                title: '',
                                first_name: '',
                                last_name: '',
                                perfix: '',
                                local_number: '',
                                perfix_personal: '',
                                local_number_personal: '',
                                date_of_birth: '',
                                ppsn: '',
                                nationality: '',

                                //where i live fields
                                address_line1:"",
                                address_line2:"",
                                // address_line3:"",
                                country:"",
                                eircode:"",
                                residential_status:"",
                                years_living_current_address:"",
                                years_resident:"",

                                //myjob
                                employment_status:"",
                                employment_sector:"",
                                occupation:"",
                                employment_industry:"",
                                lenght_of_current_job:"",
                                employer_name:"",

                                //expenses
                                property_in_mind:"no",
                                application_count:"yourself",
                                livein : "livein",
                                selfbuild : "yes",
                                estimate : "",
                                current_fund : "",
                                average_savings : "",
                                dependent : "yes",
                                anual_gross_income : "",
                                variable_income : "",
                                applicant2_gross_income:"",
                                applicant2_variable_income:"",

                              });
        //get loggedin user id
        this.state.userid = session.user_id;
         //set csrf token for register page
        this.csrfToken = odoo.csrf_token;
        //get country codes
        this.rpc = useService("rpc");
         
        
        onWillStart(async () => {
            //get country list
            const countries = await this.rpc("/get_country_codes");
            this.state.countries = countries;

            //get user ifnormation
            const userInfo = await this.rpc("/getUserInfo");
            this.state.userInfo = userInfo;
            console.log(this.state.userInfo)
            //form data        
            this.state.first_name = this.state.userInfo.first_name
            this.state.last_name = this.state.userInfo.last_name
            this.state.date_of_birth = this.state.userInfo.date_of_birth
            if(this.state.userInfo.phone && this.state.userInfo.phone!=""){
                const num1 = this.state.userInfo.phone.split(' '); 
                this.state.perfix = num1[0]
                this.state.local_number = num1[1]
            }

            if(this.state.userInfo.mobile && this.state.userInfo.mobile!=""){
                const num2 = this.state.userInfo.mobile.split(' '); 
                this.state.perfix_personal = num2[0]
                this.state.local_number_personal = num2[1]
            }
            
            this.state.title = this.state.userInfo.title
            this.state.ppsn = this.state.userInfo.ppsn
            this.state.nationality = this.state.userInfo.nationality
            this.state.gender = this.state.userInfo.gender

            //set live page state
            this.state.address_line1 = this.state.userInfo.address_line1
            this.state.address_line2 = this.state.userInfo.address_line2
            this.state.eircode = this.state.userInfo.eircode
            this.state.country = this.state.userInfo.country
            this.state.residential_status = this.state.userInfo.residential_status
            this.state.years_living_current_address = this.state.userInfo.years_living_current_address
            this.state.years_resident = this.state.userInfo.years_resident

            //set job page state
            this.state.employment_status = this.state.userInfo.employment_status
            this.state.employment_sector = this.state.userInfo.employment_sector
            this.state.occupation = this.state.userInfo.occupation
            this.state.employment_industry = this.state.userInfo.employment_industry
            this.state.lenght_of_current_job = this.state.userInfo.lenght_of_current_job
            this.state.employer_name = this.state.userInfo.employer_name

        });

        onMounted(() => {

            
        });

    }

    async submitaboutme(){
        // Access form data
        var formdata = {
            "title":this.state.title,
            "first_name":this.state.first_name,
            "last_name":this.state.last_name,
            "csrfToken":this.csrfToken,
            "perfix":this.state.perfix,
            "local_number":this.state.local_number,
            "perfix_personal":this.state.perfix_personal,
            "local_number_personal":this.state.local_number_personal,
            "date_of_birth":this.state.date_of_birth,
            "ppsn":this.state.ppsn,
            "nationality":this.state.nationality,
            "terms_and_condition":this.state.terms_and_condition,
            "page":"aboutus",
            "gender":this.state.gender,
        }

        const url = "/updatedata"
        const params = formdata
        const result = await this.rpc(url,params);
        if (result.error && result.error==true) {
            // Display the error message if validation failed
            this.notification.add(this.state.errorMessage , {
                type: 'danger', // 'danger' displays a red error notification
                sticky: false    // sticky makes the notification stay until dismissed
            });
        } else {
            if(result.success && result.success==true ){
                // Display the error message if validation failed
                this.notification.add(result.message , {
                    type: 'success', // 'danger' displays a red error notification
                    sticky: false    // sticky makes the notification stay until dismissed
                });
            }
        }
    }


    async submitlive(){
        // Access form data
        var formdata = {
            "address_line1":this.state.address_line1,
            "address_line2":this.state.address_line2,
            "country":this.state.country,
            "eircode":this.state.eircode,
            "residential_status":this.state.residential_status,
            "years_living_current_address":this.state.years_living_current_address,
            "years_resident":this.state.years_resident,
        }

        const url = "/submitlive"
        const params = formdata
        const result = await this.rpc(url,params);
        if (result.error && result.error==true) {
            // Display the error message if validation failed
            this.notification.add(this.state.errorMessage , {
                type: 'danger', // 'danger' displays a red error notification
                sticky: false    // sticky makes the notification stay until dismissed
            });
        } else {
            if(result.success && result.success==true ){
                // Display the error message if validation failed
                this.notification.add(result.message , {
                    type: 'success', // 'danger' displays a red error notification
                    sticky: false    // sticky makes the notification stay until dismissed
                });
            }
        }
    }

    async submitmyjob(){
        // Access form data
        var formdata = {
            "employment_status":this.state.employment_status,
            "employment_sector":this.state.employment_sector,
            "occupation":this.state.occupation,
            "employment_industry":this.state.employment_industry,
            "lenght_of_current_job":this.state.lenght_of_current_job,
            "employer_name":this.state.employer_name,
        }

        const url = "/submitmyjob"
        const params = formdata
        const result = await this.rpc(url,params);
        if (result.error && result.error==true) {
            // Display the error message if validation failed
            this.notification.add(this.state.errorMessage , {
                type: 'danger', // 'danger' displays a red error notification
                sticky: false    // sticky makes the notification stay until dismissed
            });
        } else {
            if(result.success && result.success==true ){
                // Display the error message if validation failed
                this.notification.add(result.message , {
                    type: 'success', // 'danger' displays a red error notification
                    sticky: false    // sticky makes the notification stay until dismissed
                });
            }
        }
    }

    //expenses tab
    // Function to update the selected option
    updateproperty(ev) {
        this.state.property_in_mind = ev.target.value
    }
    // Function to update the selected option
    applicationcount(ev) {
        this.state.application_count = ev.target.value
    }


    // Method to change the active tab
    setActiveTab(tab) {
        this.state.activeTab = tab;
    }
}
//call template
EditApplication.template = 'ti_loan_management.EditApplication';

registry.category("public_components").add("ti_loan_management.editapplication", EditApplication);