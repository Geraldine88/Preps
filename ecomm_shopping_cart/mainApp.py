# Let's build the app now

from cart_service.cartItem import CartItem
from cart_service.cartCore import CartCore
from customer_service.customer import Customer
from order_service.orders import Orders
from payment_service.payment import Payment
from product_service.product import Product



# ----------------------------------- CREATING A PRODUCT ------------------------------------------
"""
    Creat product by providing it's ID, NAME, PRICE
"""
product1 = Product('HS001', 'Rental Hill Mellow', 450000)
product2 = Product('HS002', 'Camel Suites', 15000000)
product3 = Product('SRV001', 'Realtor Access', 600)


# ----------------------------------- CREATING A CARTITEM -----------------------------------------
"""
    Create a CartItem that wraps a product and a quantity. One row in a cart
"""
cartItem1 = CartItem('ITEM001', product1, 2)
cartItem2 = CartItem('ITEM002', product2, 1)
cartItem3 = CartItem('ITEM003', product3, 1)


# ----------------------------------- CREATING CARTCORE ------------------------------------------
"""
    Create a cart to hold cartItems by providing cart id and session id
"""
cartCore1 = CartCore('A1', '09-25-2026 13:59')
cartCore2 = CartCore('A2', '09-30-2026 16:00')
cartCore3 = CartCore('A3', '10-21-2026 07:07')


# ----------------------------------- ADD CARTITEM TO CART ------------------------------------------
"""
    Telling cart to add/own cartItems
"""
cartCore1.add_item(cartItem1)
cartCore2.add_item(cartItem2)
cartCore3.add_item(cartItem3)


# ----------------------------------- CREATING A CUSTOMER -----------------------------------------
"""
    Now, a customer owns a cart(cartCore), a list of orders and payments

    I'll provide customer's id, name and email
"""
customer1 = Customer('CUST001', 'Jat Wall', 'jatter2w@email.com')
customer2 = Customer('CUST002', 'Lena Hevuq', 'ledao0@email.com')
customer3 = Customer('CUST003', 'Ada Ije III', 'ijebea8@email.com')


# ----------------------------------- CUSTOMER 'DOES' CHECKOUT ---------------------------------------
"""
    Customers will;
    Ask the cart for the items => create an Order => Store order => clear cart
"""
# Attach the filled carts to the customers before checkout
customer1.cart = cartCore1
customer2.cart = cartCore2
customer3.cart = cartCore3

print("DEBUG CART 1:", customer1.cart.get_item())


order1 = customer1.checkout()
order2 = customer2.checkout()
order3 = customer3.checkout()


# ----------------------------------- CREATING AN ORDER ------------------------------------------
"""
    Create order using cart items from the cart.
    Order receives orderId, customerId, list of cartItems, status

    NOTE: Orders are created automatically during checkout.
"""
# Already created above via checkout()


# ----------------------------------- CUSTOMER PAYS FOR ORDER ---------------------------------------
"""
    Since payment 'belongs to' order, we'd need the specific order, paymentId, paymentMethod
    to make payment for the order => process it => attach it to order
"""
payment1 = customer1.pay(order1, 'PAY001', 'Card')
payment2 = customer2.pay(order2, 'PAY002', 'Cash')
payment3 = customer3.pay(order3, 'PAY003', 'Check')


# ----------------------------------- STORE PAYMENT ------------------------------------------
"""
    Customer keeps list of payments and marks the order as 'Paid'
"""
# Already handled inside customer.pay()



# --------------------------------------- OUTPUT -----------------------------------------------
print("\n------------------------- CUSTOMER 1 -------------------------")
print("Customer ID:", customer1.customerId)
print("Order ID:", order1.order_id)
print("Order Total: $",order1.calculate_total_order())
print("Payment ID:", payment1.paymentId)
print("Payment Method:", payment1.method)
print("Payment Status:", payment1.check_success())

print("\n------------------------- CUSTOMER 2 -------------------------")
print("Customer ID:", customer2.customerId)
print("Order ID:", order2.order_id)
print("Order Total: $",order2.calculate_total_order())
print("Payment ID:", payment2.paymentId)
print("Payment Method:", payment2.method)
print("Payment Status:", payment2.check_success())

print("\n------------------------- CUSTOMER 3 -------------------------")
print("Customer ID:", customer3.customerId)
print("Order ID:", order3.order_id)
print("Order Total: $",order3.calculate_total_order())
print("Payment ID:", payment3.paymentId)
print("Payment Method:", payment3.method)
print("Payment Status:", payment3.check_success())

print("\n**************************** END OF PROGRAM ******************************\n")


# ----------------------------------- PRINT RECEIPTS ------------------------------------------

def print_receipt(customer, order, payment):
    print("\n**************************** RECEIPT ****************************")
    print("Customer:", customer.custName)
    print("Customer ID:", customer.customerId)
    print("Order ID:", order.order_id)
    print("Status:", order.status)
    print("\nItems Purchased:")

    for item in order.item:
        print(
            f" ==> {item.product.productName} | "
            f"Price: ${item.product.productPrice} | "
            f"Qty: {item.quantity} | "
            f"Line Total: {item.get_line_total()}"
        )

    print("\nOrder Total: $",order.calculate_total_order())
    print("Payment ID:", payment.paymentId)
    print("Payment Method:", payment.method)
    print("Payment Status:", payment.check_success())
    print("****************************\n")


# Print all receipts
print_receipt(customer1, order1, payment1)
print_receipt(customer2, order2, payment2)
print_receipt(customer3, order3, payment3)
