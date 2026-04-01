from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'green-trips',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
     consumer_timeout_ms=30000,  # ⏱️ หยุดเมื่อไม่มี message
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

count = 0

for message in consumer:
    data = message.value
    
    if data['trip_distance'] > 5:
        count += 1

print("Trips with distance > 5:", count)