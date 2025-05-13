class Product:
    def __init__(self, code, unit_price, discount_qty=None, discount_price=None):
        self.code = code
        self.unit_price = unit_price
        self.discount_qty = discount_qty
        self.discount_price = discount_price
