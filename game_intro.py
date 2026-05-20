class server_profile:
        def __init__(self, name, gender, workdays):
            self.name = name 
            self.gender = gender
            self.workdays = workdays
class Server:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

user_name = input("Hello! Please enter your name:")
print(f"Welcome to {user_name}'s Resturaunt! You are now a server at rank {1} with {"ZERO"} customers served so far.")

name = Server(user_name, 100, [])
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

name = ["Abby", "Bob", "Calla", "Devi", "Eli", "Francis", "George", "Henry", "Imogen", "Jonathan", "Katie", "Larry", "Michelle", "Nicole", "Opi", "Penguin"]
status = ["SUPER Happy (100)", "Happy (99)", "Nonchalant (88)", "Annoyed (75)", "SUPER Annoyed (70)", "Mad (55)", "HUNGRY... (30)", "I AM GODZILLA (0)", "SO MAD IM ON FIRE!!!! (-10)"]

class CustomerHappiness:
    def __init__(self, name, status, happiness_level):
        self.name = name
        self.happiness_level = happiness_level
        self.status = status
    def add_or_subtract(self, amount):
        self.happiness_level += amount
name = CustomerHappiness(customer["name"],customer["status"],10)
print(name.__dict__)



