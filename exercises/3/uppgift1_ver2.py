from pathlib import Path
import json

path = Path(__file__).parent / "data"

with open(path / "orders.json", "r") as file:
    orders = json.load(file)
    
print(orders)

total = 0

for order in orders:
    print(f"\n")
    print(f" Customer name: {order['customer']}\n")
    print(f" Total order: {order}\n")
        
    for products in order['products']:
        
        print(f"Product: {products['name']:<20}Quantity: {products['quantity']:<20}price: {products['price']}")
        total += products['quantity']*products['price']
        print(f"Total price: {total}")
    