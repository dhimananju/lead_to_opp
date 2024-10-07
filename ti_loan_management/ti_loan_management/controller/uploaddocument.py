# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.http import request

class UploadDocument(http.Controller):

     # thankyou page
    @http.route('/upload_document', type='http',website=True, auth='user')
    def upload_document(self, **kw):
        #return "Hello, world"
        appid = kw.get("appid")
        custom_context = {
            'appid': appid,
        }
        return http.request.render("ti_loan_management.upload_document", custom_context)

    