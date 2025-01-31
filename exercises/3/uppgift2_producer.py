# from pathlib import Path
# import json
# from quixstreams import Application

# # Define the data path
# data_path = Path(__file__).parent / "data"

# # Load orders from JSON file
# with open(data_path / "orders.json", "r") as file:
#     orders = json.load(file)

# # Initialize Kafka application
# app = Application(
#     broker_address="localhost:9092",
#     consumer_group="text-splitter"
# )

# # Define the Kafka topic
# order_topic = app.topic(name="orders", value_serializer="json")

# def main():
#     with app.get_producer() as producer:
#         for order in orders:
#             # Serialize order data
#             kafka_msg = order_topic.serialize(key=order["order_id"], value=order)
            
#             print(f"Total individual order: \n \n {order}\n")
#             print(f"Customer name: {order['customer']}\n")

#             total = 0
#             for product in order["products"]:
#                 product_name = product["name"]
#                 product_quantity = product["quantity"]
#                 product_price = product["price"]

#                 print(f"Product: {product_name:<20} Quantity: {product_quantity:<5} Price: {product_price}")
#                 total += product_quantity * product_price

#             print(f"Total price: {total:.2f}\n")

#             # Produce the message to Kafka
#             producer.produce(topic="orders", key=str(kafka_msg.key), value=kafka_msg.value)

# if __name__ == '__main__':
#     main()



                
    
        

        
           