from flask import Flask

app = Flask(__name__)
from sport import sport_bp

app.register_blueprint(sport_bp)

@app.route("/")
def hello_world():
    print("hello")
    return "<p>Hello, World!</p>"


@app.route("/about")
def about():
    return "<p>This is the ABOUT PAGE</p>"

if __name__ == '__main__':
    app.run(debug=True, port=9000)