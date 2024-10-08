from flask import Flask, url_for, redirect, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)

app.secret_key = 'secret'
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
    
