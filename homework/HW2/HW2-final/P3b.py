def make_withdrawal(init_balance):
    balance = init_balance
    def new_balance(withdrawal_amount):
        try:
            if withdrawal_amount > init_balance:
                return 'Balance must be greater than withdrawal amount'
            else:
                balance = init_balance - withdrawal_amount
                return balance
        except TypeError:
            return 'Both Withdrawal and balance amounts must be numbers'
    return new_balance


print("Once again, this doesn't work because we are using the local and initially submitted balance to the make_withdrawal function. We need to use the non-local balance in order to prevent the initial balance from reseting.")
wd= make_withdrawal(1000)
print(wd(800))
print(wd(150))
