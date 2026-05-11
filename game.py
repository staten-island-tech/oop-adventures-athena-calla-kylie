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
class CustomerHappiness:
    def __init__(self, name, happiness_level):
        self.name = name
        self.happiness_level = happiness_level
    def add_or_subtract(self, amount):
        
calm = False  
angry = False
LIVID = False

if happiness_level > 60:
    calm = True
elif happiness_level > 40:
    angry = True


""" customer_orders_day_one = [
{
    "name": "Julia",
    "price": 12.99,
    "food type": "waffles with syrup and blueberries",
    "instructions": "Toast the waffles, add syrup, add blueberries.",
    "status": "angry"
},
{
    "name": "Gerald",
    "price": 4.99,
    "food type": "hot coffee with milk and sugar",
    "instructions": "pour the coffee, add a splash of milk, and a teaspoon of sugar.",
    "status": "calm"
},
{
    "name": "Agamemnon",
    "price": 120,
    "food type": "Two kids meal pancakes, an adult size bacon and eggs, covered in gold leaf.",
    "instructions": "Toast the waffles, add syrup, add blueberries, put on two plates. Fry the bacon and eggs, put on a plate.",
    "status": "LIVID."
},
{
    "name": "Lyla",
    "price": 24.99,
    "food type": "Mac and Cheese (3 orders plus extra cheese on one of them).",
    "instructions": "Heat up the mac anc cheese, plate, sprinke extra cheese on one of them.",
    "status": "LIVID."
},
    ]
for customer in customer_orders_day_one:
    print(f"Name: {customer["name"]}, Status: {customer["status"]}")
for customer in customer_orders_day_one:
    choice = input("Choose a customer to serve")
    if choice == customer["name"]:
        print(customer["name"])
    else:
        print("No costumer found") """