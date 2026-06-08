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


