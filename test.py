
from odoo import api, fields, models



class Testsales(models.Model):
    _inherit = "sale.order"
    _description = "Sale Order"
    
    
    exchange_rate = fields.Float(string = 'Exchange Rate')
    line_items = fields.One2many('sale.order.line', 'order_id', string='Order Lines Items')

    cost_aud_per_unit  = fields.Float(string = 'Cost AUD per Unit', compute='_costUnit')
    aud_unit_price_with_margin  = fields.Float(string = 'AUD Unit PRICE with Margin')
  

    @api.depends('line_items','exchange_rate')
    def _costUnit(self):
        for orderitems in self:
            exc = 0
            exc_rate = orderitems.exchange_rate
            for line in orderitems.line_items:
                exc_val = 1/(exc_rate - 0.005)
                aud_Price = exc_val * unit_price
        
    
     

class TestPurchase(models.Model):
    _inherit = "purchase.order"
   #  _inherit = "purchase.order.line"
    _description = "Purchase Order"

    dealer_discount = fields.Float(string = 'Dealer Discount')
    
   # new_subtotal = fields.Float(string = 'New Subtotal')
  
  
    
  
    
    
    
  
    
   

   

