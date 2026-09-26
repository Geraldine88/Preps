"""
    A customer is a person who;
        - has a cart 
            - has an instance of CartCore
            - does not manage cart internals
            - calls CartCore methods
        - places/has order(s)
            - Has a list of the orders
            - creates an order on checkout
        - makes/has payments
            - has list of payments
            - create payment for a specific order
            - not compute payment
        - triggers actions
            - calls methods in CartCore, Orders, Payment
            - does not perform the logic. Just calls them

        - Payment belongs to order, not customer
"""

from cart_service.cartCore import CartCore

from order_service.orders import Orders
from payment_service.payment import Payment


class Customer:
    def __init__(self, cust_Id, cust_name, cust_email):
        self.customerId = cust_Id
        self.custName = cust_name
        self.custEmail = cust_email

        #self.cart = CartCore(cust_Id, cust_email)
        self.cart = None
        self.orders = []
        self.payment = []


    # Here the customer will call the cartCore's add_item() method
    def add_to_cart(self, item):
        return self.cart.add_item(item)

    # Here the customer will call the cartCore's remove_item() method
    def remove_from_cart(self, item):
        return self.cart.remove_item(item)

    """
        Checkout is where the customer will;
            - ask cartCore for items
            - create an order
            - store order
            - clear the cart
    """
    def checkout(self):
        # items = self.cart.get_item()
        items = list(self.cart.get_item())

        order = Orders(
            order_id=f"ORD-{len(self.orders)+1}",
            customer_id=self.customerId,
            item=items
        )

        self.orders.append(order)
        self.cart.clear_cart()
        return order

    def pay(self, order, paymentId, method):
        # First, create a pyment instance for the order
        payment = Payment(paymentId, method ,order)

        # process payment
        payment.process_payment()

        order.payment = payment

        # store the payment
        self.payment.append(payment)

        order.update_status('Paid')

        return payment
         

    def get_order(self):
        return self.orders
