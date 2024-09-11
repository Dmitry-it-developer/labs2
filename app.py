from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route("/")
@app.route('/web')
def start():
    return """<!doctype html>
        <html>
           <body>
               <h1>web-server na flask</h1>
               <a href='/author'>author</a>
            </body>
        </html>""", 200, {'X-Server':'sample','Content-Type': 'text/plain; charset=utf-8'}

@app.route('/author')
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
               <a href='/web'>web</a>
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
            </body>
        </html>"""

@app.route('/info')
def info():
    return redirect('/author')

@app.route('/lab1/created') 
def created():
    return  f"""<!doctype html> 
        <html>
           <body>
               <h1>Создано успешно</h1>
               <div><i>что-то создано...</i></div>
            </body>
        </html>""", 201

@app.errorhandler(404)
def not_found(err):
    return 'нет такой страницы', 404