import random
import time

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
print("If you need instructions on how to play, write 'Yes'. If you are ready to play now, write 'No' in the box below.")

instructions = input("Instructions? ::")

if instructions == ("Yes"):
        print(f"Hello my dear {user_name}!! I do hope your day is going well. Are you ready to master the restauraunt business? Or maybe not... Maybe you aren't ready. Are you?")
        ready = input("Are you ready for this?")
        print(f"Oh okay good, good. I am Luigi, the god of the restauraunt business. I will show you the ways of serving. Ready?")
        print("Step one: Show the customers the menu. Make sure they choose an item, which will print below for you.")
        ready2 = input("Got it??")
        print("Step two: check the customer's status (also printed below). If they are anything below annoyed, you need to REALLY make sure to get their order right... or else you lose money.")
        ready3 = input("Understood?")
        print(f"well then, {user_name}, it seems you are well prepared for the ordeal ahead. try to collect as many tips and earnings as you can, you can use them in the inventory store when you finish day one. Best of luck {user_name}, and I'll see you on the other side! XX, Luigi")
        finalready = input("Ready?")
        print("GAME START!!")
else: print("GAME START!!")

name = Server(user_name, 0, ["nothing yet"])
print(name.__dict__)

serve = input("Serve your first customer by entering ['Next Customer!']")
## REMEMBER TO INSERT ATHENA AND KYLIE AND MY CODE HERE


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
name = BankAccount(user_name, 100) 

class menus():
    def __init__(self, order_name, description, price,):
        self.order_name = order_name
        self.description = description
        self.price = price
class CustomerHappiness:
    def __init__(self, name, status, happiness_level):
        self.name = name
        self.happiness_level = happiness_level
        self.status = status
    def add_or_subtract(self, amount):
        self.happiness_level += amount

Menus = [
    {"name": "Breakfast"},
    {"name": "Lunch"},
    {"name": "Dinner"}
]

breakfast_food = [
        {"name": "Waffles - ",
        "price": "$6.99",
        "style": "strawberries" "blueberries" "bananas" "syrup" "chocolate syrup" "sprinkles" or "no toppings/sides",
        "instructions": "ghjbjb"
        },

        {"name": "Pancakes with",
        "price": "$6.50",
        "style": "strawberries" "blueberries" "bananas" "syrup" "chocolate syrup" "sprinkles" or "no toppings/sides"
        },

        {"name": "Bacon and Eggs - ",
        "price": "$6.99",
        "style": "scrambled" or "sunny side up"
        "instructions"
        },

        {"name": "Breakfast Burrito",
        "price": "$9.99",
        }
    ]

breakfast_drink = [
        {"name": "Hot Coffee - ",
        "price": "$1.99",
        "style": "espresso" "americano" "latte" or "cappuccino",
        },

        {"name": "Apple Juice",
        "price": "$0.99",
        },
                
        {"name": "Orange Juice",
        "price": "$0.99",
        },

        {"name": "Milkshake - ",
        "price": "$3.99",
        "style": "chocolate" "strawberry" or "vanilla"
        }
    ]

lunch_appetizer = [
        {"name": "Caesar Salad",
        "price": "$3.99",
        },

        {"name": "Sausage Bites",
        "price": "$3.50",
        },

        {"name": "Spinach Artichoke Dip",
        "price": "$3.50",
        },

        {"name": "Mozzarella Sticks",
        "price": "$3.99",
        }
        ]

lunch_food = [
        {"name": "Macaroni and Cheese",
        "price": "$7.99",
        },        
        
        {"name": "Burger",
        "price": "$8.99",
        },

        {"name": "Italian Grilled Cheese Sandwiches",
        "price": "$8.50",
        },

        {"name": "Chicken Caesar Pasta Salad",
        "price": "$7.99",
        },
    ]
    
lunch_drink = [
    {"name": "Soda",
     "price": "$0.99",
    },

    {"name": "Iced Tea",
     "price": "$0.99",
    },

    {"name": "Lemonade",
     "price": "$0.99",
    },
    
    {"name": "Smoothie",
     "price": "$3.99",
     "style": "strawberry banana" "mixed berries" or "tropical mango"
    }
    ]

dinner_appetizer = [
    {"name": "Spinach and Artichoke Dip",
     "price": "$3.50",
    },

    {"name": "Sausage Bites",
     "price": "$3.50",
    },

    {"name": "Smoked Salmon",
     "price": "$4.99",
    },

    {"name": "Charcuterie Board",
     "price": "$7.99",
    }
    ]

