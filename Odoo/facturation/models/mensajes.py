from odoo import models, fields, api

class Mensaje(models.Model):
    _name = 'prue01.mensaje'
    destinatario = fields.Many2one('prue01.contactos', 'Destinatario', required=True)
    de = fields.Many2one('prue01.contactos', 'De', required=True)
    subject = fields.Char('Subject', required=True)
    mensaje = fields.Char('Mensaje', required=True)