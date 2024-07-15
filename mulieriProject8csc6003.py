# Michael Mulieri, mulierim@merrimack.edu, 12/14/2023, csc6003
# Project 8 - Final Project
# A program that manages bank accounts

# import uuid if larger more complex account numbers are required
# import uuid

# import decimal module to ensure efficiency when dealing with floats
from decimal import *

# import datetime to mark date and time accounts are opened
import datetime


class BankAccount:
    def __init__(self, p_account_number, p_date_opened, p_home_state_branch, p_balance=0):
        
        """initialize attributes p_account_number, p_date_opened, p_home_state_branch, and p_balance

        Args:
            p_account_number (int): int representing account number
            p_date_opened (obj): class date.datetime 
            p_home_state_branch (str): home state branch of client
            p_balance (int, optional): account balance defaults to 0. class Decimal upon user input
        """
        self.a_account_number = p_account_number
        self.a_balance = p_balance
        self.a_date_opened = p_date_opened
        self.a_home_state_branch = p_home_state_branch

    def account_deposit(self, deposit_amount):
        self.a_balance += deposit_amount

    def account_withdraw(self, withdraw_amount):
        self.a_balance -= withdraw_amount


class Bank():
    def __init__(self):
        """initialize Bank class
        """
        # empty list to store Bank instances
        self.__accountList = []

    def create_account(self, home_state_branch, initial_balance):
        """method to create an instance of a bank account

        Args:
            home_state_branch (str): clients home state branch
            initial_balance (obj): class Decimal
        """
        # length of account list is used to create new account numbers for the sake of ease of use,
        # in a real world situation that would require more complex account numbers, something like
        # uuid could be used as depicted in below comment
        # newAccountNumber = uuid.uuid4().int >> 100
        
        newAccountNumber = len(self.__accountList)
        
        # creates date and time of when account was opened
        date_opened = datetime.datetime.now()

        print(f'\nNew account number is: {newAccountNumber}\n')

        # create new instance of a bank account
        newAccount = BankAccount(newAccountNumber, date_opened, home_state_branch, initial_balance)
        
        # adds new account object to account list
        self.__accountList.append(newAccount)  

    def __get_account(self, account_number):
        """method that retrieves specified account via account number

        Args:
            account_number (int): account number

        Returns:
            obj: instance of bank account
        """
        for account in self.__accountList:
            if account.a_account_number == int(account_number):
                return account
    
    def deposit(self, account_number, amount):
        """method that deposits user specified amount

        Args:
            account_number (int): account number
            amount (obj): class Decimal
        """
        
        # retrieve instance of bank account via return of __get_account() method and bind to 
        # currentAccountInstance variable
        currentAccountInstance = self.__get_account(account_number)
        
        # deposits amount to specified account number via account_deposit() method
        try:
            currentAccountInstance.account_deposit(amount)
            
        # Alerts user if account is not found
        except AttributeError:
            print('\nAccount does not exist.\n')
        
    def withdraw(self, account_number, amount):
        """method to withdraw specified amount

        Args:
            account_number (int): account number
            amount (obj): class Decimal
        """
        
        # retrieve bank account instance via account number and bind to 
        # currentAccountInstance variable
        currentAccountInstance = self.__get_account(account_number)
        
        # checks if there are sufficient funds to withdraw
        try:
            if currentAccountInstance.a_balance - amount >= 0:
                # withdraws funds via account_withdraw() method
                currentAccountInstance.account_withdraw(amount)
                
            # alerts user if there are insufficient funds to transfer
            else:
                print('\nInsufficient Funds\n')
        
        # alerts user if account does not exist
        except:
            print('\nAccount does not exist.\n')
        
            
            
    def transfer(self, account_number1, account_number2, amount):
        """method that allows funds to be transfered from one account to another

        Args:
            account_number1 (int): account to transfer from 
            account_number2 (int): account to transfer to
            amount (obj): class Decimal
        """
        
        # retrieves both bank account instances via __get_account() method
        currentAccountInstance1 = self.__get_account(account_number1)
        currentAccountInstance2 = self.__get_account(account_number2)
        
        # checks if there are sufficient funds to transfer
        try:
            if currentAccountInstance1.a_balance - amount >= 0:
                # transfers funds from account 1 to account 2
                currentAccountInstance2.account_deposit(amount)
                currentAccountInstance1.account_withdraw(amount)
            
            # alerts user if there are insufficient funds to transfer
            else:
                print('\nInsufficient Funds To Transfer\n')
                
        # alerts user if account does not exist
        except:
            print('\nOne or both accounts do not exist.\n')
        
        
    def check_account_balance(self, account_number):
        """method to check balance of specified account

        Args:
            account_number (int): account number

        Returns:
            obj: class Decimal
        """
        
        # retrieves instance of bank account via __get_account() method
        currentAccountInstance = self.__get_account(account_number)
        # returns balance of account
        return (currentAccountInstance.a_balance)
    
    def get_account_details(self, account_number):
        """method that provides account details

        Args:
            account_number (int): account number

        Returns:
            str: home state branch
            obj: date opened - class Datetime
            obj: balance - class Decimal
        """
        
        # retrieves instance of bank account via __get_account
        currentAccountInstance = self.__get_account(account_number)
        # returns home stat branch, date opened and balance of specified account
        return (currentAccountInstance.a_home_state_branch, currentAccountInstance.a_date_opened, currentAccountInstance.a_balance)

        

