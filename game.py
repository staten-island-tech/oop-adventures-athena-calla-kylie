
""" for customer in customer_orders_day_one:
    choice = input("Choose a customer to serve")
    if choice == customer["name"]:
        print(customer["name"])
    else:
        print("No costumer found") """
"""
class Sever:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

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
""" 
class CustomerHappiness:
    def __init__(self, name, status, happiness_level):
        self.name = name
        self.happiness_level = happiness_level
        self.status = status
    def add_or_subtract(self, amount):
        self.happiness_level += amount
"""     def ():
        if amount > 10:
       """      
name = CustomerHappiness(customer["name"],customer["status"],10)
# print(name.__dict__)

work = True
earnings = []
total_money = 0
customer_history = []
while work:
    serve_customers = (input("Serve customer? Type the number of the customer you want to serve first based on status."))
    if serve_customers != customer["name"]:
        name.add_or_subtract(-10)
        print(name.__dict__)
    else:
        work_continue = input("continue working or calculate earnings and score for today? Enter Yes (continue) or No (calculate)")
        if work_continue == "No":
            print(name.__dict__)
            work = False
            break

"""
        
"""
