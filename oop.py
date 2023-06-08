from datetime import date

class User:
    def __init__(self, first_name = "Eric", last_name = "F"):
        self.name = first_name + ' ' + last_name

    def greet(self):
        return print(f"Nice to meet you, {self.name}")
    
eric = User(first_name="Chris", last_name="S")
# print(eric.name)
# eric.greet()

class BankAccount:
    # Anything that's a parameter is something we at least might be asking the user for. If it's always going to be the same, I don't need to ask the user for that information
    def __init__(self, name, type):
        # It's creating keys with whatever I say after the dot and the value is whatever is being passed in by the user
        self.account_holder = name
        self.type = type
        self.balance = 0

    def overdraft(self):
        self.balance -= 20
    # self is referring to the object that's being created from the intialization
    def deposit(self, amount):
        # I want to tell them how much they deposited and then the remaining balance
        self.balance += amount
        return print(f"You deposited ${amount} and your account balance is now ${self.balance}")
    
    def withdraw(self, amount):
        total_left = self.balance - amount
        if total_left < -80:
            return print("You don't have enough money in the account to take that much out. Please select a lower amount")
        elif total_left < 0:
            self.balance = total_left
            self.overdraft()
            return print(f"You are withdrawing ${amount} which has caused your account to be negative. I am adding a $20 overdraft fee on top of the amount you're withdrawing bringing your account to -${self.balance * -1}")
        else:
            self.balance = total_left
            return print(f"You are withdrawing ${amount} and your remaining balance is ${self.balance}")
    
# erics_account = BankAccount(name="Eric", type="Checking")
# print(erics_account.account_holder)
# print(erics_account.balance)
# erics_account.deposit(amount=25)
# erics_account.deposit(50)
# erics_account.withdraw(40)
# erics_account.withdraw(40)
# erics_account.withdraw(300)

# print(type(erics_account))

# my_obj = {
#     'first': "String",
#     'second': "Also a string"
# }

# for key, value in my_obj.items():
#     # print(key, value)
#     # my_obj[key] = [value, type(value)]
#     print(type(value))

# print(my_obj['first'][0])
# for key, value in erics_account.items():
#     print(key, value)

class Phone:
    # We are initializing this with a phone number that has a default which will be used if it's not given the number when it's created. This will create an instance of the Phone class (an object) that has a key of number with a value of whatever the phone number passed in is
    def __init__(self, phone_number = "867-5309", keyboard=None):
        self.number = phone_number
        self.keyboard = keyboard

    # We can have methods inside of this phone class that are available to all the instances of phones that are created
    def call(self, other_number="911"):
        return print(f"Calling {self.number} from {other_number}")
    
    # You can also text people!
    def text(self, other_number, message):
        return print(f"{other_number} sent the following text to you: {message}")
    
my_phone = Phone(phone_number="123-456-7890")
print(my_phone)
my_phone.call()

# The (Phone) is what's telling this class that we're inheriting it and it's going to be a child of whatever is in the parentheses.
class IPhone(Phone):
    def __init__(self, phone_number="867-5309", keyboard=None):
        # This super is bringing in everything from the parent class. The phone number is brought in from the parent.
        super().__init__(phone_number, keyboard)
        self.fingerprint = None
        self.password = None

    def set_fingerprint(self, fingerprint):
        self.fingerprint = fingerprint

    def unlock(self, fingerprint=None):
        if fingerprint == self.fingerprint:
            return print("This phone is unlocked!")
        else:
            return print("This phone is still locked. You can also enter your password")

# new_phone = IPhone(keyboard="Built in UI")
# print(new_phone.number)
# print(new_phone.keyboard)


# Creating accounts exercise: 
# Could have imported datetime here
class Account:
    def __init__(self):
        self.funds = 100
        self.date_open = date.today()
    
    def deposit(self, amount):
        # You could've just done it for any amount. I wanted to make sure it wasn't a negative amount
        if amount < 0:
            return print("That's not how this works. That's not how any of this works!")
        else:
            self.funds += amount
            return print(f"You deposited ${amount} which brings your account balance to ${self.funds}")
    
    # I can only withdraw funds if the amount is available
    def withdraw(self, amount):
        if amount > self.funds:
            return print("I'm not letting you borrow my money!")
        else:
            self.funds -= amount
            return print(f"Your withdawl of ${amount} brings your account down to ${self.funds}")
        
    def __str__(self):
        return f"General Account opened on {self.date_open} with ${self.funds} available"

# Creating a savings account class that's a child of the account class. 
class SavingsAccount(Account):
    def __init__(self):
        # Going to get the information the parent was initialized with. If you provided a default in the parent, you have to do the same in the child
        super().__init__()
        self.type = "Savings"
        self.interest = 0.01

    def add_interest(self):
        self.funds *= (1 + self.interest)
        return print(f"You gained 1% interest and your new balance is ${self.funds}")

# my_account = Account()
# print(my_account.funds)
# my_account.withdraw(amount=50)
# my_account.deposit(amount=40)
# print(my_account)

# my_savings_account = SavingsAccount()
# print(my_savings_account)
# print(my_savings_account.date_open)
# print(my_savings_account.funds)
# my_savings_account.add_interest()

class Checking(Account):
    def __init__(self):
        # This is bringing in the date_opened and the funds from the parent class
        super().__init__()
        self.type = "Checking"
        self.monthly_fee = 25
    
    def deduct_fee(self):
        self.funds -= self.monthly_fee
        return print(f"I'm deducting ${self.monthly_fee} for the montly fee bringing your balance to ${self.funds}")
    
my_checking_account = Checking()
print(my_checking_account.date_open)
my_checking_account.deduct_fee()
# All of the methods that are available to the parent will also be available to all the children
my_checking_account.withdraw(40)