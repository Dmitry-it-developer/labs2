from flask import Flask, url_for

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
        </html>"""

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