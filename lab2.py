from flask import Blueprint, redirect, url_for, render_template

lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a')
def a():
    return 'без слэша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = [{'name':'ландыш', 'price':'200'}, {'name':'ромашка', 'price':'100'}, {'name':'лилия', 'price':'240'}, {'name':'гвоздика', 'price':'70'}]

@lab2.route('/lab2/flowers/<int:flower_id>')
def lab2_flowers_flower_id(flower_id: int):
    if flower_id < len(flower_list):
        flower = flower_list[flower_id]['name']
        return render_template('flower.html', flower=flower)
    return 'Такого цветка нет', 404


@lab2.route('/lab2/flowers/')
def lab2_flowers():
    return render_template('flowers.html', flower_list=flower_list)

@lab2.route('/lab2/clear_flower/<int:flower_id>')
def lab2_clear_flower_flower_id(flower_id: int):
    global flower_list
    if flower_id < len(flower_list):
        flower_list.pop(flower_id)
        return redirect('/lab2/flowers')
    return 'Такого цветка нет', 404


@lab2.route('/lab2/clear_flowers/')
def lab2_claer_flowers():
    global flower_list
    flower_list = []
    return render_template('clear_flowers.html')


@lab2.route('/lab2/add_flower/<string:name>')
def lab2_add_flower_name(name: str):
    if name.lower() not in [f['name'] for f in flower_list]:
        flower_list.lab2end({'name': name.lower(), 'price': '0'})
        return render_template('add_flower.html', name=flower_list[-1]['name'], len_flower=len(flower_list),
         flower_list=flower_list)
    return f'{name} уже есть в списке'


@lab2.route('/lab2/add_flower/')
def lab2_add_flower():
   return 'Вы не задали имя цветка!', 400


@lab2.route('/lab2/example/')
def lab2_example():
    name, lab_number, course_number, group = 'Кимосов Дмитрий', 2, 3, 'ФБИ-21'
    fruits = [{'name': 'lab2le', 'price': 140}, 
        {'name': 'orange', 'price': 120}, 
        {'name': 'peach', 'price': 100}, 
        {'name': 'banana', 'price': 110},
        {'name': 'pinelab2le', 'price': 200}]
    return render_template('example.html', name=name, lab_number=lab_number, course_number=course_number, group=group, fruits=fruits)


@lab2.route('/lab2/')
def lab2_main():
    return render_template('lab2.html')


@lab2.route('/lab2/filters/')
def lab2_filtesr():
    phrase = 'О <b>сколько</b> <u>нам</u> <i>открытий чудных</i>...'
    return render_template('filter.html', phrase=phrase)


@lab2.route('/lab2/calc/<int:x>/<int:y>/')
def lab2_calc_x_y(x,y):
    return render_template('calc.html', x=x, y=y)


@lab2.route('/lab2/calc/')
def lab2_calc():
    return redirect('/lab2/calc/1/1')


@lab2.route('/lab2/calc/<int:x>/')
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

@lab2.route('/lab2/books/')
def lab2_books():
    return render_template('books.html', books_list=books_list)

cars_list = [{'name': 'Audi RS 6', 'img':'audi_rs_6.jpeg', 'description': 'Audi RS 6 — спортивный автомобиль выпускаемый подразделением Audi Sport GmbH'},
            {'name': 'Audi RS 7', 'img':'audi_rs_7.webp', 'description': 'Audi RS 7 — спортивный пятидверный фастбэк класса Гран Туризмо выпускаемый подразделением Audi Sport GmbH на платформе Audi A7.'},
            {'name': 'Audi TT', 'img': 'audi_tt.webp', 'description': 'Audi TT — компактное купе немецкой компании Audi. Выпускался с 1998 года до 2023 года в городе Дьёре, Венгрия.'},
            {'name': 'Audi R8', 'img': 'audi_r8.webp', 'description': 'Audi R8 - среднемоторный полноприводный спортивный автомобиль, производимый немецким автопроизводителем Audi с 2007 года.'},
            {'name': 'Audi A6', 'img': 'audi_a6.webp', 'description': 'Audi A6 — семейство спортивных автомобилей бизнес-класса, выпускающихся под маркой Audi'}]

@lab2.route('/lab2/cars/')
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