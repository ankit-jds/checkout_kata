from collections import Counter
from product import Product
from constants import PRICING_RULES

class Checkout:
    def __init__(self):
        self.cart = []

    def scan(self, item_code):
        rule = PRICING_RULES.get(item_code)
        if not rule:
            raise ValueError(f"Invalid item: {item_code}")
        product = Product(item_code, **rule)
        self.cart.append(product)

    def total(self):
        counter = Counter([product.code for product in self.cart])
        total_price = 0

        for code, count in counter.items():
            rule = PRICING_RULES[code]
            unit_price = rule['unit_price']
            discount_qty = rule.get('discount_qty')
            discount_price = rule.get('discount_price')

            if discount_qty and discount_price:
                total_price += (count // discount_qty) * discount_price
                total_price += (count % discount_qty) * unit_price
            else:
                total_price += count * unit_price

        return total_price
