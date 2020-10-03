from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

print(AccountType.SAVINGS == AccountType.SAVINGS)
print(AccountType.SAVINGS == AccountType.CHECKING)
print(AccountType.SAVINGS.name)

class BankAccount():
    
    def __init__(self, owner, accountType: AccountType):
        # your code

    def withdraw(self, amount):
        # your code
        
    def deposit(self, amount):
        # your code

    def __str__(self
        # your code

    def __len__(self):
        # your code