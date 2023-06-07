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
    
erics_account = BankAccount(name="Eric", type="Checking")
print(erics_account.account_holder)
print(erics_account.balance)
erics_account.deposit(amount=25)
erics_account.deposit(50)
erics_account.withdraw(40)
erics_account.withdraw(40)
erics_account.withdraw(300)