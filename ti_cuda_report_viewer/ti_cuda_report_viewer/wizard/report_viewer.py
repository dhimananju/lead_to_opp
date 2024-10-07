# -*-coding: utf-8 -*-

from odoo import models, fields


class ReportPreviewer(models.TransientModel):
    _name = "report.viewer"
    _description = "Report Previewer"

    name = fields.Char(required=True, copy=False)
    data_file = fields.Binary(required=True, copy=False)

    def open_report_preview(self):
        """Open a report preview without option to download or print it."""

        self.ensure_one()
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        url = f"{base_url}/ti_cuda_report_viewer/static/src/lib/pdfjs/web/viewer.html?file=%2Fweb%2Fcontent%3Fmodel%3D{self._name}%26field%3Ddata_file%26id%3D{self.id}"
        return {
            'name'  : "Report Preview",
            'type'      : "ir.actions.act_url",
            'url'       : url,
            'target'    : "new"
        }
