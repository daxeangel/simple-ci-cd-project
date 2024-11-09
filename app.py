from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

if __name__ == '_main_':
    print("Starting Flask app...")  # Added debug print
    app.run(debug=True)