dinner_food = [
    {"name": "Spaghetti and Meatballs",
     "price": "$8.99"
    },
    
    {"name": "Chicken Alfredo",
     "price": "$9.99"
    },

    {"name": "Cast-Iron Steak - ",
     "price": "$14.99",
     "style" :"rare" "medium-rare" "medium" "medium well" or "well done"
    },

    {"name": "Burger",
     "price": "$8.99"}
    ]


dinner_dessert = [
    {"name": "Icecream",
     "price": "$3.99",
     "style": "chocolate" "strawberry" "vanilla" or "matcha"},
    
    {"name": "Molten Lava Cake",
     "price": "$7.99",
    },

    {"name": "Chocolate Chip Cookies",
     "price": "$4.99",
    },

    {"name": "Cheesecake",
     "price": "$6.50",
    }
    ]
name = ["Abby", "Bob", "Calla", "Devi", "Eli", "Michael Francis Aaron Jake Diner", "George", "Henry", "Imogen", "Jonathan", "Katie", "Larry", "Michelle", "Nicole", "Opi", "Penguin"]
happiness_level = random.randint(10,100)
steal = random.randint(-20,-1)

def show_menus(Menus):
    for index, Menus in enumerate(Menus):
        print(index, ":", Menus["name"])
show_menus(Menus)
print("You: 'Hi! Select your menu!'")
print(". . .")
menu_choice = ["breakfast", "lunch", "dinner"]
selection = random.choice(menu_choice)
print("Customer selects the", (selection), "menu")
print(input("Show customers the menu..."))

if selection == "breakfast":
    print("Breakfast Menu: ")
    print("Foods")
    def show_menu(breakfast_food):
        for index, breakfast_food in enumerate(breakfast_food):
            print(index, ":", breakfast_food["name"], "-", breakfast_food["price"])
    show_menu(breakfast_food)
    print("Drinks")
    def show_menu(breakfast_drink):
        for index, breakfast_drink in enumerate(breakfast_drink):
            print(index, ":", breakfast_drink["name"], "-", breakfast_drink["price"])
    show_menu(breakfast_drink)

    b_food = random.sample(breakfast_food,1)
    b_drink = random.sample(breakfast_drink,1)
    r_name = random.sample(name, 1)
    for breakfast_food in b_food:
        (breakfast_food["name"], breakfast_food["price"])

    for breakfast_drink in b_drink:
        (breakfast_drink["name"], breakfast_drink["price"])

    customers = [
        {"name" : r_name,
        "happiness_level" : happiness_level,
        "order_f" : breakfast_food["name"],
        "order_d" : breakfast_drink["name"],
        "price_f" :  breakfast_food["price"],
        "price_d" : breakfast_drink["price"]
        },

    ]

    for customer in customers:
        (customer["name"],"orders", customer["order_f"], customer["price_f"], customer["order_d"], customer["price_d"], customer["happiness_level"])
    for index, customers in enumerate(customers):
        print(customer["name"],"Customer orders", customer["order_f"], customer["price_f"], customer["order_d"], customer["price_d"],customer["happiness_level"])

if selection == "lunch":
    print("Lunch Menu: ")
    print("Foods")
    def show_menu(lunch_food):
        for index, lunch_food in enumerate(lunch_food):
            print(index, ":", lunch_food["name"], "-", lunch_food["price"])
    show_menu(lunch_food)
    print("Drinks")
    def show_menu(lunch_drink):
        for index,lunch_drink in enumerate(lunch_drink):
            print(index, ":", lunch_drink["name"], "-", lunch_drink["price"])
    show_menu(lunch_drink)
    def show_menu(lunch_appetizer):
        for index,lunch_appetizer in enumerate(lunch_appetizer):
            print(index, ":", lunch_appetizer["name"], "-", lunch_appetizer["price"])
    show_menu(lunch_appetizer)


    l_food = random.sample(lunch_food,1)
    l_drink = random.sample(lunch_drink,1)
    l_appetizer = random.sample(lunch_appetizer,1)
    r_name = random.sample(name, 1)
    for lunch_food in l_food:
        (lunch_food["name"], lunch_food["price"])

    for lunch_drink in l_drink:
        (lunch_drink["name"], lunch_drink["price"])
    
    for lunch_appetizer in l_appetizer:
        (lunch_appetizer["name"], lunch_appetizer["price"])

    customers = [
        {"name" : r_name,
        "happiness_level" : happiness_level,
        "order_f" : lunch_food["name"],
        "order_d" : lunch_drink["name"],
        "order_a" : lunch_appetizer["price"],
        "price_f" : lunch_food["price"],
        "price_d" : lunch_drink["price"],
        "price_a" : lunch_appetizer["price"]
        },

    ]

    for customer in customers:
        (customer["name"],"orders", customer["order_f"], customer["price_f"], customer["order_a"], customer["price_a"],customer["order_d"], customer["price_d"], customer["happiness_level"])
    for index, customers in enumerate(customers):
        print(customer["name"],"Customer orders", customer["order_f"], customer["price_f"], customer["order_a"], customer["price_a"],customer["order_d"], customer["price_d"], customer["happiness_level"])

