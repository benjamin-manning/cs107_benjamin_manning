def make_withdrawal(init_balance):
    balance = init_balance
    def new_balance(withdrawal_amount):
        nonlocal balance
        try:
            if withdrawal_amount > balance:
                return 'Balance must be greater than withdrawal amount'
            else:
                balance = balance - withdrawal_amount
                return balance
        except TypeError:
            return 'Both Withdrawal and balance amounts must be numbers'
    return new_balance

wd= make_withdrawal(1000)
print(wd(800))
print(wd(150))
