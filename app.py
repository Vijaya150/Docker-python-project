from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>Sample Python Web App</title></head>
    <body>
        <h1>Hello from Flask!</h1>
        <p>This is a simple one-file Python web application.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
