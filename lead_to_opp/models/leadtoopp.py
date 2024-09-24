from odoo import models, api
import logging
_logger = logging.getLogger(__name__)

class CrmLead(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'

    def action_apply(self):
        result = super(CrmLead, self).action_apply()
        if self.name == 'convert':
             _logger.info('Anju first step.')
             _logger.info(self.action)
             if(self.action=="create"):
                _logger.info('Anju second step')
                all_fields = self.fields_get()
                # Extract the field names
                field_names = list(all_fields.keys())
                _logger.info(field_names)
                _logger.info("all fields name")

                # Access the leads selected in the wizard
                leads = self.env['crm.lead'].browse(self._context.get('active_ids', []))
                existing_contact = self.env['res.partner'].search([('email', '=', leads.email)], limit=1)
                if existing_contact:
                    # If a contact with the same email exists, log and return the existing contact
                    _logger.info('Contact with email %s already exists. Contact ID: %s', email, existing_contact.id)
                    return existing_contact
                else:
                    # Iterate over the leads and access the custom field
                    for record in leads:
                        new_contact = self.env['res.partner'].create({
                             'name': record.x_studio_first_name + " "+ record.x_studio_last_name,
                             'x_studio_email_opt_out': record.x_studio_email_opt_out,
                             'x_studio_facebook': record.x_studio_facebook,
                             'x_studio_first_name': record.x_studio_first_name,
                             'x_studio_last_name': record.x_studio_last_name,
                             'industry_id': record.x_studio_industry,
                             'x_studio_linkedin_url': record.x_studio_linkedin_url,
                             'x_studio_type_of_lead': record.x_studio_type_of_lead,
                             'x_studio_source': record.x_studio_source,
                             'x_studio_secondary_email': record.x_studio_secondary_email,
                        })
                    
                    # Log the creation for debugging
                    _logger.info('New contact created with ID: %s', new_contact.id)


                 

        
