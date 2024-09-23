from kafka import KafkaConsumer
import json
import psycopg2
from config import postgresql_pwd


def upload_to_db():
    # KafkaConsumer
    consumer = KafkaConsumer(
        'weather-data',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',  # Start from the earliest message
        enable_auto_commit=True,  # Automatically commit offsets
        group_id='weather-consumer'  # Consumer group ID
    )

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="city_comparison",
        user="postgres",
        password=f"{postgresql_pwd}",
        host="localhost"
    )
    cur = conn.cursor()

    # Kafka to PostgreSQL
    for message in consumer:
        weather_data = json.loads(message.value.decode('utf-8'))
        print(f"Received data: {weather_data}")

        # Insert to PostgreSQL
        query = """INSERT INTO weather (datetime, city, temp, humidity, pressure) VALUES (%s, %s, %s, %s, %s)"""
        values = (
            weather_data['datetime'],
            weather_data['city'],
            weather_data['temp'],
            weather_data['humidity'],
            weather_data['pressure'])
        cur.execute(query, values)

        # Commit
        conn.commit()

    # Close
    cur.close()
    conn.close()
