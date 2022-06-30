from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers="localhost:9092")

for i in range(0,1000):
    message = f"hello_{i}".encode()
    print(message)
    producer.send(topic="demo", value=message)

print("exit")