from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():
    
    def __init__(self, owner, accountType: AccountType):
        #Establish the owner and staring balance
        self.owner = owner
        self.balance = 0
        self.accountType = accountType

    def withdraw(self, amount):
        #Check if withdrawal is greater than balance
        if amount > self.balance:
            raise Exception('withdrawal amount greater than balance')
        #Check if withdrawal is negative
        elif amount < 0:
            raise Exception('Withrawal amount must be positive')
        #Update the balance
        else:
            self.balance = self.balance - amount
        
    def deposit(self, amount):
        #Check if the deposit is negative
        if amount < 0:
            raise Exception('Deposit amount must be positive')
        #Update the Balance
        else:
            self.balance = self.balance + amount

    def __str__(self):
        #Print the owner, account type
        return(f'The owner of the account is {self.owner}, the account type is {self.accountType}')

    def __len__(self):
        #Prints the balance of the account
        return (self.balance)

class BankUser():
    
    def __init__(self, owner):
        #Initializing the owner and initialing empty checking and savings accounts
        self.owner = owner
        self.save_exist= 'No Account'
        self.check_exist = 'No Account'
        
    def addAccount(self, accountType):
        #For adding a savings account
        if accountType == AccountType.SAVINGS:
            #Seeing if a checking account already exists
            if self.save_exist == 'No Account':
                #Creating savings account in users name
                self.account_save = BankAccount(self.owner, accountType)
                #Updating Savings Account as added
                self.save_exist = "Account Added"
            else:
                #if Savings account already exists, raise exception
                raise Exception('You cannot have more than one saving account')
        #For adding checking accounts
        if accountType == AccountType.CHECKING:
            #Seeing if a checking account already exists
            if self.check_exist == 'No Account':
                #Creating Checking Account in user's name
                self.account_check = BankAccount(self.owner, accountType)
                #Updating Checking Account status as added
                self.check_exist = "Account Added"
            else:
                #If Checking account already exists, raise exception
                raise Exception('You cannot have more than one checking account')
  
    def getBalance(self, accountType):
        #Return balance of savings account if savings account
        if accountType == AccountType.SAVINGS:
            #Check if savings account exists
            if self.save_exist == 'No Account':
                raise Exception(f'{self.owner} Has not yet added a savings account')
            else:
                #Return savings account balance
                return(len(self.account_save))
        #Return balance of checking account if checking account
        if accountType == AccountType.CHECKING:
            #Check if checking account exists
            if self.check_exist == 'No Account':
                raise Exception(f'{self.owner} Has not yet added a checking account')
            else:
                #Return checking account balance
                return(len(self.account_check))
        
    def deposit(self, accountType, amount):
        #Check if deposit is negative
        if amount < 0:
            raise Exception('Deposit amount must be positive')
        #Check account type
        if accountType == AccountType.SAVINGS:
            #Check if savings account exists
            if self.save_exist == 'No Account':
                raise Exception(f'{self.owner} Has not yet added a savings account')
            else:
                #Update and return savings balance with deposit
                self.account_save.balance = self.account_save.balance + amount
                return self.account_save.balance
        if accountType == AccountType.CHECKING:
            #Check if checking account exists
            if self.check_exist == 'No Account':
                raise Exception(f'{self.owner} Has not yet added a checking account')
            else:
                #Update and return checking balance with deposit
                self.account_check.balance = self.account_check.balance + amount
                return self.account_check.balance

    def withdraw(self, accountType, amount):
        if amount < 0:
            print('Withdraw amount must be positive')
        if accountType == AccountType.SAVINGS:
             #Check if savings account exists
            if self.save_exist == 'No Account':
                raise Exception(f'{self.owner} Has not yet added a savings account')
            #check if withdrawal amount is greater than savingsbalance
            elif amount > self.account_save.balance:
                raise Exception('withdrawal amount greater than balance')
            else:
                #update savings balance with withdrawal
                self.account_save.balance = self.account_save.balance - amount
                return self.account_save.balance
        if accountType == AccountType.CHECKING:
             #Check if checking account exists
            if self.check_exist == 'No Account':
                raise Exception(f'{self.owner} Has not yet added a checking account')
            #check if withdrawal amount is greater than checking balance
            elif amount > self.account_check.balance:
                raise Exception('withdrawal amount greater than balance')
            else:
                #update checking balance with withdrawal
                self.account_check.balance = self.account_check.balance - amount
                return self.account_check.balance

    def __str__(self):
        #check for checking account
        if self.check_exist == "Account Added":
            #check for savings account too
            if self.save_exist == "Account Added":
                #If user has both accounts
                return(f'{self.owner} has two accounts\n checking Balance = {self.account_check.balance}\n Savings Balance = {self.account_save.balance}')
            else:
                #if user only has a checking account
                return(f'{self.owner} has one account\n Checking Balance = {self.account_check.balance}')
        if self.save_exist == "Account Added":
            #if user only has a savings account
            return(f'{self.owner} has one account\n Savings Balance = {self.account_save.balance}')
        else:
            #if user has no accounts
            return(f'{self.owner} has no accounts')

