class Sever:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
user_name = input("Hello! Please enter your name:")
print(f"Welcome to {user_name}'s Resturaunt!")

name = Sever(user_name,100, [])
print(name.__dict__)

