def make_withdrawal(init_balance):
    def new_balance(withdrawal_amount):
        try:
            if withdrawal_amount > init_balance:
                return 'Balance must be greater than withdrawal amount'
            else:
                return init_balance - withdrawal_amount
        except TypeError:
            return 'Both Withdrawal and balance amounts must be numbers'
    return new_balance

print('This function does not work because the initial balance is reset everytime once it is within the inner function. The inner function always recalls the initial balance it was first fed and resets.')

wd = make_withdrawal(1000)
print(wd(800))
print(wd(150))
