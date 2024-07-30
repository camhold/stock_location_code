from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StockLocation(models.Model):
    _inherit = 'stock.location'

    code = fields.Char(string='Location Code', required=False, copy=False)

    # Eliminar la restricción SQL para permitir valores vacíos
    # Si deseas agregar la restricción SQL, tendrás que manejar los valores vacíos de forma especial

    #@api.constrains('code')
    #def _check_code_unique(self):
    #    for record in self:
    #        if record.code:
    #            # Buscar otros registros con el mismo código, excluyendo el registro actual
    #            duplicate_count = self.search_count([('code', '=', record.code), ('id', '!=', record.id)])
    #            if duplicate_count > 0:
    #                raise ValidationError('The location code must be unique.')
