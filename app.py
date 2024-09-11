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

@app.route('/lab1')
def lab1():
    return  f"""<!doctype html>
        <html>
            <head>
            <title>Лабораторная 1</title>
            </head>
           <body>
           <header>
                НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
           </header>
           <main>
                <p>Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов 
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности. <a href='/'>Главное меню</a></p>

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

@app.route('/lab1/400')
def lab1_400():
    return f"""<!doctype html> 
        <html>
           <body>
               <h1>Ошибка 400</h1>
            </body>
        </html>""", 400

@app.route('/lab1/401')
def lab1_401():
    return f"""<!doctype html> 
        <html>
           <body>
               <h1>Ошибка 401</h1>
            </body>
        </html>""", 401


@app.route('/lab1/402')
def lab1_402():
    return f"""<!doctype html> 
        <html>
           <body>
               <h1>Ошибка 402</h1>
            </body>
        </html>""", 402


@app.route('/lab1/403')
def lab1_403():
    return f"""<!doctype html> 
        <html>
           <body>
               <h1>Ошибка 403</h1>
            </body>
        </html>""", 403


@app.route('/lab1/405')
def lab1_405():
    return f"""<!doctype html> 
        <html>
           <body>
               <h1>Ошибка 405</h1>
            </body>
        </html>""", 405