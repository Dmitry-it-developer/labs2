from flask import Flask, url_for, redirect

app = Flask(__name__)

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
            </main>
            <footer>
                Кимосов Дмитрий Владимирович ФБИ - 21 3 курс 2024 год
            </footer>
            </body>
        </html>"""


@app.route('/lab1/web')
def start():
    return """<!doctype html>
        <html>
           <body>
               <h1>web-server na flask</h1>
               <a href=''/lab1/author'>author</a>
            </body>
        </html>""", 200, {'X-Server':'sample','Content-Type': 'text/plain; charset=utf-8'}


@app.route('/lab1/author')
def author():
    name = 'Кимосов Дмитрий Владимирович'
    group = 'ФБИ-21'
    faculty = 'ФБ'

    return f"""<!doctype html> 
        <html>
           <body>
               <p>Студент: {name}</p>
               <p>Группа: {group}</p>
               <p>Факультет: {faculty}</p>
               <a href='/lab1/web'>web</a>
            </body>
        </html>"""


@app.route('/lab1/oak')
def oak():
    path = url_for('static', filename='oak.jpg')

    return f"""<!doctype html> 
        <html>
            <head>
            <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
            </head>
           <body>
               <h1>Дуб</h1>
               <img src="{path}">
            </body>
        </html>"""


count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    
    return f"""<!doctype html> 
        <html>
           <body>
               Сколько раз вы сюда заходили: {count}
               <a href='/lab1/clearCounter'>Очистка счетчика</a>
            </body>
        </html>"""


@app.route('/lab1/info')
def info():
    return redirect('/lab1/author')


@app.route('/lab1/created') 
def created():
    return  f"""<!doctype html> 
        <html>
           <body>
               <h1>Создано успешно</h1>
               <div><i>что-то создано...</i></div>
            </body>
        </html>""", 201


@app.route('/lab1/clearCounter')
def clearCounter():
    global count
    count = 0
    return f"""<!doctype html> 
        <html>
           <body>
               <h1>Очищено успешно</h1>
            </body>
        </html>"""


@app.errorhandler(404)
def not_found(err):
    return 'нет такой страницы', 404