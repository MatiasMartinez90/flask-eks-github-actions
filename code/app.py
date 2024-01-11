from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Holy</h2>'

if __name__ == "__main__":
    app.run(debug=True)
