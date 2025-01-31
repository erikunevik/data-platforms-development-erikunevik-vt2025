# from quixstreams import Application

# app = Application(
#     broker_address="localhost:9092",
#     consumer_group="text-splitter",
#     auto_offset_reset="earliest",
# )

# order_topic = app.topic(name="orders", value_deserializer="json")

# sdf = app.dataframe(topic=order_topic)

# def process_message(order):
#     print(f"\nTotal individual order: \n {order}\n")
#     print(f"\nCustomer name = {order['customer']}\n")

#     total_price = 0
#     for product in order["products"]: 
#         name = product['name']
#         price = product["price"]
#         quantity = product["quantity"]
#         total_price += price * quantity
#         print(f"Product: {name:<25} Quantity: {quantity:<5} Price: {price:.2f}")

#     print(f"Total price: {total_price:.2f}\n")  

# sdf = sdf.update(process_message)


# if __name__ == "__main__":
#     app.run()


