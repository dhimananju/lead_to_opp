/** @odoo-module */

import { useState, xml ,onWillStart, onMounted} from "@odoo/owl";
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { session } from "@web/session";

class EditExpense extends Component {

    state = useState({
        appid:'',
        applicationInfo:[],
    });
    
    //initial setup
    async setup() {
        //service for notification
        this.notification = useService("notification");
        //service for rpc call
        this.rpc = useService("rpc");
        //set states
        this.state = useState({ userid : "",
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
        console.log(this.state.userid+"helo")
         //set csrf token for register page
        this.csrfToken = odoo.csrf_token;
      
        
        onWillStart(async () => {
            //get app ifnormation
            // Extract query parameters from the URL
            const params = new URLSearchParams(window.location.search);
            this.state.appid = params.get('id') || ' ';

            const appparams = {
                id: this.state.appid,
            }
            const applicatioInfo = await this.rpc("/get_application_by_id",appparams);
            this.state.applicationInfo = applicatioInfo;

            this.state.livein = this.state.applicationInfo.livein
            this.state.property_in_mind = this.state.applicationInfo.property_in_mind
            this.state.application_count = this.state.applicationInfo.application_count
            this.state.selfbuild = this.state.applicationInfo.selfbuild
            this.state.estimate = this.state.applicationInfo.property_value
            this.state.current_fund = this.state.applicationInfo.current_fund
            this.state.average_savings = this.state.applicationInfo.average_savings
            this.state.dependent = this.state.applicationInfo.employment_sector
            this.state.anual_gross_income = this.state.applicationInfo.total_basic_income_1
            this.state.variable_income = this.state.applicationInfo.total_other_income_1
            this.state.applicant2_gross_income = this.state.applicationInfo.total_basic_income_2
            this.state.applicant2_variable_income = this.state.applicationInfo.total_other_income_2
        });

        onMounted(() => {

            
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

    async submitapplictaion(){
        // Access form data
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
        }

        const url = "/submitapplictaion"
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

}
//call template
EditExpense.template = 'ti_loan_management.EditExpense';

registry.category("public_components").add("ti_loan_management.editexpense", EditExpense);