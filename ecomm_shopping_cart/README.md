# E‑Commerce Shopping Cart

A modular, object‑oriented e‑commerce simulation built in Python.  
This project demonstrates how products, carts, customers, orders, and payments interact in a real shopping workflow.

---

## Features

- Add products to a cart  
- Create cart items with quantity and line totals  
- Customer checkout → generates an order  
- Payment processing for each order  
- Automatic receipt generation  
- Clean multi‑service architecture  
- Fully object‑oriented design  

---

## Project Structure

```
ecomm_shopping_cart/
│
├── cart_service/
│   ├── cartCore.py        # Shopping cart logic
│   └── cartItem.py        # Single cart row (product + quantity)
│
├── customer_service/
│   └── customer.py        # Customer actions (checkout, pay)
│
├── order_service/
│   └── orders.py          # Order model
│
├── payment_service/
│   └── payment.py         # Payment model
│
├── product_service/
│   └── product.py         # Product model
│
└── mainApp.py             # Application runner
```

---

## How the System Works

### 1. **Products**
Created with ID, name, and price.

### 2. **CartItems**
Wrap a product + quantity  
Calculate line total automatically.

### 3. **CartCore**
Stores CartItems  
Calculates total  
Clears cart  
Returns list of items

### 4. **Customer**
Owns a cart  
Checks out → creates an Order  
Pays → creates a Payment

### 5. **Orders**
Created during checkout  
Stores cart items  
Tracks status  
Attaches payment

### 6. **Payment**
Processes order payment  
Marks success  
Belongs to an order

---

## Running the Application

Run:

```bash
python mainApp.py
```

You will see:

- Customer summaries  
- Order totals  
- Payment status  
- Full receipts  

---

## Example Receipt Output

```
**************************** RECEIPT ****************************
Customer: Jat Wall
Customer ID: CUST001
Order ID: ORD-1
Status: Paid

Items Purchased:
 ==> Rental Hill Mellow | Price: $450000 | Qty: 2 | Line Total: 900000

Order Total: $ 900000
Payment ID: PAY001
Payment Method: Card
Payment Status: True
****************************
```

---

## Concepts Demonstrated

- Object‑oriented programming  
- Composition between classes  
- Multi‑module architecture  
- Clean separation of concerns  
- Realistic e‑commerce workflow   

---

## 

Exploring Python OOP, architecture design, and e‑commerce modeling.

---