def menu(welcomePrompt=False):
    """method to display operation choices. 

    Args:
        welcomePrompt (bool, optional):  welcome prompt is only displayed upon first call.
    """
    
    if welcomePrompt:
        print('\nWelcome To Your Digital Bank Management System!\n')
    
    # displays menu of operation options
    print('1. Create New Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transer\n6. Get Account Details\n7. Quit')
    
    # calls executeChoice() method 
    executeChoice()
    
def executeChoice():
    """method that allows user to choose operation to execute
    """
    
    # variable actionChoice binds to user input of desired operation
    actionChoice = input('Enter number of desired task (1-7): ')
    
    if actionChoice.strip() == '1':
        
        """user input is validated via validateEnterAmount() method
        if validation is succesful initial_balance variable is bound to return of
        validateEnterAmount() """
        initial_balance = validateEnterAmount()    
        
        """home_state_branch variable bound to user input - strip() removes whitespace from 
        beginning and end of string, title() capitilizes first character of each word"""
        home_state_branch = input('What is the clients home state?: ').strip().title()
        
        # split home_state_branch string into seperate strings at spaces and bind to 
        # home_state_branch_word_list variable
        home_state_branch_word_list = home_state_branch.split()
        
        # check if all characters are letters
        for word in home_state_branch_word_list:
            if word.isalpha() == False:
                
                # user entered invalid character and is asked to try again
                print('\nERROR - Invalid entry, please try again.\n')
                menu()
        
        # creates instance of bank account
        B.create_account(home_state_branch, initial_balance)
        
    elif actionChoice.strip() == '2':
    
        # binds account_number variable to return of validateAccountNumber()
        account_number = validateAccountNumber()
        
        # amount variable binds to return of validateEnterAmount() method
        amount = validateEnterAmount()
            
        # deposit made to specified account via deposit() method
        B.deposit(account_number, amount)
        
    elif actionChoice.strip() == '3':
        
        # prompts user for input via validateAccountNumber() and binds return to account_number variable
        account_number = validateAccountNumber()
        
        # amount variable binds to return of validateEnterAmount() method
        amount = validateEnterAmount()
        
        # withdraws funds from specified account via withdraw() method
        B.withdraw(account_number, amount)
        
    elif actionChoice.strip() == '4':
        # prompts user for input, validates input via validateAccountNumber() method
        account_number = validateAccountNumber()
        
        # displays account balance via return of check_account_balance() method
        try:
            account_balance = B.check_account_balance(account_number)
            print(f'\nAccount balance of account number {account_number} is: ${account_balance}\n')
        
        # error raised if account does not exist, user alerted via print statement 
        except:
            print('\nAccount does not exist.')
        
    elif actionChoice.strip() == '5':
        
        # binds account_number1 and account_number2 variables to return of validateAccountNumbers()
        account_number1, account_number2 = validateAccountNumbers()
        
        
        # amount variable binds to return of validateEnterAmount() method
        amount = validateEnterAmount()           
        
        # transfers funds from account 1 to account 2 via transfer() method
        B.transfer(account_number1, account_number2, amount)
        
    elif actionChoice.strip() == '6':
        
        # prompts user for input
        account_number = input('Enter account number: ')
        
        # retrieves account details via get_account_details() method, then displays details
        try:
            home_state_branch, account_opened, account_balance = B.get_account_details(account_number)
            print(f'\nAccount number: {account_number}\nAccount balance: ${account_balance}\nAccount opened: {account_opened}\nHome state branch: {home_state_branch}')
            
        # alerts user if account does not exist
        except:
            print('\nAccount does not exist.\n')
            
        
    elif actionChoice.strip() == '7':
        # exits program and displays goodbye message
        print('\nGoodbye\n')
        return
    
    # error message displayed if user enters invalid input 
    else:
        print('\nERROR - Must enter a valid number.\n')
        
        menu()  
    
    # continueOperation() method called after completion of every operation  
    continueOperation()
    
