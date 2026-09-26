"""
    Importing cartCore to check if the list is empty or 
    - CartItem represents every single row(item) in the cart which has product and line total
    - Line total is the total cost for that one CartItem
    - Line total = price of the product × quantity of that product

    It should:
        - Store products
        - store quantity
        
"""


class CartItem:
    def __init__(self, cartItemId, product, quantity):
        self.cartItemId = cartItemId
        self.product = product
        self.quantity = quantity

        # Line total
        self.__line_total = self.product.getPrice() * self.quantity

    def get_line_total(self):
        return self.__line_total
