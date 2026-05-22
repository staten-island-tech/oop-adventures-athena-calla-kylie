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

name = ["Abby", "Bob", "Calla", "Devi", "Eli", "Diner", "George", "Henry", "Imogen", "Jonathan", "Katie", "Larry", "Michelle", "Nicole", "Opi", "Penguin"]
status = ["SUPER Happy (100)", "Happy (99)", "Nonchalant (88)", "Annoyed (75)", "SUPER Annoyed (70)", "Mad (55)", "HUNGRY... (30)", "I AM GODZILLA (0)", "SO MAD IM ON FIRE!!!! (-10)"]

class CustomerHappiness:
    def __init__(self, name, status, happiness_level):
        self.name = name
        self.happiness_level = happiness_level
        self.status = status
    def add_or_subtract(self, amount):
        self.happiness_level += amount



