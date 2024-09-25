from odoo import models, api
import logging
import json
import requests

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'
      
    def action_invoice_paid(self):
        """get payment state and tciekyt ref  and call redmine API function"""
        for move in self:
             _logger.info(move.payment_state)
             _logger.info(move.ref)
             if move.ref:
                if move.payment_state == "paid":
                    self.redmine_api(move.ref)
                 
                 
    """custom function to hit redmine API"""         
    def redmine_api(self,ref):
        redmineurl = "https://mypmstudio.com/issues/"+ref+".json"
        dataparams = { "issue": { "is_private": "1", "notes": "This Invoice is paid so closing the ticket", "status_id": 5 } }
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache","X-Redmine-API-Key":"eaffd4f722364a677d97e3e775eacfafc8adca82"}
        response = requests.put(redmineurl, data=json.dumps(dataparams), headers=headers)
        