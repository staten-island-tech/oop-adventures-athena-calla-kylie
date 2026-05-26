import random
import time
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
name = ["Abby", "Bob", "Calla", "Devi", "Eli", "Michael Francis Aaron Jake Diner", "George", "Henry", "Imogen", "Jonathan", "Katie", "Larry", "Michelle", "Nicole", "Opi", "Penguin"]
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
    r_status = random.sample(status, 1)
    for lunch_food in l_food:
        (lunch_food["name"], lunch_food["price"])

    for lunch_drink in l_drink:
        (lunch_drink["name"], lunch_drink["price"])
    
    for lunch_appetizer in l_appetizer:
        (lunch_appetizer["name"], lunch_appetizer["price"])

    customers = [
        {"name" : r_name,
        "status" : r_status,
        "order_f" : lunch_food["name"],
        "order_d" : lunch_drink["name"],
        "order_a" : lunch_appetizer["price"],
        "price_f" : lunch_food["price"],
        "price_d" : lunch_drink["price"],
        "price_a" : lunch_appetizer["price"]
        },

    ]

    for customer in customers:
        (customer["name"],"orders", customer["order_f"], customer["price_f"], customer["order_a"], customer["price_a"],customer["order_d"], customer["price_d"], customer["status"])
    for index, customers in enumerate(customers):
        print(customer["name"],"Customer orders", customer["order_f"], customer["price_f"], customer["order_a"], customer["price_a"],customer["order_d"], customer["price_d"], customer["status"])

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
    r_status = random.sample(status, 1)
    for dinner_food in l_food:
        (dinner_food["name"], dinner_food["price"])

    for dinner_dessert in l_dessert:
        (dinner_dessert["name"], dinner_dessert["price"])
    
    for dinner_appetizer in l_appetizer:
        (dinner_appetizer["name"], dinner_appetizer["price"])

    customers = [
        {"name" : r_name,
         "status" : r_status,
         "order_f" : dinner_food["name"],
         "order_a" : dinner_appetizer["name"],
         "order_d" : dinner_dessert["name"],
         "price_f" : dinner_food["price"],
         "price_a" : dinner_appetizer["price"],
         "price_d" : dinner_dessert["price"],
        },

    ]

    for customer in customers:
        (customer["name"],"orders", customer["order_f"], customer["price_f"], customer["order_a"], customer["price_a"], customer["order_d"], customer["price_d"],customer["status"])
    for index, customers in enumerate(customers):
        print(customer["name"],"Customer orders", customer["order_f"], customer["price_f"],  customer["order_a"], customer["price_a"], customer["order_d"], customer["price_d"], customer["status"])

start_time = time.time()
answer = input("Input")
end_time = time.time()
if end_time - start_time > 5:
    print("You have went overtime, customer happiness has decreased.")

else:
    print(":)")

""" time.sleep(5)
print("Hi") """