def make_withdrawal(init_balance):
    balance = init_balance
    def new_balance(withdrawal_amount):
        try:
            if withdrawal_amount > init_balance:
                return 'Balance must be greater than withdrawal amount'
            else:
                balance = balance - withdrawal_amount
                return balance
        except TypeError:
            return 'Both Withdrawal and balance amounts must be numbers'
        except UnboundLocalError:
            return 
    return new_balance


print("This doesn't work because we are callng a nonlocal variable locally - so we get an unbound local error. If we have a name binding on the inner function, it will reference that inner binding always unless declare dotherwise. We need to use the non-local balance in order to prevent the initial balance from reseting.")
wd = make_withdrawal(1000)
print(wd(800))
print(wd(150))
