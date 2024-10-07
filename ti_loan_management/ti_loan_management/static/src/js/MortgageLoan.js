/** @odoo-module */

import { useState, xml } from "@odoo/owl";
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { redirect } from "@web/core/utils/urls";
import { useService } from "@web/core/utils/hooks";
import { session } from "@web/session";

class MortgageLoan extends Component {
    //initial setup
    setup() {
        console.log()
        //set states
        this.state = useState({ isModalOpen: false, pageContent: '', userid : ""});
        //set csrf token for register page
        this.csrfToken = odoo.csrf_token;
        //get loggedin user id
        this.state.userid = session.user_id;
        this.notification = useService("notification");
        if(!this.state.userid){
            this.notification.add('Please login to create a application for loan', {
                type: 'danger', // 'danger' displays a red error notification
                sticky: true    // sticky makes the notification stay until dismissed
            });
        }
    }

    // Function to open the modal
    openModal() {
        this.state.isModalOpen = true;
    }
    
    // Function to close the modal
    closeModal() {
        this.state.isModalOpen = false;
    }

    //open create_application link
    opencreateapp(){
        const url = "/create_application";
        window.open(url); // Opens the URL in a new tab
    }
    
}
//call template
MortgageLoan.template = 'ti_loan_management.MortgageLoan';

registry.category("public_components").add("ti_loan_management.mortgage_loan", MortgageLoan);