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

new_phone = IPhone(keyboard="Built in UI")
print(new_phone.number)
print(new_phone.keyboard)