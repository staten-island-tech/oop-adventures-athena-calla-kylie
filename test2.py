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

menu_instruct = breakfast_food[0]["name"]["instructions"]

""" for food_dict in breakfast_food:
    instruction_info = food_dict.get(breakfast_food[instructions], {})
    if instructions in instruction_info:
        print(instruction_info[instructions]) """

""" for dictionary in breakfast_food:
    for key, value in dictionary.items():
        print(key, value)
for menu, info in breakfast_food.items():
    print(info["name"]["instructions"]) """
