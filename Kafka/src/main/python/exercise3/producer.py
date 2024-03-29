from json import dumps
from confluent_kafka import Producer
import time



def read_ccloud_config(config_file):
    conf = {}
    with open(config_file) as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                conf[parameter] = value.strip()
    return conf



producer = Producer(read_ccloud_config("src\main\python\exercise3\client.properties"))


# Send 100 messages where the key is the index and the message to send is "test message - index"
# the topic name is myTopic

topic_kafka = 'whatsapp'

edad = 18

for e in range(100):
    data = {'New message - ': e*4}
    data2 = {'Nuevo mensaje entrando - ': e*2}
    data3= {'name':'Hugo', 'age': edad + e}
    data_str = dumps(data3)  # Serialize dictionary to a string
    data_bytes = data_str.encode('utf-8')  # Encode string to bytes
    key = str(e).encode('utf-8')
    producer.produce(topic=topic_kafka, value=data_bytes, key=key)  # Send bytes
    print("Sending data: {} to topic {}".format(data3, topic_kafka))
    time.sleep(3)

# After your loop where you send messages:
producer.flush()

# Optionally, you can check if there are any messages that failed to be delivered:
if producer.flush() != 0:
    print("Some messages failed to be delivered")

