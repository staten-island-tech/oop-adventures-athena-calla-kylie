import random
breakfast_food = {
        "name": "Waffles - ",
        "instructions": ["create batter", "preheat waffle iron", "pour batter into machine", "take the waffle out", "select toppings if necessary"]
        }


random.shuffle(breakfast_food["instructions"])
print(breakfast_food)