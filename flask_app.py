from flask import Flask

from main import import_current_weather
from posgresql_upload import upload_to_db

app = Flask('OpenWeather_API')


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/import_weather')
def current_weather():
    """Runs the OpenWeather API to create a table for SLC and Denver"""
    import_current_weather()
    return 'OK', 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
