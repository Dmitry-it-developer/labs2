from flask import Flask, url_for, redirect, render_template

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
                <p><a href='/lab2' target="_blank">Лабораторная работа 2</a></p>
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
                <h2>Список роутов</h2>
                <ul>
                    <li><a href="/lab1/web">Web</a></li>
                    <li><a href="/lab1/author">author</a></li>
                    <li><a href="/lab1/oak">oak</a></li>
                    <li><a href="/lab1/counter">counter</a></li>
                    <li><a href="/lab1/created">created</a></li>
                    <li><a href="/lab1/delete">delete</a></li>
                    <li><a href="/lab1/resource_info">resource</a></li>
                    <li><a href="/lab1/info">info</a></li>
                    <li><a href="/lab1/clearCounter">clearCounter</a></li>
                    <li><a href="/lab1/400">400</a></li>
                    <li><a href="/lab1/401">401</a></li>
                    <li><a href="/lab1/402">402</a></li>
                    <li><a href="/lab1/403">403</a></li>
                    <li><a href="/lab1/405">405</a></li>
                    <li><a href="/lab1/500">500</a></li>
                    <li><a href="/lab1/my">my</a></li>
                </ul>

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

resource = 'Я не создан'

@app.route('/lab1/created') 
def created():
    global resource
    if resource == 'Я создан':
        return 'Отказано: ресурс уже создан', 400
    resource = 'Я создан'
    return  f"""<!doctype html> 
        <html>
           <body>
               <h1>Создано успешно</h1>
            </body>
        </html>""", 201

@app.route('/lab1/delete') 
def delete():
    global resource
    if resource != 'Я создан':
        return 'Отказано: ресурс еще не существует', 400
    resource = 'Я не создан'
    return  f"""<!doctype html> 
        <html>
           <body>
               <h1>Удалено успешно</h1>
            </body>
        </html>""", 200

@app.route('/lab1/resource_info') 
def resource_info():
    global resource
    return  f"""<!doctype html> 
        <html>
           <body>
               <h1>{resource}</h1><br>
               <a href='/lab1/created'>Создать</a><br>
               <a href='/lab1/delete'>Удалить</a>
            </body>
        </html>""", 200


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

@app.route('/lab1/500')
def lab1_500():
    return 200/0

@app.errorhandler(500)
def server_err(err):
    return 'Ошибка сервера! Сервер временно не отвечает'

@app.route('/lab1/my')
def my():
    return f"""<!doctype html> 
        <html>
           <body>
               <h1>Собственный роут</h1>
               <p>Дорогие друзья, дальнейшее развитие различных форм деятельности способствует повышению актуальности 
               системы обучения кадров, соответствующей насущным потребностям! Повседневная практика показывает, 
               что постоянное информационно-техническое обеспечение нашей деятельности влечет за собой процесс внедрения и 
               модернизации форм воздействия. Не следует, однако, забывать о том, что начало повседневной работы по формированию 
               позиции в значительной степени обуславливает создание соответствующих условий активизации!<br>
               <img src="{url_for('static', filename='oak.jpg')}">
            </body>
        </html>""", 200, {'Content-Language': 'ru-Ru', 'X-api-key': '312fdse2drf2csaDAaw', 'X-more': 'more information'}
    

@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = [{'name':'ландыш', 'price':'200'}, {'name':'ромашка', 'price':'100'}, {'name':'лилия', 'price':'240'}, {'name':'гвоздика', 'price':'70'}]

@app.route('/lab2/flowers/<int:flower_id>')
def lab2_flowers_flower_id(flower_id: int):
    if flower_id < len(flower_list):
        flower = flower_list[flower_id]['name']
        return render_template('flower.html', flower=flower)
    return 'Такого цветка нет', 404

@app.route('/lab2/flowers/')
def lab2_flowers():
    return render_template('flowers.html', flower_list=flower_list)

@app.route('/lab2/clear_flower/<int:flower_id>')
def lab2_clear_flower_flower_id(flower_id: int):
    global flower_list
    if flower_id < len(flower_list):
        flower_list.pop(flower_id)
        return redirect('/lab2/flowers')
    return 'Такого цветка нет', 404

@app.route('/lab2/clear_flowers/')
def lab2_claer_flowers():
    global flower_list
    flower_list = []
    return render_template('clear_flowers.html')

