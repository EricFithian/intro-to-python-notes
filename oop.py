class User:
    def __init__(self, first_name = "Eric", last_name = "F"):
        self.name = first_name + ' ' + last_name

    def greet(self):
        return print(f"Nice to meet you, {self.name}")
    
eric = User(first_name="Chris", last_name="S")
print(eric.name)
eric.greet()