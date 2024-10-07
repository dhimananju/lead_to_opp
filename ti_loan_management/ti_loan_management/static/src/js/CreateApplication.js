/** @odoo-module */

import { useState, xml, onWillStart, onMounted } from "@odoo/owl";
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { redirect } from "@web/core/utils/urls";
import { useService } from "@web/core/utils/hooks";
import { session } from "@web/session";

class CreateApplication extends Component {
    
    //set states for countries
    state = useState({
        countries: [],
        userInfo: []
    });

    async setup() {
        //notification service
        this.notification = useService("notification");
        //rpc service
        this.rpc = useService("rpc");
       //set states
       this.state = useState({
                            activeTab: 'tab1',   //default active tab
                            tab1Done: false,  // Completion status for Tab 1
                            tab2Done: false,  // Completion status for Tab 2
                            tab3Done: false,  // Completion status for Tab 1
                            tab4Done: false,  // Completion status for Tab 2
                            userid : "",          //session user id
                            isModalOpen: false, 

                            title:"Mr.",            //about me form field
                            first_name:"",         //about me form field
                            last_name:"",          //about me form field
                            // countrycode:"",         //about me form field
                            perfix:"",              //about me form field
                            local_number:"",        //about me form field
                            // countrycode_personal:"",    //about me form field
                            perfix_personal:"",         //about me form field
                            local_number_personal:"",    //about me form field
                            date_of_birth:"",           //about me form field
                            ppsn:"",                //about me form field
                            nationality:"",         //about me form field
                            gender:"male",              //about me form field
                            terms_and_condition:"checked", //about me form field

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
                            applicant2_variable_incom:"",

                            
                            errorMessage: null,     //error message for validation
                            successMessage: null,   //success message for validation
                            maxDate: this.getCurrentDate(), //mx date for inout type dob
                            page:"", //define page in which user is currently to show error message
                    });
       //set csrf token for register page
       this.csrfToken = odoo.csrf_token;
       //get loggedin user id
       this.state.userid = session.user_id;
       console.log(this.state.userid)
        //get country codes
       onWillStart(async () => {
            const countries = await this.rpc("/get_country_codes");
            console.log(countries)
            this.state.countries = countries;

            //get user ifnormation
            const userInfo = await this.rpc("/getUserInfo");
            this.state.userInfo = userInfo;
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
            
            this.state.title = this.state.userInfo.title || "Mr."
            this.state.ppsn = this.state.userInfo.ppsn
            this.state.nationality = this.state.userInfo.nationality
            this.state.gender = this.state.userInfo.gender || "male"
            //set live page
            this.state.address_line1 = this.state.userInfo.address_line1
            this.state.address_line2 = this.state.userInfo.address_line2
            this.state.eircode = this.state.userInfo.eircode
            this.state.country = this.state.userInfo.country
            this.state.residential_status = this.state.userInfo.residential_status
            this.state.years_living_current_address = this.state.userInfo.years_living_current_address
            this.state.years_resident = this.state.userInfo.years_resident
            //set job page
            this.state.employment_status = this.state.userInfo.employment_status
            this.state.employment_sector = this.state.userInfo.employment_sector
            this.state.occupation = this.state.userInfo.occupation
            this.state.employment_industry = this.state.userInfo.employment_industry
            this.state.lenght_of_current_job = this.state.userInfo.lenght_of_current_job
            this.state.employer_name = this.state.userInfo.employer_name

        });
        //for validation
        this.errors = useState({
            first_name: false,
            last_name: false,
            // countrycode: false,
            perfix: false,
            local_number: false,
            // countrycode_personal: false,
            perfix_personal: false,
            local_number_personal: false,
            date_of_birth: false,
            ppsn: false,
            nationality: false,
            terms_and_condition: false,
            dobError: false,
            localnumberfield: false,
            personalnumberfield: false,
            //where i live fields
            address_line1:false,
            address_line2:false,
            // address_line3:false,
            country:false,
            eircode:false,
            residential_status:false,
            years_living_current_address:false,
            years_resident:false,
            //myjob
            employment_status:false,
            employment_sector:false,
            occupation:false,
            employment_industry:false,
            lenght_of_current_job:false,
            employer_name:false,
            //expenses
            property_in_mind:false,
            application_count:false,
            livein : false,
            selfbuild : false,
            estimate : false,
            current_fund : false,
            average_savings : false,
            dependent : false,
            anual_gross_income : false,
            variable_income : false,
            applicant2_gross_income:false,
            applicant2_variable_incom:false,
        });

        //get query string data from mortgage loan page
        onMounted(() => {
            // Extract query parameters from the URL
            const params = new URLSearchParams(window.location.search);
            this.state.mortage_select = params.get('mortage_select') || 'yes';
            this.state.interest_type = params.get('interest_type') || 'yes';
            this.state.applicant_no = params.get('applicant_no') || 'yes';
        });

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
    setActiveTab(tab,page) {
        //console.log(this.state.activeTab);
        if (tab === 'tab1' && !this.state.tab1Done) {
            // If Tab 1 is not done, don't allow switching to Tab 2
            return;
        }
        if (tab === 'tab2' && !this.state.tab2Done) {
            // If Tab 1 is not done, don't allow switching to Tab 2
            return;
        }
        if (tab === 'tab3' && !this.state.tab3Done) {
            // If Tab 1 is not done, don't allow switching to Tab 2
            return;
        }
        if (tab === 'tab4' && !this.state.tab4Done) {
            // If Tab 1 is not done, don't allow switching to Tab 2
            return;
        }

        this.state.activeTab = tab;
        this.state.page = page;
        
    }
    //on click view summary button view summary
    // Function to open the modal for summary
    openModal() {
        this.state.isModalOpen = true;
    }
    
    // Function to close the modal
    closeModal() {
        this.state.isModalOpen = false;
    }
     // Function to get the current date to diable future dates in input type date
     getCurrentDate() {
        const today = new Date();
        const day = String(today.getDate()).padStart(2, '0'); // Add leading 0 if necessary
        const month = String(today.getMonth() + 1).padStart(2, '0'); // Add leading 0 if necessary
        const year = today.getFullYear();
        return `${year}-${month}-${day}`;
    }
    // Function to calculate if the user is 18 years or older
    isOver18(dob) {
        const dobDate = new Date(dob);
        const today = new Date();
        const eighteenYearsAgo = new Date(today.setFullYear(today.getFullYear() - 18));
        return dobDate <= eighteenYearsAgo;
    }
    // Validate the date of birth on form submission
    validateDOB() {
        //if dob give age leass than 18 it will give error
        if (this.state.date_of_birth && this.isOver18(this.state.date_of_birth)) {
            this.errors.dobError = false;
            return false;
        } else {
            this.errors.dobError = true;
            return true;
        }
    }

    //about me form validation
    validateForm(page) {
        // Clear previous errors
        if(page=="aboutus"){
                this.errors.first_name = !this.state.first_name;
                this.errors.last_name = !this.state.last_name;
                // this.errors.countrycode = !this.state.countrycode;
                this.errors.perfix = !this.state.perfix;
                this.errors.local_number = !this.state.local_number;
                // this.errors.countrycode_personal = !this.state.countrycode_personal;
                this.errors.perfix_personal = !this.state.perfix_personal;
                this.errors.local_number_personal = !this.state.local_number_personal;
                this.errors.date_of_birth = !this.state.date_of_birth;
                this.errors.ppsn = !this.state.ppsn;
                this.errors.nationality = !this.state.nationality;
                this.errors.terms_and_condition = !this.state.terms_and_condition;
                // If there are any errors, return false
                if (this.errors.first_name || this.errors.last_name || this.errors.perfix ||
                    this.errors.local_number || this.errors.perfix_personal || this.errors.local_number_personal ||
                    this.errors.date_of_birth || this.errors.ppsn || this.errors.nationality || this.errors.terms_and_condition
                ) {
                    return false;
                }else if (isNaN(this.state.local_number) && this.state.local_number.trim() !== "") {
                    this.errors.localnumberfield = true
                    return false;
                }else if (isNaN(this.state.local_number_personal) && this.state.local_number_personal.trim() !== "") {
                    this.errors.personalnumberfield = true
                    return false;
                }else{
                    //if DOB give age less than 18 years though error that age is less than 18
                    if(this.validateDOB()==true){
                        return false;
                    }else{
                        return true;
                    }

                    return false;
                }
        }else if(page=="live"){
                //where i live fields
                this.errors.address_line1 = !this.state.address_line1;
                this.errors.address_line2 = !this.state.address_line2;
                // this.errors.address_line3 = !this.state.address_line3;
                this.errors.country = !this.state.country;
                this.errors.eircode = !this.state.eircode;
                this.errors.residential_status = !this.state.residential_status;
                this.errors.years_living_current_address = !this.state.years_living_current_address;
                this.errors.years_resident = !this.state.years_resident;
                // If there are any errors, return false
                if (this.errors.address_line1 || this.errors.address_line2 || this.errors.country ||
                    this.errors.eircode || this.errors.residential_status || this.errors.years_living_current_address || this.errors.years_resident
                ) {
                    return false;
                }else{
                    return true;
                }
        }else if(page=="job"){
                this.errors.employment_status = !this.state.employment_status;
                this.errors.employment_sector = !this.state.employment_sector;
                this.errors.occupation = !this.state.occupation;
                this.errors.employment_industry = !this.state.employment_industry;
                this.errors.lenght_of_current_job = !this.state.lenght_of_current_job;
                this.errors.employer_name = !this.state.employer_name;
                // If there are any errors, return false
                if (this.errors.employment_status || this.errors.employment_sector || this.errors.occupation || this.errors.employment_industry ||
                    this.errors.lenght_of_current_job || this.errors.employer_name) {
                    return false;
                }else{
                    return true;
                }
        } else if(page=="finish"){
                /* this.errors.property_in_mind = !this.state.property_in_mind;
                this.errors.application_count = !this.state.application_count;
                this.errors.livein = !this.state.livein;
                this.errors.selfbuild = !this.state.selfbuild;
                this.errors.estimate = !this.state.estimate;
                this.errors.current_fund = !this.state.current_fund;
                this.errors.average_savings = !this.state.average_savings;
                this.errors.dependent = !this.state.dependent;
                this.errors.anual_gross_income = !this.state.anual_gross_income;
                this.errors.variable_income = !this.state.variable_income;
                this.errors.applicant2_gross_income = !this.state.applicant2_gross_income;
                this.errors.applicant2_variable_income = !this.state.applicant2_variable_income;
                // If there are any errors, return false
                if (this.errors.employment_status || this.errors.employment_sector || this.errors.occupation || this.errors.employment_industry ||
                    this.errors.lenght_of_current_job || this.errors.employer_name) {
                    return false;
                }else{
                    return true;
                } */
               return true;
        } 
        return false;
    }

    

    //submit form on button click and call method for rpc call
    submitaboutus(page,nexttab,currenttab){
        this.state.page = page;
        if(page=="aboutus"){
             var formdata = {
                "title":this.state.title,
                "first_name":this.state.first_name,
                "last_name":this.state.last_name,
                "csrfToken":this.csrfToken,
                // "countrycode":this.state.countrycode,
                "perfix":this.state.perfix,
                "local_number":this.state.local_number,
                // "countrycode_personal":this.state.countrycode_personal,
                "perfix_personal":this.state.perfix_personal,
                "local_number_personal":this.state.local_number_personal,
                "date_of_birth":this.state.date_of_birth,
                "ppsn":this.state.ppsn,
                "nationality":this.state.nationality,
                "terms_and_condition":this.state.terms_and_condition,
                "page":"aboutus",
                "gender":this.state.gender,
            }
        }else if(page=="live"){
            var formdata = {
                //where i live fields
                "address_line1":this.state.address_line1,
                "address_line2":this.state.address_line2,
                "country":this.state.country,
                "eircode":this.state.eircode,
                "residential_status":this.state.residential_status,
                "years_living_current_address":this.state.years_living_current_address,
                "years_resident":this.state.years_resident,
                "page":"live",
            }
        }else if(page=="job"){
            var formdata = {
                "employment_status":this.state.employment_status,
                "employment_sector":this.state.employment_sector,
                "occupation":this.state.occupation,
                "employment_industry":this.state.employment_industry,
                "lenght_of_current_job":this.state.lenght_of_current_job,
                "employer_name":this.state.employer_name,
                "page":"job",
            }
        }else if(page=="finish"){
            var formdata = {
                "property_in_mind":this.state.property_in_mind,
                "application_count":this.state.application_count,
                "livein":this.state.livein,
                "selfbuild":this.state.selfbuild,
                "estimate":this.state.estimate,
                "current_fund":this.state.current_fund,
                "average_savings":this.state.average_savings,
                "dependent":this.state.dependent,
                "anual_gross_income":this.state.anual_gross_income,
                "variable_income":this.state.variable_income,
                "applicant2_gross_income":this.state.applicant2_gross_income,
                "applicant2_variable_income":this.state.applicant2_variable_income,
                "page":"finish",
                "date_of_birth":this.state.date_of_birth,
                "first_time_buyer":this.state.mortage_select,
            }
        }
        
        //store form data so that can be accessible in senddata
        this.formdata_val = formdata
        //  Make an RPC call with form data
        if (this.validateForm(page)) {
            // Proceed with form submission 
            this.sendData(currenttab,nexttab);
        } else {
            this.state.errorMessage = "Please fill all mendatory fields";
            this.notification.add(this.state.errorMessage , {
                type: 'danger', // 'danger' displays a red error notification
                sticky: false    // sticky makes the notification stay until dismissed
            });
        }
        
        
    }

    // function to send data to the backend via an RPC call
    async sendData(currenttab,nexttab) {
        this.state.errorMessage = null;  // Reset error message
        this.state.successMessage = null;  // Reset success message
        const url = "/submit_form"
        const params = this.formdata_val
        const result = await this.rpc(url,params);
        if (result.error && result.error==true) {
            // Display the error message if validation failed
            this.state.errorMessage = result.message;
            this.notification.add(this.state.errorMessage , {
                type: 'danger', // 'danger' displays a red error notification
                sticky: false    // sticky makes the notification stay until dismissed
            });
        } else {
            if(currenttab=="tab1"){
                this.state.tab1Done = true;
                this.state.tab2Done = true;
            }else if(currenttab=="tab2"){
                this.state.tab2Done = true;
                this.state.tab3Done = true;
            }else if(currenttab=="tab3"){
                this.state.tab3Done = true;
                this.state.tab4Done = true;
            }else if(currenttab=="tab4"){
                this.state.tab1Done = true;
                this.state.tab2Done = true;
                this.state.tab3Done = true;
                this.state.tab4Done = true;
            }
            if(result.success && result.success==true && result.message=="thankyou"){
                const url = "/thankyou?id="+result.id;
                //window.open(url); // Opens the URL in a new tab
                window.location.href = url;
            }
            //swicth to next tab
            this.state.activeTab = nexttab;
        }        
    }

}

//call template
CreateApplication.template = 'ti_loan_management.CreateApplication';

registry.category("public_components").add("ti_loan_management.create_application", CreateApplication);