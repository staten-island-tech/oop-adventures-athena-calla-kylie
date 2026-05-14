    

customer_orders_day_one = [
{
    "name": "Julia",
    "price": 12.99,
    "tip": 2.00,
    "order": "{menu_selection}",
    "instructions": "Toast the waffles, add syrup, add blueberries.",
    "status": "angry"
},
{
    "name": "Gerald",
    "price": 4.99,
    "tip": 0.50,
    "order": "hot coffee with milk and sugar",
    "instructions": "pour the coffee, add a splash of milk, and a teaspoon of sugar.",
    "status": "calm"
},
{
    "name": "Agamemnon",
    "price": 120,
    "tip": 0.000000000001,
    "order": "Two kids meal pancakes, an adult size bacon and eggs, covered in gold leaf.",
    "instructions": "Toast the waffles, add syrup, add blueberries, put on two plates. Fry the bacon and eggs, put on a plate.",
    "status": "LIVID."
},
{
    "name": "Lyla",
    "price": 24.99,
    "tip": 5.00,
    "order": "menu.choice}",
    "instructions": "Heat up the mac anc cheese, plate, sprinke extra cheese on one of them.",
    "status": "LIVID."
},
{
    "name": "odysseus",
    "price": 24.99,
    "tip": 2.00,
    "order": "Mac and Cheese (3 orders plus extra cheese on one of them).",
    "instructions": "Heat up the mac anc cheese, plate, sprinke extra cheese on one of them.",
    "status": "LIVID."
},
{
    "name": "Jake",
    "price": 12.99,
    "tip": 4.00,
    "order": "Mac and Cheese (3 orders plus extra cheese on one of them).",
    "instructions": "Heat up the mac anc cheese, plate, sprinke extra cheese on one of them.",
    "status": "LIVID."
},
{
    "name": "Marty",
    "price": 7.99,
    "tip": 2.00,
    "order": "Mac and Cheese (3 orders plus extra cheese on one of them).",
    "instructions": "Heat up the mac anc cheese, plate, sprinke extra cheese on one of them.",
    "status": "chill."
},
{
    "name": "chris",
    "price": 6.99,
    "tip": 1.00,
    "order": "Bacon and eggs",
    "instructions": "Heat up the mac anc cheese, plate, sprinke extra cheese on one of them.",
    "status": "hungry."
},
{
    "name": "Mr. Whalen",
    "price": 5000000.99,
    "tip": 0.00,
    "order": "everyting. give me everything.",
    "instructions": "Heat up the mac anc cheese, plate, sprinke extra cheese on one of them.",
    "status": "LIVID."
},
    ]
'''class Customer:
    def __init__(self, name, order, status):
        self.name = name 
        self.order = order
        self.status = status
name = Customer()'''


earnings = []
extra_tips = []
total_money = 0
totaltips = 0
customer_history = []
work = True
for index, customer in enumerate(customer_orders_day_one):
        print(index, ":", customer["name"],customer["status"])

while work:
    serve_customers = int(input("Serve customer? Type the number of the customer you want to serve first based on status."))
    customer_history.append(customer_orders_day_one[serve_customers]["name"])
    earnings.append(customer_orders_day_one[serve_customers]["price"])
    extra_tips.append(customer_orders_day_one[serve_customers]["tip"])
    work_continiue = input("continue working or calculate earnings and score for today? Enter Yes (continiue) or No (calculate)")

    if work_continiue == "No":
         work = False

for earning in earnings:
    total_money += earning
    rounded_total_money = round(total_money, 2)
for tips in extra_tips:
    totaltips += tips
    rounded_total_tips = round(totaltips, 2)

print(f"your total earnings you worked for today were: $${rounded_total_money}")
print(f"your tip amount is:  $${rounded_total_tips}")
print(f"customers served today included: {customer_history}")
    
