from odoo import models, api
import logging
_logger = logging.getLogger(__name__)

class CrmLead(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'

    def action_apply(self):
        #result = super(CrmLead, self).action_apply()
        if self.name == 'convert':
             _logger.info('Anju first step.')
             _logger.info(self.action)
             if(self.action=="create"):
                _logger.info('Anju second step')
                _logger.info(self)
                new_contact = self.env['res.partner'].create({
                     #'x_studio_email_opt_out': self.x_studio_email_opt_out,
                     'x_studio_facebook': self.x_studio_facebook,
                     'x_studio_first_name': self.x_studio_first_name,
                     'x_studio_last_name': self.x_studio_last_name,
                     'industry_id': self.x_studio_industry_id,
                     'x_studio_linkedin_url': self.x_studio_linkedin_url,
                     'x_studio_type_of_lead': self.x_studio_type_of_lead,
                     'x_studio_source_id': self.x_studio_source_id | "source",
                     'x_studio_secondary_email': self.x_studio_secondary_email,
                })
                # Log the creation for debugging
                _logger.info('New contact created with ID: %s', new_contact.id)


                 

        
