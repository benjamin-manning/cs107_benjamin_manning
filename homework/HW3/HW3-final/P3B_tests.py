from enum import Enum
from Bank import AccountType, BankAccount, BankUser

def test_over_withdrawal():  
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 10);
    #Try withdrawing more than balance
    try:
        user.withdraw(AccountType.SAVINGS, 1000);
    except Exception as e:
        print(e);
    #Try getting balance of unmade account
    try:
        user.getBalance(AccountType.CHECKING);
    except Exception as e:
        print(e);
    #Try depositing a negative value
    try:
        user.deposit(AccountType.SAVINGS, -1);
    except Exception as e:
        print(e); 
    try:
        user.addAccount(AccountType.SAVINGS);
    except Exception as e:
        print(e); 

test_over_withdrawal();
