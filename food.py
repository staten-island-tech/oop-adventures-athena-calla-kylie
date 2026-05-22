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
        "style": "strawberries" "blueberries" "bananas" "syrup" "chocolate syrup" "sprinkles" or "no toppings/sides"
        },

        {"name": "Pancakes with",
        "price": "$6.50",
        "style": "strawberries" "blueberries" "bananas" "syrup" "chocolate syrup" "sprinkles" or "no toppings/sides"
        },

        {"name": "Bacon and Eggs - ",
        "price": "$6.99",
        "style": "scrambled" or "sunny side up"
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

    {"name": "Cheescake",
     "price": "$6.50",
    }
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