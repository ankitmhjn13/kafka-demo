from kafka import KafkaConsumer


consumer = KafkaConsumer('demo')

for msg in consumer:
    print(f"event value is: {msg.value}")
    print(f"partition is: {msg.partition}")
    print(f"offset is: {msg.offset}")
    print(f"headers is: {msg.headers}")
    print("\n\n\n\n")