from enum import Enum
from pydantic import BaseModel


class TransactionType(str, Enum):
    deposit = "deposit"
    withdraw = "withdraw"


class Account(BaseModel):
    account_id: int
    customer_id: int
    account_number: str
    balance: float
    
    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")

    def get_balance(self) -> float:
        return self.balance
        

class Customer(BaseModel):
    customer_id: int
    name: str
    email: str
    phone_number: str
