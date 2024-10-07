/** @odoo-module */

import { useState, xml ,onMounted} from "@odoo/owl";
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { session } from "@web/session";

class ThankYou extends Component {
    //initial setup
    setup() {
        //set states
        this.state = useState({ userid : "",appid:""});
        //get loggedin user id
        this.state.userid = session.user_id;
         //set csrf token for register page
       this.csrfToken = odoo.csrf_token;

       //get query string data from mortgage loan page
       onMounted(() => {
            // Extract query parameters from the URL
            const params = new URLSearchParams(window.location.search);
            this.state.appid = params.get('id') || ' ';
        });
    }
}
//call template
ThankYou.template = 'ti_loan_management.ThankYou';

registry.category("public_components").add("ti_loan_management.thankyou", ThankYou);