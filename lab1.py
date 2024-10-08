from flask import Blueprint, redirect, url_for, render_template

lab1 = Blueprint('lab1', __name__)


@lab1.route('/lab1')
def lab1_main():
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
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности. <br>
                <a href='/'>Главное меню</a></p>
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


@lab1.route('/lab1/web')
def start():
    return """<!doctype html>
        <html>
           <body>
               <h1>web-server na flask</h1>
               <a href=''/lab1/author'>author</a>
            </body>
        </html>""", 200, {'X-Server':'sample','Content-Type': 'text/plain; charset=utf-8'}


@lab1.route('/lab1/author')
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


@lab1.route('/lab1/oak')
def oak():
    path = url_for('static', filename='lab1/oak.jpg')

    return f"""<!doctype html> 
        <html>
            <head>
            <link rel="stylesheet" href="{url_for('static', filename='lab1/lab1.css')}">
            </head>
           <body>
               <h1>Дуб</h1>
               <img src="{path}">
            </body>
        </html>"""

count = 0

@lab1.route('/lab1/counter')
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


@lab1.route('/lab1/info')
def info():
    return redirect('/lab1/author')

resource = 'Я не создан'

@lab1.route('/lab1/created') 
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


@lab1.route('/lab1/delete') 
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


@lab1.route('/lab1/resource_info') 
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


@lab1.route('/lab1/clearCounter')
def clearCounter():
    global count
    count = 0
    return f"""<!doctype html> 
        <html>
           <body>
               <h1>Очищено успешно</h1>
            </body>
        </html>"""


@lab1.route('/lab1/400')
def lab1_400():
    return f"""<!doctype html> 
        <html>
           <body>
               <h1>Ошибка 400</h1>
            </body>
        </html>""", 400


@lab1.route('/lab1/401')
def lab1_401():
    return f"""<!doctype html> 
        <html>
           <body>
               <h1>Ошибка 401</h1>
            </body>
        </html>""", 401


@lab1.route('/lab1/402')
def lab1_402():
    return f"""<!doctype html> 
        <html>
           <body>
               <h1>Ошибка 402</h1>
            </body>
        </html>""", 402


@lab1.route('/lab1/403')
def lab1_403():
    return f"""<!doctype html> 
        <html>
           <body>
               <h1>Ошибка 403</h1>
            </body>
        </html>""", 403


@lab1.route('/lab1/405')
def lab1_405():
    return f"""<!doctype html> 
        <html>
           <body>
               <h1>Ошибка 405</h1>
            </body>
        </html>""", 405


@lab1.route('/lab1/500')
def lab1_500():
    return 200/0


@lab1.route('/lab1/my')
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
               <img src="{url_for('static', filename='lab1/oak.jpg')}">
            </body>
        </html>""", 200, {'Content-Language': 'ru-Ru', 'X-api-key': '312fdse2drf2csaDAaw', 'X-more': 'more information'}