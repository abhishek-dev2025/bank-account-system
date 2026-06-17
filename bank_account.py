import random

class BankAccount:
   
    def __init__(self):
        #Initialize account details
        self.name=None
        self.pin=''
        self.balance=0
        self.phone_number=None
        #Generate a random account number
        self.account_number=random.randint(10000000,999999999)
        self.menu()


    def menu(self):
        #Main menu
        user_input=input('''
            Please enter your choice:
            1. Create Account
            2. Deposit Money 
            3. Withdraw Money 
            4. Check Balance 

            ''')

        if user_input=="1":
            self.create_account()
        elif user_input=='2':
            self.deposit_money() 
        elif user_input=="3":
            self.withdraw_money() 
        elif user_input=="4":
            self.check_balance() 
        else:
            exit()


    def create_account(self):
        #Collect user information and create an account
        print("Hello! Please enter your details.")
        self.name=input("Enter your name:")
        self.pin=(input("Create your PIN:"))
        self.phone_number=input("Enter your mobile number:")

        print("Account created successfully!")
        print("Your account number:",self.account_number)
        self.menu()
   
   
    def deposit_money(self):
        #Verify account details and deposit money
        print("Please enter the information below:")
        user_account=int(input("Enter your account number:"))
        user_pin=input("Enter your PIN:")
        if user_account==self.account_number and user_pin==self.pin:
            deposit_amount=int(input("Enter the amount to deposit:"))
            if deposit_amount<=0:
                print("Please enter a valid amount.")
            else:
                self.balance+=deposit_amount
                print("Deposit successful!")
        else:
            print("Invalid account number or PIN.")
        self.menu()


    def withdraw_money(self):
        #Verify account details and withdraw money
        user_account=int(input("Enter your account number:"))
        user_pin=(input("Enter your PIN:"))
        if user_pin==self.pin and user_account==self.account_number:
            withdraw_amount=int(input("Enter the amount to withdraw:"))
            if withdraw_amount>self.balance:
                print("Insufficient amount!")
            else:
                self.balance-=withdraw_amount
                print("Money withdrawn successfully!")
                print("Remaining balance:",self.balance)
                
        else:
            print("Invalid information.")
        self.menu()
    
    
    def check_balance(self):
        #Display balance after verifying user information
        user_name=input('Enter your name:')
        user_account=int(input("Enter your account number:"))
        user_pin=input("Enter your PIN:")

        if user_name==self.name and user_account==self.account_number and user_pin==self.pin:
            print("Account Balance:",self.balance)

        else:
            print("Invalid information.")
        self.menu()

account=BankAccount()        

        
