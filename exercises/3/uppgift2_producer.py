# from pathlib import Path
# import json
# from quixstreams import Application

# data_path = Path(__file__).parent / "data"

# with open(data_path / "orders.json", "r") as file:
#         orders = json.load(file)

# app = Application(
#     broker_address="localhost:9095",
#     consumer_group="text-splitter")

# # print(app)

# order_topic = app.topic(name = "orders", value_serializer="json")

# # print(order_topic)

# def main():
    
#     with app.get_producer() as producer:
        
#         # print(producer)
        
#         for i in orders:
#             kafka_msg = order_topic.serialize(key=i['order_id'], value = i)
#             print(f"Input:{kafka_msg}")
#             # print(f"Customer name = {i['customer']}")
#             total = 0
#             total2 = order_topic.serialize(total)
#             for x in i["products"]:
#                 kafka_msg2 = order_topic.serialize(key=x['products'], value = x)
#                 print(f"Product: {kafka_msg2.value['name']:<20} Quantity: {kafka_msg.value['quantity']:<20} Price:{kafka_msg2.value['price']}")
#                 total += kafka_msg2.values()['quantity'] * kafka_msg2.value['price']
#                 print(f"Total price: {total}")
                
#                 producer.produce(topic="orders", key=str(kafka_msg.key, kafka_msg2.key), total2)
                
# if __name__ == '__main__':
#         main()
                

from pathlib import Path
import json
from quixstreams import Application

# Define the data path
data_path = Path(__file__).parent / "data"

# Load orders from JSON file
with open(data_path / "orders.json", "r") as file:
    orders = json.load(file)

# Initialize Kafka application
app = Application(
    broker_address="localhost:9092",
    consumer_group="text-splitter"
)

# Define the Kafka topic
order_topic = app.topic(name="orders", value_serializer="json")

def main():
    with app.get_producer() as producer:
        for order in orders:
            # Serialize order data
            kafka_msg = order_topic.serialize(key=order["order_id"], value=order)
            
            print(f"Total individual order: \n \n {order}\n")
            print(f"Customer name: {order['customer']}\n")

            total = 0
            for product in order["products"]:
                product_name = product["name"]
                product_quantity = product["quantity"]
                product_price = product["price"]

                print(f"Product: {product_name:<20} Quantity: {product_quantity:<5} Price: {product_price}")
                total += product_quantity * product_price

            print(f"Total price: {total:.2f}\n")

            # Produce the message to Kafka
            producer.produce(topic="orders", key=str(kafka_msg.key), value=kafka_msg.value)

if __name__ == '__main__':
    main()


   