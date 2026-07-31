from abc import ABC, abstractmethod
#strtegic interface 
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
#cocrete strategy 1
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

#concrete strategy 2
class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Debit Card.")

#concrete strategy 3
class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")

#cocrete strategy 4
class RDGPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using RDG.")

#cotext class
class paymentprocessor:
    def __init__(self, strategy =None):
        self.strategy = strategy
    def set_strategy(self, strategy):
        self.strategy = strategy
    def process_payment(self, amount):
        if self.strategy is None:
            print("Payment strategy not set.")
        else:
            self.strategy.pay(amount)
        
#driver code
processor = paymentprocessor()
while True:

    print("***** Payment Options *****")
    print("1. Credit Card Payment")
    print("2. Debit Card Payment")
    print("3. UPI Payment")
    print("4. RDG Payment")
    print("5. Exit") 
    
    choice = int(input("Enter your choice (1-5): "))
    amount = float(input("Enter the amount to pay: "))
    if choice == 1:
        processor.set_strategy(CreditCardPayment())
    elif choice == 2:
        processor.set_strategy(DebitCardPayment())
    elif choice == 3:
        processor.set_strategy(UPIPayment())
    elif choice == 4:
        processor.set_strategy(RDGPayment())
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
    processor.process_payment(amount)
    




