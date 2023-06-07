class User:
    def __init__(self, name = "Eric"):
        self.name = name

    def greet(self):
        return print(f"Nice to meet you, {self.name}")
    
eric = User("Chris")
print(eric.name)
eric.greet()