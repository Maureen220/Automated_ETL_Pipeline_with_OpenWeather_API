from flask import Flask, request

from main import import_current_weather

app = Flask('OpenWeather_API')


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/main')
def current_weather():
    import_current_weather()
    return 'OK', 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
