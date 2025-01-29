from quixstreams import Application



app = Application(
    broker_address="localhost:9092", 
    consumer_group="text-splitter", 
    auto_offset_reset="earliest",
) # Auto_offset kör skriptet från början. Behövs ej till producerar då vi ara appendar. 


jokes_topic = app.topic(name="jokes", value_deserializer="json")
# Vi tar emot binarys och transformerar dom till json


sdf = app.dataframe(topic=jokes_topic)

#Lambda innebär: def print_message(message):
                    #print(message)
                    #sdf.update(print_message)


sdf = sdf.update(lambda message: print(f"Input: {message}")) 

sdf = sdf.apply(
    lambda message: [{"word": word} for word in message["joke_text"].split()], 
    expand=True,
    
)

sdf["length"] = sdf["word"].apply(lambda word: len(word))

sdf = sdf.update(lambda row: print(f"Otput: {row}"))



if __name__ == "__main__":
    app.run()
