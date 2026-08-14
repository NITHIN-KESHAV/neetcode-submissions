from abc import ABC, abstractmethod

class PaymentCard():
    def __init__(self, card_number: str, balance: float):
        self.card_number = card_number
        self.balance = balance

    @abstractmethod
    def process_payment(self, amt: int)->None:
        pass



# TODO: Implement the DebitCard class
class DebitCard(PaymentCard):

    def __int__(self, card_number: str, balance: float, amt: int):
        super().__init__(self, card_number, balance)

    def process_payment(self, amt: int)->None:
        if self.balance < amt:
            return "Insufficient funds"
        self.balance = self.balance - amt
        return "Payment successful"



class CreditCard(PaymentCard):

    def __int__(self, card_number: str, balance: float, amt: int):
        super().__init__(self, card_number, balance)

    def process_payment(self, amt: int)->None:
        self.balance = self.balance - amt
        return "Payment successful"
        

# TODO: Implement the CreditCard class


# Don't modify the code below
debit_card = DebitCard("1234", 100.0)  # Card with $100 balance
credit_card = CreditCard("5678", 100.0) # Card with $100 balance

# Test debit card
print(debit_card.process_payment(50.0))  
print(debit_card.balance)                
print(debit_card.process_payment(100.0))  
print(debit_card.balance)    

# Test credit card
print(credit_card.process_payment(50.0))   
print(credit_card.balance)                
print(credit_card.process_payment(100.0))  
print(credit_card.balance)    