if selection == "dinner":
    print("Dinner Menu: ")
    print("Foods")
    def show_menu(dinner_food):
        for index, dinner_food in enumerate(dinner_food):
            print(index, ":", dinner_food["name"], "-", dinner_food["price"])
    show_menu(dinner_food)
    print("Drinks")
    def show_menu(dinner_appetizer):
        for index, dinner_appetizer in enumerate(dinner_appetizer):
            print(index, ":", dinner_appetizer["name"], "-", dinner_appetizer["price"])
    show_menu(dinner_appetizer)
    print("Appetizer")

    def show_menu(dinner_dessert):
        for index, dinner_dessert in enumerate(dinner_dessert):
            print(index, ":", dinner_dessert["name"], "-", dinner_dessert["price"])
    show_menu(dinner_appetizer)

    l_food = random.sample(dinner_food,1)
    l_appetizer = random.sample(dinner_appetizer,1)
    l_dessert = random.sample(dinner_dessert,1)
    r_name = random.sample(name, 1)
    for dinner_food in l_food:
        (dinner_food["name"], dinner_food["price"])

    for dinner_dessert in l_dessert:
        (dinner_dessert["name"], dinner_dessert["price"])
    
    for dinner_appetizer in l_appetizer:
        (dinner_appetizer["name"], dinner_appetizer["price"])

    customers = [
        {"name" : r_name,
        "happiness_level" : happiness_level,
         "order_f" : dinner_food["name"],
         "order_a" : dinner_appetizer["name"],
         "order_d" : dinner_dessert["name"],
         "price_f" : dinner_food["price"],
         "price_a" : dinner_appetizer["price"],
         "price_d" : dinner_dessert["price"],
        },

    ]

    for customer in customers:
        (customer["name"],"orders", customer["order_f"], customer["price_f"], customer["order_a"], customer["price_a"], customer["order_d"], customer["price_d"],customer["happiness_level"],
)
    for index, customers in enumerate(customers):
        print(customer["name"],"Customer orders", customer["order_f"], customer["price_f"],  customer["order_a"], customer["price_a"], customer["order_d"], customer["price_d"], customer["happiness_level"])

class CustomerHappiness:
    def __init__(self, name, happiness_level):
        self.name = name
        self.happiness_level = happiness_level
    def add_or_subtract(self, amount):
        self.happiness_level += amount
r_name = CustomerHappiness(customer["name"], happiness_level)

start_time = time.time()
answer = input("Enter the instructions in order.")
end_time = time.time()
earnings = []
count = 0
total = 0
Serve = True
print("You have _ set amount of time to prepare the dish!")


if answer
while True:
        
    count += 1
    if end_time - start_time > 5:
        print("You have went overtime, customer happiness has decreased.")
        r_name.add_or_subtract(-10)
        print(r_name.__dict__)
        if happiness_level > 0:
            print(f"Customer has left and stolen ${steal}")
            BankAccount.deposit({steal})
            break

    elif answer == correct_a:
        print("Congrats you have prepare the dish!")
        earnings.append(customer["price_a"])
        break
    if count >= 5:
        Serve = False
    
""" for index in enumerate(customer["instructions"]):
    def i:
    i = index
 """
for earning in earnings:
    total += earning
    rounded_total = round(total, 2)
print(f"your total earnings you worked for today were: $${rounded_total}")
print(f"your tip amount is:  $${rounded_total}")


""" time.sleep(5)
print("Hi") """