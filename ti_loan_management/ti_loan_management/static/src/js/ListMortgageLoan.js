/** @odoo-module */

import { useState, xml,onWillStart, onMounted } from "@odoo/owl";
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { session } from "@web/session";

class ListMortgageLoan extends Component {

    
    //initial setup
    setup() {
        //service for notification
        this.notification = useService("notification");
        // to make rpc call
        this.rpc = useService("rpc");
        //set states
        this.state = useState({ userid : "",applicationlist: [],});
        //get loggedin user id
        this.state.userid = session.user_id;
         //set csrf token for register page
        this.csrfToken = odoo.csrf_token;
        //load application list 
        this.loadlist();
    }

    async loadlist(){
            const applicationlist = await this.rpc("/get_applications_list");
            this.state.applicationlist = applicationlist;
    }
    editacoount(){
        const url="/editaccount"
        window.location.href = url;
    }
    editapplication(id){
        const url="/editapplication?id="+id
        window.location.href = url;
    }
    async deleteapplication(id){
        var formdata = {
            "id":id,
        }
        const result = await this.rpc('deleteapplication',formdata);
        if (result.error && result.error==true) {
            
            // Display the error message if validation failed
            this.notification.add(this.state.errorMessage , {
                type: 'danger', // 'danger' displays a red error notification
                sticky: false    // sticky makes the notification stay until dismissed
            });
            
        } else {
            if(result.success && result.success==true ){
                await this.loadlist();
                // Display the error message if validation failed
                this.notification.add(result.message , {
                    type: 'success', // 'danger' displays a red error notification
                    sticky: false    // sticky makes the notification stay until dismissed
                });
            }
        }

        // const url="/deleteapplication?id="+id
        // window.location.href = url;
    }
}
//call template
ListMortgageLoan.template = 'ti_loan_management.ListMortgageLoan';

registry.category("public_components").add("ti_loan_management.listmortgageloan", ListMortgageLoan);