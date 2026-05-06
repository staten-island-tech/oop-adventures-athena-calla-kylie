""" class costumer:
    def __init__(self, name, order):
        self.name = name 
        self.order = order

    customer_order = input("Please choose your order from the ") """

customer_orders_day_one = [
{
    "name": "Julia",
    "price": 12.99,
    "food type": "waffles with syrup and blueberries",
    "instructions": "Toast the waffles, add syrup, add blueberries.",
    "status": "angry"
},
{
    "name": "Gerald",
    "price": 4.99,
    "food type": "hot coffee with milk and sugar",
    "instructions": "pour the coffee, add a splash of milk, and a teaspoon of sugar.",
    "status": "calm"
},
{
    "name": "Agamemnon",
    "price": 120,
    "food type": "Two kids meal pancakes, an adult size bacon and eggs, covered in gold leaf.",
    "instructions": "Toast the waffles, add syrup, add blueberries, put on two plates. Fry the bacon and eggs, put on a plate.",
    "status": "LIVID."
},
    ]
for customer in customer_orders_day_one:
    print(f"Customer Name: {customer["name"]}, Customer Status: {customer["status"]}")

    customer_choice = input("Please enter the name of the customer you would like to serve.")
    if customer_choice in customer_orders_day_one:
        print(customer_orders_day_one['name'],['price'],['food type'],['instructions'],['status'])
