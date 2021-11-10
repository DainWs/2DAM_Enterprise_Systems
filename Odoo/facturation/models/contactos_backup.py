from odoo import models, fields, api

class Factura(models.Model):
    _name = 'prue01.factura'
    numfac = fields.Integer('Numero de la Factura', required=True)
    cliente = fields.Char('Cliente', required=True)
    lineas = fields.Many2many('prue01.lineasfactura', 'Lineas')

    total = fields.Float(compute='_compute_precio_total', string="Total de la Factura")

    @api.depends('lineas.preciolinea')
    def _compute_precio_total(self):
        price = 0.0
        for line in self.lineas:
            price += line.preciolinea
        record.total = price

    def name_get(self):
        res=[]
        for record in self:
            res.append((record.id, record.numfac))
        return res

class LineasFactura(models.Model):
    _name = 'prue01.lineasfactura'
    articulo = fields.Many2one('prue01.articulos', 'Articulo', required=True)
    cantidad = fields.Float('Cantidad', required=True)

    preciolinea = fields.Float(compute='_compute_precio', string="Total de la linea")

    @api.depends('cantidad')
    @api.depends('articulo')
    @api.depends('articulo.precio')
    def _compute_precio (self):
        for record in self:
            record.preciolinea = (record.articulo.precio * record.cantidad)

class Articulos(models.Model):
    _name = 'prue01.articulos'
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    precio = fields.Float('Precio', required=True)
    cantidad = fields.Integer('Cantidad', required=True)
    proveedor = fields.Many2one('prue01.proveedores', 'Proveedor', required=True)

    def name_get(self):
    	res=[]
    	for record in self:
    		res.append((record.id, record.nombre))
    	return res

    
class Proveedores(models.Model):
    _name = 'prue01.proveedores'
    nombre = fields.Char('Nombre', required=True)

    def name_get(self):
    	res=[]
    	for record in self:
    		res.append((record.id, record.nombre))
    	return res
