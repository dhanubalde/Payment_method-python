# Ordering System in Python
# by Dhanubalde
from abc import ABC, abstractmethod


class Order():
    item = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        # creating an object
        self.item.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        # computing for total order
        # total = quantity * price
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor(ABC):
    # creating a sub classes
    @abstractmethod
    def pay(self, order, email_address, security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        # two ways of payment method using credit & debit
        print("Processing Debit payment type")
        print(f"Verifying security code : {self.security_security_code}")
        self.status = "paid"


class CredirPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        # two ways of payment method using credit & debit
        print("Processing Credit payment type")
        print(f"Verifying security code : {self.security_code}")
        self.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address):
        self.email_address = email_address

    def pay(self, order):
        print("Processing Paypal payment type")
        print(f"Verifying Email Address : {self.email_address}")
        self.status = "paid"


order = Order()
# adding order item list to cart
order.add_item("flashdrive", 1, 40)
order.add_item("drone", 2, 100)
order.add_item("tv", 1, 20)

# viewing total price
print(order.total_price())
# payment_type and security code
processor = PaypalPaymentProcessor("kedanubalde41@gmail.com")
processor.pay(order)
