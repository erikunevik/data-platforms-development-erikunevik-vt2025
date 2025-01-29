from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application

data_path = Path(__file__).parents[1] / "data"
#print(data_path)


# Read in jokes.json through its absolute path
with open(data_path / "jokes.json", "r") as file:
        jokes = json.load(file) # Converts the json file to python format
        
# pprint(jokes)

# Communicates with the broker, broker_address är servern. A form of entry poitn for interacting with kafka. 
# Local host 90:92. text-splitter that we communicate with. 
app = Application(broker_address="localhost:9092", consumer_group="text-splitter")
                  
#print(app)

jokes_topic = app.topic(name = "jokes", value_serializer="json")

#print(jokes_topic)

# skapa kod

def main():
    with app.get_producer() as producer:
            
       
                
        for joke in jokes:
            kafka_msg = jokes_topic.serialize(key=joke["joke_id"], value = joke)
            print(f" Produced message: key = {kafka_msg.key, kafka_msg.value}")
                        
            producer.produce(topic="jokes", key=str(kafka_msg.key), value=kafka_msg.value) # Sends serialized message to kafka topic jokes
# Run this script only when executing this script and when importing this module
if __name__ == '__main__':
        main()
