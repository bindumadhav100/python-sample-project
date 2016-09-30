from flask import Flask, request, render_template, jsonify
import json
from flask_cors import CORS
from dao import UserDao

app = Flask(__name__)
CORS(app)

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

@app.route('/rest/', methods=['GET', 'POST'])
def rest_get_all():
    if request.method == 'POST':
        data = request.get_json()
        user = User(**data)
        userDao.save(user)
        return json.dumps(user.__dict__)
    else:
        return jsonify(results=userDao.get_all())
        
@app.route('/rest/<int:user_id>', methods=['GET'])
def rest_get_by_id(user_id):
    return jsonify(results=userDao.get_by_id(user_id))

app.run(port=8081)