def continueOperation():
    """method called recursively allowing user to continue operations or exit
    """
    
    # prompts user for input
    answer = input('\nWould you like to do more? Y/N: ').strip().lower()
    
    # if user does not provide 'y' or 'n' error message displayed
    while answer != 'y' and answer != 'n':
        answer = input('\nERROR - Must type Y or N. Would you like to do more? Y/N: ').strip().lower()
    
    # calls menu() function if user enters 'y' 
    if answer == 'y':
        menu()
    
    # displays goodbye message and exits program 
    elif answer == 'n':
        print('\nGoodbye\n')
        return 
    
def validateEnterAmount():
    """helper method that checks validity of user input

    Returns:
        obj: class Decimal
    """
    
    while True:
        # prompts user to enter amount
            try:
                amount = Decimal(input('Enter amount: $')).quantize(
                    Decimal('.01'), rounding=ROUND_DOWN)
            
            # if user enters letter or special character, error raised
            except InvalidOperation:
                print('\nERROR - Invalid Input')
                
            else:
                return amount
            
def validateAccountNumber():
    """helper method to validate user input of account number

    Returns:
        int: account number
    """
    
    # prompts user for input and binds to acount_number variable
    account_number = input('Enter account number: ')
    
    # ensures user enters a digit, otherwise displays error message 
    while account_number.isdigit() == False:
        account_number = input('ERROR - Please enter a number: ')
        
    return account_number

def validateAccountNumbers():
    """helper method to validate user input two account numbers

    Returns:
        int: account number 1
        int: account number 2
    """
    
    # prompts user for input and binds to account_number1 variable
    account_number1 = input('Enter account number to transfer from: ')
    
    # ensures user provides digit for account 1
    while account_number1.isdigit() == False:
        account_number1 = input('ERROR - Please enter a number: ')
    
    # prompts user for input and binds to accountNumber2 variable 
    account_number2 = input('Enter account number to transfer to: ')
    
    # ensures user provides digit for account 2
    while account_number2.isdigit() == False:
        account_number2 = input('ERROR - Please enter a number: ')
        
    return account_number1, account_number2
    
if __name__ == '__main__':
    # instanciates Bank
    B = Bank()
    # calls menu() method, passes True so welcome prompt is only displayed once
    menu(True)






