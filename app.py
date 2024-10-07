from flask import Flask, url_for, redirect, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)

@app.route("/")
@app.route('/index')
def index():
    return  f"""<!doctype html>
        <html>
            <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
            </head>
           <body>
           <header>
                НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
           </header>
           <main>
                <p><a href='/lab1' target="_blank">Лабораторная работа 1</a></p>
                <p><a href='/lab2' target="_blank">Лабораторная работа 2</a></p>
                <p><a href='/lab3' target="_blank">Лабораторная работа 3</a></p>
                <p><a href='/lab4' target="_blank">Лабораторная работа 4</a></p>
            </main>
            <footer>
                Кимосов Дмитрий Владимирович ФБИ - 21 3 курс 2024 год
            </footer>
            </body>
        </html>"""

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
    
