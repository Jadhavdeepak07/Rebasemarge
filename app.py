from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from Python!</h1>
    <p>This Flask application is running successfully.</p>
    """

if __name__ == "__main__":
    app.run(host="10.10.1.1", port=5000)
