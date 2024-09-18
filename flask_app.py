from flask import Flask, request

app = Flask('OpenWeather_API')


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
