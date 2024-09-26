## Python Banking System
#Python Banking Program (JSON allows the system to retain user data (like usernames, passwords, balances, and transaction history) across multiple runs of the program. )
import json
from random import choice

#Load user data from a JSON file
def load_users(filename='users.json'):
    try:
        with open(filename, 'r') as f:
          return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
#Save user data to JSON
def user_data(account_users, filename='users.json'):
    with open(filename, 'w') as f:
        json.dump(account_users, f)


def greeting_page():
    print("--------------------")
    print("Welcome to the Bank!")
    print("--------Menu--------")

    print("| Type 1 to Login                    |")
    print("| Type 2 to Register                 |")
    print("| Type 3 if you forgot your passoword|")
    print("| Type 4 to Exit                     |")
    return greeting_page 

#Ask user to input a number
def bank_user():
    print("--------------")
    choice = input("Please Enter a Number:")
    return choice 
breakpoint

def user_choice(account_user):
    choice = bank_user()
    return choice


def account_users():
    choice = bank_user()
    return choice

def username():
    username = input("Enter your Username:")
    return username

def password():
    password = input("Enter your Password:")
    return password
# defining account
def account(username, password, balance=0.0):
    """Create a simple account."""
    return {
        "username": username,
        "password": password,
        "balance": balance,
        "transaction_history": []
    }

def new_account():
     new_account = {}
     new_account["username"] = input("Enter a new username:")
     new_account["password"] = input("Enter a new Password:")
     #Add User data to json
     new_account["balance"] = 0.0 #Balance attribute
     new_account["transaction_history"] = [] #Intialize transaction history
     account_users.append(new_account)
     user_data(account_users) #data saved
     print("Registration Successful")

def login(account_users):
    username_input = username()
    password_input = password()
    for account in account_users:
        if account["username"] == username_input and account["password"] == password_input:
            print("Login Successful!")
            user_functions(account)
            return
    print("Invalid username or password. Please try again.")

def forgot_password (account_users):
        username_input = input("Enter your username:")
        for account in account_users:
             if account["username"] == username_input:
                print("Password Succesfully recovered. Your password is:", account["password"])
                return 
             print("Uusername not found.")

#Establish Deposit & Transaction history
def user_functions(acccount):
    while True:
        print("\n----- User Menu -----")
        print("| Type 1 to Deposit       |")
        print("| Type 2 to Withdraw      |")
        print("| Type 3 to Check Balance  |")
        print("| Type 4 to View Transactions |")
        print("| Type 5 to Logout        |")
        choice = input("Select an option: ")

def user_deposit():
    if choice == "1":
        ammount = float(input("Enter deposit ammount:")) 
        account["balance"] += ammount
        account["transaction_history"].append(f"Deposited: ${ammount}")
        user_data(account_users)
        print(f"Deposited ${ammount}. New balance: ${account['balance']}")
# User Withdrawl
    elif choice == "2":
        amount = float(input("Enter withdrawl amount:"))
        if ammount <= account["balance"]:
            account["balance"] -= ammount
            account["transaction_history"].append(f"withdrew: ${ammount}")
        else:
             print("Insufficient funds.")
    elif choice == "3":
        print(f"Current Balance: ${account['balance']}")
    elif choice == "4":
        print("Transaction History:")
        for transaction in account["transaction_history"]:
            print(transaction)
    elif choice == "5":
        print("Logging out...")
        breakpoint
    else:
        print("Invalid. Try agin.")

def exit_program():
    print("You have chosen to Exit the Page.")
    response = input("Please type Yes/No:")
    if response.lower() == "yes":
        print("Goodbye") 
        exit()
        return
       
while True:
    greeting_page()
    choice = user_choice(account_users)
    if choice == "1":
       login(account_users)
    elif choice == "2":
        new_account()
    elif choice == "3":
        forgot_password(account_users)
    elif choice == "4":
        exit_program()
    else:
        print("Invalid. Try again.")
        