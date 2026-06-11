import random
import time

class server_profile:
        def __init__(self, name, gender, workdays):
            self.name = name 
            self.gender = gender
            self.workdays = workdays
class Server:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

user_name = input("Hello! Please enter your name:")
print(f"Welcome to {user_name}'s Resturaunt! You are now a server at rank {1} with {"ZERO"} customers served so far.")
print("If you need instructions on how to play, write 'Yes'. If you are ready to play now, write 'No' in the box below.")

instructions = input("Instructions? ::")

if instructions == ("Yes"):
        print(f"Hello my dear {user_name}!! I do hope your day is going well. Are you ready to master the restauraunt business? Or maybe not... Maybe you aren't ready. Are you?")
        ready = input("Are you ready for this?")
        print(f"Oh okay good, good. I am Luigi, the god of the restauraunt business. I will show you the ways of serving. Ready?")
        print("Step one: Show the customers the menu. Make sure they choose an item, which will print below for you.")
        ready2 = input("Got it??")
        print("Step two: check the customer's status (also printed below). If they are anything below annoyed, you need to REALLY make sure to get their order right... or else you lose money.")
        ready3 = input("Understood?")
        print(f"well then, {user_name}, it seems you are well prepared for the ordeal ahead. try to collect as many tips and earnings as you can, you can use them in the inventory store when you finish day one. Best of luck {user_name}, and I'll see you on the other side! XX, Luigi")
        finalready = input("Ready?")
        print("GAME START!!")
else: print("GAME START!!")

name = Server(user_name, 0, ["nothing yet"])
print(name.__dict__)

serve = input("Serve your first customer by entering ['Next Customer!']")
## REMEMBER TO INSERT ATHENA AND KYLIE AND MY CODE HERE


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
name = BankAccount(user_name, 100) 

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

lunch_appetizer = [
        {"name": "Caesar Salad",
        "price": "$3.99",
        "instructions": ["add toppings, aka tomatoes and croutons on the iceburg lettuce", "pour dressing over the salad"] 
        },

        {"name": "Sausage Bites",
        "price": "$3.50",
        "instructions": ["cut the sausage into small pieces", "preheat oven", "bake the sausage bites for ten minutes at 450", "serve hot"] 
        },

        {"name": "Spinach Artichoke Dip",
        "price": "$3.50",
        "instructions": ["prepare cream cheese, sour cream, and mayonnaise", "stir", "add the greens and artichokes"] 
        },

        {"name": "Mozzarella Sticks",
        "price": "$3.99",
        "instructions": ["preheat oven to 400", "Bread mozerella sticks in bread crumbs and egg", "bake at 400 for 12 minutes, or until crispy"]
        }
        ]

lunch_food = [
        {"name": "Macaroni and Cheese",
        "price": "$7.99",
        "instructions": ["Add boiled pasta and cheese to a baking dish", "sprinke cheddar on top and add cream cheese to the mixture", "top with customer's choice"]
        },        
        
        {"name": "Burger",
        "price": "$8.99",
        "instructions": ["fry bread", "cook the meat and neccesary ingredients", "sandwich patties, tomato, lettuce, onions, cheese onto bread"]   
        },

        {"name": "Grilled Cheese Sandwiches",
        "price": "$8.50",
        "instructions":["place bread on skillet", "spread butter on one slice", "top with sliced cheese on another", "cook until golden brown and melted"]
        },

        {"name": "Chicken Caesar Pasta Salad",
        "price": "$7.99",
        "instructions": ["cook pasta", "assemble salad", "add caesar dressing", "toss until evenly coated"]
        }
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
     "style": "strawberry banana" "mixed berries" or "tropical mango",
     "instructions": ["select fruits", "add milk", "blend until smooth"]
    }
    ]

