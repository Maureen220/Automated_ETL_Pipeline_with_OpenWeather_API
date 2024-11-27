import psycopg2

from google.cloud import secretmanager


def get_secret(secret_name):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/weather-data-439820/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(name=name)
    secret = response.payload.data.decode("UTF-8")
    return secret


postgresql_pwd = get_secret("db_password")


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
