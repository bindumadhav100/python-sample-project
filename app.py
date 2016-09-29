from flask import Flask,request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_all():
    return 'Hello, World!'

@app.route('/create', methods=['POST'])
def create():
    return 'Hello, World!'

app.run(port=8081)