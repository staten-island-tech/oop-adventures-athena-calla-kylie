class menus():
    def __init__(self, order_name, description, price,):
        self.order_name = order_name
        self.description = description
        self.price = price
import random
import time
Menus = [
    {"name": "Breakfast"},
    {"name": "Lunch"},
    {"name": "Dinner"}
]

breakfast_food = [
        {"name": "Waffles",
        "price": "$5.99",
        "description": "Three golden-brown waffles, with crispy exterior and fluffy interior",
        "topping choice" : "strawberries, blueberries, bananas, syrup, chocolate syrup, sprinkles"
        },

        {"name": "Pancakes",
        "price": "$4.99",
        "description": "Three thick, fluffy golden-brown pancakes",
        "topping choice": "strawberries, blueberries, bananas, syrup, chocolate syrup, sprinkles"
        },

        {"name": "Bacon and Eggs",
        "price": "$6.99",
        "description": "Crispy bacon with two eggs",
        "style": "scrambled or sunny side up"
        },

        {"name": "Breakfast Burrito",
        "price": "$9.99",
        "description": "A flour tortilla filled with flavorful breakfast goods"
        }
    ]

breakfast_drink = [
        {"name": "Hot Coffee",
        "price": "$2.99",
        "description": "hot",
        "style": "espresso, americano, latte, or cappuccino",
        },

        {"name": "Apple Juice",
        "price": "$1.99",
        "description": "cold"},
                
        {"name": "Orange Juice",
        "price": "$1.99",
        "description": "cold"},

        {"name": "Milkshake",
        "price": "$3.99",
        "description": "cold",
        "style": "chocolate, strawberry, or vanilla"}
    ]

lunch_appetizer = [
        {"name": "Caesar Salad",
        "price": "",
        "description": ""},

        {"name": "Sausage Bites",
        "price": "",
        "description": "Spinach Artichoke Dip"},

        {"name": "Fried Zucchini",
        "price": "",
        "description": ""}
        ]

lunch_food = [
        {"name": "Macaroni and Cheese",
        "price": "$7.99",
        "description": "Cheesy"
        },        
        
        {"name": "Burger",
        "price": "$5.99",
        "description": ""
        },

        {"name": "Italian Grilled Cheese Sandwiches",
        "price": "",
        "description": ""
        },

        {"name": "Chicken Caesar Pasta Salad",
        "price": "",
        "description": ""
        },
    ]
    
lunch_drink = [
    {"name": "Soda",
     "price": "$0.99",
     "description": ""},

    {"name": "Iced Tea",
     "price": "$",
     "description": ""},

    {"name": "Lemonade",
     "price": "$",
     "description": ""},
    
    {"name": "Smoothie",
     "price": "$",
     "description": ""
     "s"}
    ]

dinner_appetizer = [
    {"name": "Spinach and Artichoke Dip",
     "price": "$",
     "description": ""},

    {"name": "",
     "price": "$",
     "description": ""},

    {"name": "",
     "price": "$",
     "description": ""},

    {"name": "",
     "price": "$",
     "description": ""}
    ]

dinner_food = [
    {"name": "",
     "price": "$",
     "description": ""},
    
    {"name": "",
     "price": "$",
     "description": ""},

    {"name": "",
     "price": "$",
     "description": ""},

    {"name": "",
     "price": "$",
     "description": ""}
    ]

dinner_dessert = [
    {"name": "",
     "price": "$",
     "description": ""},
    
    {"name": "",
     "price": "$",
     "description": ""},

    {"name": "",
     "price": "$",
     "description": ""},

    {"name": "",
     "price": "$",
     "description": ""}
    ]
name = ["Abby", "Bob", "Calla", "Devi", "Eli", "Francis", "George", "Henry", "Imogen", "Jonathan", "Katie", "Larry", "Michelle", "Nicole", "Opi", "Penguin"]
status = ["SUPER Happy (100)", "Happy (99)", "Nonchalant (88)", "Annoyed (75)", "SUPER Annoyed (70)", "Mad (55)", "HUNGRY... (30)", "I AM GODZILLA (0)", "SO MAD IM ON FIRE!!!! (-10)"]
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
    r_status = random.sample(status, 1)
    for breakfast_food in b_food:
        (breakfast_food["name"], breakfast_food["price"])

    for breakfast_drink in b_drink:
        (breakfast_drink["name"], breakfast_drink["price"])

    customers = [
        {"name" : r_name,
        "status" : r_status,
        "order_f" : breakfast_food["name"],
        "order_d" : breakfast_drink["name"],
        "price_f" :  breakfast_food["price"],
        "price_d" : breakfast_drink["price"],
        },

    ]

    for customer in customers:
        (customer["name"],"orders", customer["order_f"], customer["price_f"], customer["order_d"], customer["price_d"], customer["status"])
    for index, customers in enumerate(customers):
        print(customer["name"],"Customer orders", customer["order_f"], customer["price_f"], customer["order_d"], customer["price_d"], customer["status"])
if selection == "lunch":
    print("Lunch Menu: ")
    print("Foods")
    def show_menu(lunch):
        for index, lunch_food in enumerate(lunch_food):
            print(index, ":", lunch_food["name"], "-", lunch_food["price"])
    show_menu(lunch_food)
    print("Drinks")
    def show_menu(breakfast_drink):
        for index, breakfast_drink in enumerate(breakfast_drink):
            print(index, ":", breakfast_drink["name"], "-", breakfast_drink["price"])
    show_menu(breakfast_drink)

    b_food = random.sample(breakfast_food,1)
    b_drink = random.sample(breakfast_drink,1)
    r_name = random.sample(name, 1)
    r_status = random.sample(status, 1)
    for breakfast_food in b_food:
        (breakfast_food["name"], breakfast_food["price"])

    for breakfast_drink in b_drink:
        (breakfast_drink["name"], breakfast_drink["price"])

    customers = [
        {"name" : r_name,
        "status" : r_status,
        "order_f" : breakfast_food["name"],
        "order_d" : breakfast_drink["name"],
        "price_f" :  breakfast_food["price"],
        "price_d" : breakfast_drink["price"],
        },

    ]

    for customer in customers:
        (customer["name"],"orders", customer["order_f"], customer["price_f"], customer["order_d"], customer["price_d"], customer["status"])
    for index, customers in enumerate(customers):
        print(customer["name"],"Customer orders", customer["order_f"], customer["price_f"], customer["order_d"], customer["price_d"], customer["status"])

time.sleep(5)
print("Hi")