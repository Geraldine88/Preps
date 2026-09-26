"""
    'Order' represents the finalized 'CartCore'

    It;
        - own cartItems
        - owns payment
        - store order details
"""
from cart_service.cartItem import CartItem


class Orders:
    def __init__(self, order_id, customer_id, item ,status = "pending"):
        self.order_id = order_id
        self.customer_id = customer_id
        self.item = item # This is the list of CartItem from checkout
        self.status = status
        self.payment = None
        self.totalOrder = 0.00

    def calculate_total_order(self):
        return sum(item.get_line_total() for item in self.item)

    def attach_payment(self, payment):
        self.payment = payment

    def update_status(self, status):
        self.status = status
