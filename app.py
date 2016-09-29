from flask import Flask, request, render_template, jsonify
import json
from dao import UserDao

app = Flask(__name__)

userDao = UserDao()

class User:
    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

@app.route('/', methods=['GET'])
def get_create_page():
    return render_template('home.html')

@app.route('/create', methods=['POST'])
def create():
    user = User(name=request.form['name'],
            city=request.form['city'],
            age=request.form['age'])
    userDao.save(user)
    return render_template('success.html', user=user)

@app.route('/rest/', methods=['GET'])
def rest_get_all():
    return jsonify(results=userDao.get_all())

@app.route('/rest/create', methods=['POST'])
def rest_create():
    data = request.get_json()
    user = User(**data)
    userDao.save(user)
    return json.dumps(user.__dict__)

app.run(port=8081)