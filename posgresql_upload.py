import psycopg2

from config import postgresql_pwd


def upload_to_db(weather_data):
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="city_comparison",
        user="postgres",
        password=f"{postgresql_pwd}",
        host="localhost"
    )
    cur = conn.cursor()

    # Insert to PostgreSQL
    for data in weather_data:
        query = """INSERT INTO denver_and_slc_comparison 
                    (datetime, city, temp, humidity, pressure) VALUES (%s, %s, %s, %s, %s)"""
        values = (
            data['datetime'],
            data['city'],
            data['temp'],
            data['humidity'],
            data['pressure'])
        cur.execute(query, values)

        # Commit
        conn.commit()

    # Close
    cur.close()
    conn.close()
