# from quixstreams import Application

# app = Application(
#     broker_address="localhost:9092",
#     consumer_group="text-splitter",
#     auto_offset_reset="earliest",
# )

# jokes_topic = app.topic(name="jokes", value_deserializer="json")

# sdf = app.dataframe(topic=jokes_topic)

# # def print_message(message):
# #     print(message)
# # sdf.update(print_message)
# sdf.update(lambda message: print(f"Input message: {message}"))

# # transformations
# def split_words(message):
#     return [{"word": word} for word in message["joke_text"].split()]


# sdf = sdf.apply(split_words, expand=True)

# sdf["length"] = sdf["word"].apply(lambda word: len(word))

# sdf.update(lambda row: print(f"Output: {row}"))

# if __name__ == "__main__":
#     app.run()

from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="text-splitter",
    auto_offset_reset="earliest",
)

order_topic = app.topic(name="orders", value_deserializer="json")

sdf = app.dataframe(topic=order_topic)

# ✅ Transform messages correctly using `apply`
def transform_order(message):
    order = message.value  # Extract JSON order

    output = []
    output.append(f"\nCustomer name = {order['customer']}")

    total_price = 0
    for product in order["products"]:
        name = product["name"]
        price = product["price"]
        quantity = product["quantity"]
        total_price += price * quantity
        output.append(f"Product: {name:<25} Quantity: {quantity:<5} Price: {price:.2f}")

    output.append(f"Total price: {total_price:.2f}\n")

    return [{"formatted_output": "\n".join(output)}]  # Return formatted output

# ✅ Apply transformation
sdf = sdf.apply(transform_order, expand=True)

# ✅ Print the formatted output correctly
sdf.update(lambda row: print(row["formatted_output"]))

if __name__ == "__main__":
    app.run()

