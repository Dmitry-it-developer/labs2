from flask import Flask, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from db import db
import os
from os import path
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретныйкод')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')
app.secret_key = 'секретныйкод'

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'dmitry_kimosov_8'
    db_user = 'dmitry_kimosov_8'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, 'dmitry_kimosov_8.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

@app.route("/")
@app.route('/index')
def index():
    return  render_template('lab.html')

@app.errorhandler(404)
def not_found(err):
    path = url_for('static', filename='404-error.jpg')
    return '''<!doctype html> 
        <html>
            <head>
            <style>
            body {
                background-color: black;
                font-weight: bold;
                color: red
            }
            h1 {
                margin-left: 45%
            }
            </style>
            </head>
           <body>
               <h1>Ошибка 404</h1>
               <img src='''f"""{path}>
            </body>
        </html>""", 400

@app.errorhandler(500)
def server_err(err):
    return 'Ошибка сервера! Сервер временно не отвечает'
    
