from pathlib import Path
import json

data_path = Path(__file__).parents[1] / "data"

with open(data_path / "orders.json", "r") as file:
        orders = json.load(file) 

for i in orders:
    print(f"Input:{i}")
    print(f"Customer name = {i['customer']}")
    total = 0
    for x in i["products"]:
        print(f"Product: {x['name']:<20} Quantity: {x['quantity']:<20} Price:{x['price']}")
        total += x['quantity'] * x['price']
    print(f"Total price: {total}")
        
    







