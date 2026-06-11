if selection == "lunch":
        print("Lunch Menu: ")
        print("Foods")
        def show_menu(lunch_food):
                for index, lunch_food in enumerate(lunch_food):
                        print(index, ":", lunch_food["name"], "-", lunch_food["price"])
                        show_menu(lunch_food)
        l_food = random.choice(lunch_food,1)
        l_drink = random.sample(lunch_drink,1)
        l_appetizer = random.sample(lunch_appetizer,1)
        r_name = random.sample(name, 1)
        for lunch_food in l_food:
                (lunch_food["name"], lunch_food["price"])
for lunch_drink in l_drink:
        (lunch_drink["name"], lunch_drink["price"])
for lunch_appetizer in l_appetizer:
        (lunch_appetizer["name"], lunch_appetizer["price"])
customers = [{"name" : r_name,
              "happiness_level" : happiness_level,
              "order_f" : lunch_food["name"],
              "order_d" : lunch_drink["name"],
              "order_a" : lunch_appetizer["price"],
              "price_f" : lunch_food["price"],
              "price_d" : lunch_drink["price"],
              "price_a" : lunch_appetizer["price"]},
              ]
for customer in customers:(customer["name"],"orders", customer["order_f"], customer["price_f"], customer["order_a"], customer["price_a"],customer["order_d"], customer["price_d"], customer["happiness_level"])    for index, customers in enumerate(customers):        print(customer["name"],"Customer orders", customer["order_f"], customer["price_f"], customer["order_a"], customer["price_a"],customer["order_d"], customer["price_d"], customer["happiness_level"])
correct_order = l_food["instructions"]
shuffled = correct_order[:] 
random.shuffle(shuffled)
print(f"Your item: {l_food['name']} 
        ({l_food['price']})")

import random
breakfast_food = [
        {"name": "Waffles - ",
        "price": "$6.99",
        "style": "strawberries" "blueberries" "bananas" "syrup" "chocolate syrup" "sprinkles" or "no toppings",
        "instructions": ["create batter", "preheat waffle iron", "pour batter into machine", "take the waffle out", "select toppings if necessary"]
        },

        {"name": "Pancakes with",
        "price": "$6.50",
        "style": "strawberries" "blueberries" "bananas" "syrup" "chocolate syrup" "sprinkles" or "no toppings",
        "instructions": ["create batter", "preheat the pan", "pour into pan", "flip when underside is golden brown", "take the pancake out", "select toppings if necessary"]
        },

        {"name": "Bacon and Eggs - ",
        "price": "$6.99",
        "style": "scrambled" or "sunny side up",
        "instructions": ["grab bacon", "take out when fully cooked", "cook the eggs"]
        },

        {"name": "Breakfast Burrito",
        "price": "$9.99",
        "instructions": ["lay out tortilla", "place ingredients inside", "wrap it up"]
        }
]

breakfast_drink = [
        {"name": "Hot Coffee - ",
        "price": "$1.99",
        "style": "espresso" "americano" "latte" or "cappuccino",
        "instructions": ["place paper filter and rinse with hot water", "grind coffee beans", "add the grounds into filter", "brew coffee"]
        },

        {"name": "Apple Juice",
        "price": "$0.99"
        },
                
        {"name": "Orange Juice",
        "price": "$0.99",
        },

        {"name": "Milkshake - ",
        "price": "$3.99",
        "style": "chocolate" "strawberry" or "vanilla",
        "instructions":["select ice cream flavor", "add milk", "blend until smooth"]
        }
    ]

instructionsbf = breakfast_food[0]
menu_instructbf = breakfast_food[0]["instructions"]
random.shuffle(menu_instructbf)
print(menu_instructbf)

instructionsbd = breakfast_drink[0]
menu_instructbd = breakfast_drink[0]["instructions"]
random.shuffle(menu_instructbd)
print(menu_instructbd)


