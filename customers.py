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
{
    "name": "Lyla",
    "price": 24.99,
    "food type": "Mac and Cheese (3 orders plus extra cheese on one of them).",
    "instructions": "Heat up the mac anc cheese, plate, sprinke extra cheese on one of them.",
    "status": "LIVID."
},
    ]

earnings = []
total_money = 0
customer_history = []
work = True
for index, customer in enumerate(customer_orders_day_one):
        print(index, ":", customer["name"],customer["status"])

while work:
    serve_customers = int(input("Serve customer? Type the number of the customer you want to serve first based on status."))
    customer_history.append(customer_orders_day_one[serve_customers]["name"])
    earnings.append(customer_orders_day_one[serve_customers]["price"])
    work_continiue = input("continue working or calculate earnings and score for today? Enter Yes (continiue) or No (calculate)")

    if work_continiue == "No":
         work = False


if work == False:
    for customer in customer_history:
        print(f"{customer_history}")

for earning in earnings:
    total_money += earning
print(total_money)
for customer in customer_history:
     print(f"{customer_history}")
    

