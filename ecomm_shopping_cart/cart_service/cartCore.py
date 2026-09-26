# This is the core of the E-commerce cart.

"""
    This is the shopping cart itself. 

    The shopping CartCore;
        - Owns CartItems
        - Adds/removes items
        - Calculates total
        - Calculates quantity
        - Clears cart
"""
from cart_service.cartItem import CartItem


class CartCore:
    def __init__(self, cartId, sessionId):
        # DEFINING THE ATTRIBUTES
        self.cartId = cartId
        self.sessionId = sessionId

        self._items = []  # this will contain the items in cartItem

        self.__total_price = 0.00
        

    # Defining the methods of this class
    # add item, remove item, count items, calculate total price, clear cart
    
    def add_item(self, _item: CartItem):
        # checking for 'worst' case
        if not self.cartId:
            return "You're not in a cart."

        # Adding item to a cart
        self._items.append(_item)

        #getting the current total price
        self.__recalculate_total()


    def remove_item(self, _item: CartItem):
        # If there's nothing in cart, display that
        if not self._items:
            return " Nothing in your cart to remove."

        if _item in self._items:
            self._items.remove(_item)
            self.__recalculate_total() 

    def get_item(self):
        return self._items

    def get_total(self):
        # Calculate total
        return self.__total_price

    def clear_cart(self):
        self._items.clear()
        self.__total_price = 0.00

    # PRIVATE for total
    def __recalculate_total(self):
        self.__total_price = sum(item.get_line_total() for item in self._items)
