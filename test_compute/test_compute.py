from openerp import models, fields, api, _

class test_compute(models.Model):
    _name = "test.compute"
    _description = "Test Compute"
    
    @api.one
    @api.depends('line.amount')
    def _getAmount(self):
        self.amount = 0.0
        self.amount = sum(line.amount for line in self.line)
    
    name = fields.Char('Name', size=64, required=True)
    amount = fields.Float(compute='_getAmount', store=True, string='Amount', digits=(12,4))
    line = fields.One2many('test.compute.line', 'test_compute_id', 'Lines')
    
        
class test_compute_line(models.Model):
    _name = "test.compute.line"
    _description = "Test Compute Lines"
    
    @api.one
    @api.depends('qty','price')
    def _getLineAmount(self):
        self.amount = self.qty * self.price
    
    test_compute_id = fields.Many2one('test.compute', 'Test Compute', required=True)
    price = fields.Float('Price', digits=(12,4) )
    qty = fields.Float('Quantity', digits=(12,3))
    amount = fields.Float(compute='_getLineAmount', store=True, string='Amount', digits=(12,4))
    