#Defining the ATM Session
def ATMSession(BankUser):
    #Define Inner Interface Function
    def Interface():
        #Access the BankUser
        nonlocal BankUser
        while True:
            #Create option and offer the 5 choices
            option = int(input("Enter Option:\n1) Exit\n2) Create Account\n3) Check Balance\n4) Deposit\n5) Withdraw\n"))
            #If user selects exit
            if option == 1:
                print("You have exited the ATM session")
                exit(1)
            #If user selects Create account
            elif option == 2:
                #Account type selection
                account_choice = int(input("Enter Option:\n1) Checking\n2) Savings\n"))
                if account_choice == 1:
                    #check if user already made a savings account
                    if BankUser.check_exist == 'No Account':
                        #Establish a checking account
                        print('You have created a checking account')
                        BankUser.addAccount(AccountType.CHECKING)
                    else:
                        #will alert that user can't have more than 1 checking account
                        BankUser.addAccount(AccountType.CHECKING)
                elif account_choice == 2:
                    if BankUser.save_exist == 'No Account':
                        #Establish a savings account
                        print('You have created a savings account')
                        BankUser.addAccount(AccountType.SAVINGS)
                    else:
                        #will alert that user can't have more than 1 savings account
                        BankUser.addAccount(AccountType.SAVINGS)
                else:
                    #Return error if user doesn't select 1 or 2
                    print("Must enter a valid account type")
            #If User selects check balance
            elif option == 3:
                #Account type selection
                account_choice = int(input("Enter Option:\n1) Checking\n2) Savings\n"))
                if account_choice == 2:
                    if BankUser.save_exist == 'Account Added':
                    #check savings account balance
                        print(f'{BankUser.owner} Your Savings account balance is:', BankUser.getBalance(AccountType.SAVINGS))
                    else:
                        #Reminds user that they don't have a savings account to check
                        BankUser.getBalance(AccountType.SAVINGS)
                elif account_choice == 1:
                    if BankUser.check_exist == 'Account Added':
                        #Check checking account balance
                        print(f'{BankUser.owner} Your Checking account balance is:', BankUser.getBalance(AccountType.CHECKING))
                    else:
                        #Reminds user that they don't have a checking account to check
                        BankUser.getBalance(AccountType.CHECKING)
                else:
                    #Return error if user doesn't select 1 or 2
                    print("Must enter a valid account type")
            #If user selects Deposit
            elif option == 4:
                #select account type
                account_choice = int(input("Enter Option:\n1) Checking\n2) Savings\n"))
                #choose savings account
                if account_choice == 2:
                    if BankUser.save_exist == 'Account Added':
                        #Get depisit amount and update savings
                        deposit_amount = int(input('Enter Deposit Amount (cannot be negative)\n'))
                        BankUser.deposit(AccountType.SAVINGS, deposit_amount)
                    else:
                        #Savings account doens't exist
                        BankUser.deposit(AccountType.SAVINGS, 0)
                elif account_choice == 1:
                    if BankUser.check_exist == 'Account Added':
                        #Get depisit amount and update checking
                        deposit_amount = int(input('Enter Deposit Amount (cannot be negative)\n'))
                        BankUser.deposit(AccountType.CHECKING, deposit_amount)
                    else:
                        #checking account doesn't exist
                        BankUser.deposit(AccountType.CHECKING, 0)
                else:
                    #Return error if user doesn't select 1 or 2
                    print("Must enter a valid account type")
            elif option == 5:
                #select account type
                account_choice = int(input("Enter Option:\n1) Checking\n2) Savings\n"))
                #choose savings account
                if account_choice == 2:
                    if BankUser.save_exist == 'Account Added':
                        #Get withdraw amount and update
                        withdraw_amount = int(input('Enter Withdraw Amount (cannot be negative or greater than your balance)\n'))
                        BankUser.withdraw(AccountType.SAVINGS, withdraw_amount)
                    else:
                        #Savings account does not exist
                        BankUser.withdraw(AccountType.SAVINGS, 0)
                elif account_choice == 1:
                    if BankUser.check_exist == 'Account Added':
                        #Get withdraw amount and update
                        withdraw_amount = int(input('Enter Withdraw Amount (cannot be negative or greater than your balance)\n'))
                        BankUser.withdraw(AccountType.CHECKING, withdraw_amount)
                    else:
                        #Checking account doesn't exist
                        BankUser.withdraw(AccountType.CHECKING, 0)
                else:
                    #Return error if user doesn't select 1 or 2
                    print("Must enter a valid account type")
            #In case someone puts in an incorrect interface value
            else:
                print('Please Select a valid action')
    return Interface
