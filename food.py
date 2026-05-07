""" class menu():
    def __init__(self, order_name, description, price,):
        self.order_name = order_name
        self.description = description
        self.price = price """

Menus = [
    {"name": "Breakfast"},
    {"name": "Lunch"},
    {"name": "Dinner"}
]


""" if input == "0" or "Breakfast":
    print("Breakfast Menu: ")
elif input == "1" or "Lunch":
    print("Lunch Menu: ")
elif input == "2" or "Dinner":
    print("Dinner Menu: ") """

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
        }
    ]

breakfast_drink = [
        {"name": "Hot Coffee",
        "price": "$2.99",
        "description": "hot",
        "style": "espresso, americano, latte, or cappuccino" },

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

def show_menus(Menus):
    for index, Menus in enumerate(Menus):
        print(index, ":", Menus["name"])
show_menus(Menus)
print(input("Select your choice of menu: "))

if input == "0" or "Breakfast":
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

elif input == "1" or "Lunch":
    print("Lunch Menu: ")

elif input == "2" or "Dinner":
    print("Dinner Menu: ")



