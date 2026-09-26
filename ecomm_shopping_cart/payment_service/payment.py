"""
    Payment actually indicates for an Order's transaction. So therefore, it will;
        - Process payment
        - Be owned by an Order
"""
from order_service.orders import Orders


class Payment:
    def __init__(self, paymentId, method, order: Orders):
        self.paymentId = paymentId
        self.method = method
        self.order = order
        self.amount = order.calculate_total_order()
        self.is_sucessful = False

    def process_payment(self):
        # self.payment = [(item * order) for order in order]
        # return self.payment

        # Payment uses the Order’s total.
        self.is_sucessful = True
        return self.is_sucessful

    def refund(self):
        return self.is_sucessful

    def check_success(self):
        return self.is_sucessful