dinner_appetizer = [
    {"name": "Spinach and Artichoke Dip",
     "price": "$3.50",
     "instructions": ["prepare cream cheese, sour cream, and mayonnaise", "stir", "add the greens and artichokes"]
    },

    {"name": "Sausage Bites",
     "price": "$3.50",
     "instructions": ["cut the sausage intop small pieces", "preheat oven", "bake the sausage bites"]
    },

    {"name": "Smoked Salmon",
     "price": "$4.99",
     "instructions": ["prep salmon(remove bones)", "coat with sea salt and brown sugar", "place in fridge until firm", "smoke it", "place onto crackers with cream cheese"]
    },

    {"name": "Charcuterie Board",
     "price": "$7.99",
     "instructions": ["grab items", "separate into 'islands'", "decorate neatly"]
    }
    ]

dinner_food = [
    {"name": "Spaghetti and Meatballs",
     "price": "$8.99",
     "instructions": ["combine ingredients and mix gently", "roll into balls", "cook meatballs in the pan until brown", "cook spaghetti in separate pot", "transfer onto plate"]
    },
    
    {"name": "Chicken Alfredo",
     "price": "$9.99",
     "instructions": ["boil pasta", "cook seasoned chicken", "make alfredo sauce", "combine pasta and sauce and lay sliced chicken on top"]
    },

    {"name": "Cast-Iron Steak - ",
     "price": "$14.99",
     "style" :"rare" "medium-rare" "medium" "medium well" or "well done",
     "instructions": ["pat and season steak", "lay steak onto pan", "flip", "baste with butter", "place onto plate and pour remaining pan juices"]
    },

    {"name": "Burger",
     "price": "$8.99",
     "instructions": ["fry bread", "cook the meat and neccesary ingredients", "sandwich patties, tomato, lettuce, onions, cheese onto bread"]
     }
    ]


dinner_dessert = [
    {"name": "Icecream",
     "price": "$3.99",
     "style": "chocolate" "strawberry" "vanilla" or "matcha",
     "instructions": ["select icecream flavor", "scoop icecream"]
     },
    
    {"name": "Molten Lava Cake",
     "price": "$7.99",
     "instructions":["butter and dust muffin tins", "melt and create chocolate mixture", "bake", "plate it and sprinkle with powder"]
    },

    {"name": "Chocolate Chip Cookies",
     "price": "$4.99",
     "instructions":["prep equipment and oven", "mix dry ingredients", "add wet ingredients", "spread onto baking sheet", "bake"]
    },

    {"name": "Cheescake",
     "price": "$6.50",
     "instructions":["create crust", "prepare the filling", "bake in warm water bath", "bake in oven", "refrigerate"]
    }
    ]
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
    b_food = random.choice(breakfast_food)
    b_drink = random.sample(breakfast_drink)
    correct_order = b_food["instructions"]
    shuffled = correct_order[:] 
    random.shuffle(shuffled)
    print(f"Your item: {b_food["name"]} ({b_food["price"]})")
    print(f"Your item: {b_drink["name"]} ({b_drink["price"]})")
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
    l_food = random.sample(lunch_food)
    l_drink = random.sample(lunch_drink)
    l_appetizer = random.sample(lunch_appetizer)
    correct_order = l_food["instructions"]
    shuffled = correct_order[:] 
    random.shuffle(shuffled)
    print(f"Your item: {l_food["name"]} ({l_food["price"]})")
    print(f"Your item: {l_drink["name"]} ({l_drink["price"]})")


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
    show_menu(dinner_dessert)

    d_food = random.sample(dinner_food)
    d_appetizer = random.sample(dinner_appetizer)
    d_dessert = random.sample(dinner_dessert)
    correct_order = d_food["instructions"]
    shuffled = correct_order[:] 
    random.shuffle(shuffled)
    print(f"Your item: {d_food["name"]} ({d_food["price"]})")
    print(f"Your item: {d_appetizer["name"]} ({d_appetizer["price"]})")
    print(f"Your item: {d_dessert["name"]} ({d_dessert["price"]})")


earnings = []
total_money = 0
work = True
while work:
    for i, step in enumerate(shuffled, 1): 
        print(f"{i}. {step}") 
        user_input = input("Rearrange the list of instructions.")
        order = [int(x.strip()) for x in user_input.split(",")]
        sequence = [shuffled[i - 1] for i in order]
        if sequence == correct_order:
            print("Correct!")
        else:
            print("Incorrect.")