@app.route('/lab2/add_flower/<string:name>')
def lab2_add_flower_name(name: str):
    if name.lower() not in [f['name'] for f in flower_list]:
        flower_list.append({'name': name.lower(), 'price': '0'})
        return render_template('add_flower.html', name=flower_list[-1]['name'], len_flower=len(flower_list),
         flower_list=flower_list)
    return f'{name} уже есть в списке'

@app.route('/lab2/add_flower/')
def lab2_add_flower():
   return 'Вы не задали имя цветка!', 400

@app.route('/lab2/example/')
def lab2_example():
    name, lab_number, course_number, group = 'Кимосов Дмитрий', 2, 3, 'ФБИ-21'
    fruits = [{'name': 'apple', 'price': 140}, 
        {'name': 'orange', 'price': 120}, 
        {'name': 'peach', 'price': 100}, 
        {'name': 'banana', 'price': 110},
        {'name': 'pineapple', 'price': 200}]
    return render_template('example.html', name=name, lab_number=lab_number, course_number=course_number, group=group, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters/')
def lab2_filtesr():
    phrase = 'О <b>сколько</b> <u>нам</u> <i>открытий чудных</i>...'
    return render_template('filter.html', phrase=phrase)

@app.route('/lab2/calc/<int:x>/<int:y>/')
def lab2_calc_x_y(x,y):
    return render_template('calc.html', x=x, y=y)

@app.route('/lab2/calc/')
def lab2_calc():
    return redirect('/lab2/calc/1/1')

@app.route('/lab2/calc/<int:x>/')
def lab2_calc_x(x):
    return redirect(f'/lab2/calc/{x}/1')

books_list = [{'author': 'Автор1', 'title': 'Название1', 'genre': 'Роман', 'pages': '324'},
            {'author': 'Автор2', 'title': 'Название2', 'genre': 'Поэзия', 'pages': '234'},
            {'author': 'Автор3', 'title': 'Название3', 'genre': 'Ужасы', 'pages': '123'},
            {'author': 'Автор4', 'title': 'Название4', 'genre': 'Фантастика', 'pages': '321'},
            {'author': 'Автор5', 'title': 'Название5', 'genre': 'Детектив', 'pages': '231'},
            {'author': 'Автор6', 'title': 'Название6', 'genre': 'Фентази', 'pages': '423'},
            {'author': 'Автор7', 'title': 'Название7', 'genre': 'Роман', 'pages': '512'},
            {'author': 'Автор8', 'title': 'Название8', 'genre': 'Фантастика', 'pages': '125'},
            {'author': 'Автор9', 'title': 'Название9', 'genre': 'Поэзия', 'pages': '194'},
            {'author': 'Автор10', 'title': 'Название10', 'genre': 'Ужасы', 'pages': '329'}]

@app.route('/lab2/books/')
def lab2_books():
    return render_template('books.html', books_list=books_list)

cars_list = [{'name': 'Audi RS 6', 'img':'audi_rs_6.jpeg', 'description': 'Audi RS 6 — спортивный автомобиль выпускаемый подразделением Audi Sport GmbH'},
            {'name': 'Audi RS 7', 'img':'audi_rs_7.webp', 'description': 'Audi RS 7 — спортивный пятидверный фастбэк класса Гран Туризмо выпускаемый подразделением Audi Sport GmbH на платформе Audi A7.'},
            {'name': 'Audi TT', 'img': 'audi_tt.webp', 'description': 'Audi TT — компактное купе немецкой компании Audi. Выпускался с 1998 года до 2023 года в городе Дьёре, Венгрия.'},
            {'name': 'Audi R8', 'img': 'audi_r8.webp', 'description': 'Audi R8 - среднемоторный полноприводный спортивный автомобиль, производимый немецким автопроизводителем Audi с 2007 года.'},
            {'name': 'Audi A6', 'img': 'audi_a6.webp', 'description': 'Audi A6 — семейство спортивных автомобилей бизнес-класса, выпускающихся под маркой Audi'}]

@app.route('/lab2/cars/')
def lab2_cars():
    cars_text = ''
    for car in cars_list:
        cars_text += f'<b>{car['name']}</b>.<br> {car['description']} <br> <img width="300px" src="{url_for('static', filename=car['img'])}"><br>'
    html_content =  f"""<!doctype html> 
        <html>
            <head>
            </head>
           <body>
               {cars_text}
            </body>
        </html>"""
    return html_content