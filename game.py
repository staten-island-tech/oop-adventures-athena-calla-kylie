class Sever:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"

user_name = input("Hello! Please enter your name:")
print(f"Welcome to {user_name}'s Resturaunt!")

name = Sever(user_name, 100, [])
print(name.__dict__)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
name = BankAccount(user_name, 100)
user_name.show_balance

class CustomerHappiness:
    def __init__(self, name, happiness_level):
        self.name = name
        self.happiness_level = happiness_level
        
