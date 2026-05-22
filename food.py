import time

class menus():
    def __init__(self, order_name, description, price,):
        self.order_name = order_name
        self.description = description
        self.price = price

Menus = [
    {"name": "Breakfast"},
    {"name": "Lunch"},
    {"name": "Dinner"}
]

breakfast_food = [
        {"name": "Waffles - ",
        "price": "$6.99",
        "description": "Three golden-brown waffles, with crispy exterior and fluffy interior",
        "topping choice" : "strawberries" "blueberries" "bananas" "syrup" "chocolate syrup" "sprinkles" "no toppings/sides"
        },

        {"name": "Pancakes with",
        "price": "$6.50",
        "description": "Three thick, fluffy golden-brown pancakes",
        "topping choice": "strawberries" "blueberries" "bananas" "syrup" "chocolate syrup" "sprinkles"
        },

        {"name": "Bacon and Eggs - ",
        "price": "$6.99",
        "description": "Crispy bacon with two eggs",
        "style": "scrambled" or "sunny side up"
        },

        {"name": "Breakfast Burrito",
        "price": "$9.99",
        "description": "A flour tortilla filled with flavorful breakfast goods"
        }
    ]

breakfast_drink = [
        {"name": "Hot Coffee - ",
        "price": "$1.99",
        "description": "hot",
        "style": "espresso" "americano" "latte" or "cappuccino",
        },

        {"name": "Apple Juice",
        "price": "$0.99",
        "description": "cold"},
                
        {"name": "Orange Juice",
        "price": "$0.99",
        "description": "cold"},

        {"name": "Milkshake - ",
        "price": "$3.99",
        "description": "cold",
        "style": "chocolate" "strawberry" or "vanilla"}
    ]

lunch_appetizer = [
        {"name": "Caesar Salad",
        "price": "$3.99",
        "description": ""},

        {"name": "Sausage Bites",
        "price": "$3.50",
        "description": ""},

        {"name": "Spinach Artichoke Dip",
        "price": "$3.50",
        "description": ""},

        {"name": "Mozzarella Sticks",
        "price": "$3.99",
        "description": ""}
        ]

lunch_food = [
        {"name": "Macaroni and Cheese",
        "price": "$7.99",
        "description": "Cheesy"
        },        
        
        {"name": "Burger",
        "price": "$8.99",
        "description": ""
        },

        {"name": "Italian Grilled Cheese Sandwiches",
        "price": "$8.50",
        "description": ""
        },

        {"name": "Chicken Caesar Pasta Salad",
        "price": "$7.99",
        "description": ""
        },
    ]
    
lunch_drink = [
    {"name": "Soda",
     "price": "$0.99",
     "description": ""},

    {"name": "Iced Tea",
     "price": "$0.99",
     "description": ""},

    {"name": "Lemonade",
     "price": "$0.99",
     "description": ""},
    
    {"name": "Smoothie",
     "price": "$3.99",
     "description": ""
     "s"}
    ]

dinner_appetizer = [
    {"name": "Spinach and Artichoke Dip",
     "price": "$3.50",
     "description": ""},

    {"name": "Sausage Bites",
     "price": "$3.50",
     "description": ""},

    {"name": "Smoked Salmon",
     "price": "$4.99",
     "description": ""},

    {"name": "Charcuterie Board",
     "price": "$7.99",
     "description": ""}
    ]

dinner_food = [
    {"name": "Spaghetti and Meatballs",
     "price": "$8.99",
     "description": ""},
    
    {"name": "Chicken Alfredo",
     "price": "$9.99",
     "description": ""},

    {"name": "Cast-Iron Steak - ",
     "price": "$14.99",
     "description": "",
     "style" :"rare" "medium-rare" "medium" "medium well" or "well done"},

    {"name": "Burger",
     "price": "$8.99",
     "description": ""}
    ]


dinner_dessert = [
    {"name": "Icecream",
     "price": "$3.99",
     "description": ""},
    
    {"name": "Molten Lava Cake",
     "price": "$7.99",
     "description": ""},

    {"name": "Chocolate Chip Cookies",
     "price": "$4.99",
     "description": ""},

    {"name": "Cheescake",
     "price": "$6.50",
     "description": ""}
    ]

import random
breakfast_f = [breakfast_food["name"], breakfast_drink["name"]]
b_selection = random.sample(breakfast_f, 1, 1)

import random
lunch_choice = [lunch_food["name"], lunch_drink["name"]]
l_selection = random.sample(lunch_choice, 1, 1) 

import random
dinner_choice = [dinner_food["name"], lunch_drink["name"]]
d_selection = random.sample(dinner_choice, 1, 1)

def show_menus(Menus):
    for index, Menus in enumerate(Menus):
        print(index, ":", Menus["name"])
show_menus(Menus)
print("You: 'Hi! Select your menu!'")
print(". . .")
import random
menu_choice = ["breakfast", "lunch", "dinner"]
selection = random.choice(menu_choice)
print("Customer selects the", (selection), "menu")
print("Show customers the menu...")
time.sleep(2)


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
    
    print("Customer orders", (b_selection))

elif selection == "lunch":
    print("Lunch Menu: ")
    print("Appetizers")
    def show_menu(lunch_appetizer):
        for index, lunch_appetizer in enumerate(lunch_appetizer):
            print(index, ":", lunch_appetizer["name"], "-", lunch_appetizer["price"])
    show_menu(lunch_appetizer)
    print("Foods")
    def show_menu(lunch_food):
        for index, lunch_food in enumerate(lunch_food):
            print(index, ":", lunch_food["name"], "-", lunch_food["price"])
    show_menu(lunch_food)
    print("Drinks")
    def show_menu(lunch_drink):
        for index, lunch_drink in enumerate(lunch_drink):
            print(index, ":", lunch_drink["name"], "-", lunch_drink["price"])
    show_menu(lunch_drink)

    print("Customer orders", (l_selection))


elif selection == "dinner":
    print("Dinner Menu: ")
    print("Appetizers")
    def show_menu(dinner_appetizer):
        for index, dinner_appetizer in enumerate(dinner_appetizer):
            print(index, ":", dinner_appetizer["name"], "-", dinner_appetizer["price"])
    show_menu(dinner_appetizer)
    print("Foods")
    def show_menu(dinner_food):
        for index, dinner_food in enumerate(dinner_food):
            print(index, ":", dinner_food["name"], "-", dinner_food["price"])
    show_menu(dinner_food)
    print("Drinks")
    def show_menu(dinner_dessert):
        for index, dinner_dessert in enumerate(dinner_dessert):
            print(index, ":", dinner_dessert["name"], "-", dinner_dessert["price"])
    show_menu(dinner_dessert)
    def show_menu(lunch_drink):
        for index, lunch_drink in enumerate(lunch_drink):
            print(index, ":", lunch_drink["name"], "-", lunch_drink["price"])
    show_menu(lunch_drink)
    print("Customer orders", (d_selection))