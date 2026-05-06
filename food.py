class menu():
    def __init__(self, order_name, description, price,):
        self.order_name = order_name
        self.description = description
        self.price = price

food_menu = [
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
             "description": "Four pieces of crispy bacon with two eggs",
             "style": "scrambled or sunny side up"
            }
        ]

drink_menu = [
            {"name": "Hot Coffee",
             "price": "$2.99",
             "description": "",
             "style": "espresso, americano, latte, or cappuccino" },

            {"name": "Apple Juice",
             "price": "$1.99",
             "description": ""},
            
            {"name": "Orange Juice",
             "price": "$1.99",
             "description": ""},

            {"name": "milkshake",
             "price": "$3.99",
             "description": "",
             "style": "chocolate, strawberry, or vanilla"}
        ]

print(food_menu["name"])
print(drink_menu["name"])


