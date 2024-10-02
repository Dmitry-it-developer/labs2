from flask import Blueprint, redirect, url_for, render_template, request, make_response

lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab3_main():
    name = request.cookies.get('name')
    color = request.cookies.get('color')
    age = request.cookies.get('age')
    return render_template('lab3/lab3.html', name=name, color=color, age=age)


@lab3.route('/lab3/cookie')
def lab3_cookie():
    resp = make_response(redirect('/lab3'))
    resp.set_cookie('name', 'Dmitry', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('color', 'black')
    return resp

@lab3.route('/lab3/del_cookie')
def lab3_del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('color')
    resp.delete_cookie('color_t')
    resp.delete_cookie('color_b')
    resp.delete_cookie('font_s')
    return resp


@lab3.route('/lab3/form1')
def lab3_form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def lab3_order():
    return render_template('lab3/order.html')


for_order = {'cofee': 120, 'black-tea': 80, 'green-tea': 70}
@lab3.route('/lab3/pay')
def lab3_pay():
    drink = request.args.get('drink')
    price = 0
    price += for_order[drink]

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    resp = make_response(render_template('lab3/pay.html', price=price))
    resp.set_cookie('last_order', str(price))
    return resp

@lab3.route('/lab3/success')
def lab3_succes():
    price = request.cookies.get('last_order')
    return render_template('lab3/success.html', price=price)

@lab3.route('/lab3/settings/')
def lab3_settings():
    color_t = request.args.get('color_t')
    color_b = request.args.get('color_b')
    font_s = request.args.get('font_s')
    if color_t:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('color_t', color_t)
        resp.set_cookie('color_b', color_b)
        resp.set_cookie('font_s', font_s)
        return resp
    color_t = request.cookies.get('color_t')
    color_b = request.cookies.get('color_b')
    font_s = request.cookies.get('font_s')
    resp = make_response(render_template('lab3/settings.html', color_t=color_t, color_b=color_b, font_s=font_s))
    return resp

@lab3.route('/lab3/order2/')
def lab3_order2():
    errors = {}
    full_name = request.args.get('full_name')
    age = request.args.get('age')
    place = request.args.get('place')
    clothes = request.args.get('clothes')
    bag = request.args.get('bag')
    insurance = request.args.get('insurance')
    start = request.args.get('start')
    end = request.args.get('end')
    date_travel = request.args.get('date_travel')

    for i in ['full_name', 'age', 'start', 'end', 'date_travel']:
        if locals()[i] == '':
            errors[i] = 'Заполните поле!'
    if str(age) != 'None':
        if int(age) < 1 or int(age) > 120:
            errors['age'] = 'Возраст должен быть от 1 до 120'
    if len(errors) != 0 or len(request.args) == 0:
        resp = make_response(render_template('lab3/order2.html', full_name=full_name, age=age, start=start, 
        end=end, date_travel=date_travel, errors=errors))
    else:
        price = make_price(age, place, clothes, bag,insurance)
        if str(age) != 'None':
            age_type = 'детский' if int(age) < 18 else 'взрослый'
        else:
            age_type = 'взрослый'
        resp = make_response(render_template('lab3/ticket.html', full_name=full_name, start=start, end=end, 
        date_travel=date_travel, age_type=age_type, price=price))

    return resp

def make_price(age:str, place:str, clothes:str, bag:str, insurance:str) -> int:
    price = 0
    if str(age) != 'None':
        if int(age) < 18:
            price += 700
    else:
        price += 1000
    if place in ['lower', 'lower_side']:
        price += 100
    if clothes == 'on':
        price += 75
    if bag == 'on':
        price += 250
    if insurance == 'on':
        price += 150
    return price

phones = [{'name': 'Iphone 1', 'price': '100', 'color': 'Белый'},
    {'name': 'Iphone 2', 'price': '200', 'color': 'Черный'},
    {'name': 'Iphone 3', 'price': '300', 'color': 'Белый'},
    {'name': 'Iphone 4', 'price': '400', 'color': 'Черный'},
    {'name': 'Iphone 5', 'price': '500', 'color': 'Белый'},
    {'name': 'Iphone 6', 'price': '600', 'color': 'Черный'},
    {'name': 'Iphone 7', 'price': '700', 'color': 'Белый'},
    {'name': 'Iphone 8', 'price': '800', 'color': 'Черный'},
    {'name': 'Iphone 9', 'price': '900', 'color': 'Белый'},
    {'name': 'Iphone 10', 'price': '1000', 'color': 'Черный'},
    {'name': 'Iphone 11', 'price': '1100', 'color': 'Белый'},
    {'name': 'Iphone 12', 'price': '1200', 'color': 'Черный'},
    {'name': 'Iphone 13', 'price': '1300', 'color': 'Белый'},
    {'name': 'Iphone 14', 'price': '1400', 'color': 'Черный'},
    {'name': 'Iphone 15', 'price': '1500', 'color': 'Белый'},
    {'name': 'Iphone 16', 'price': '1600', 'color': 'Черный'},
    {'name': 'Iphone 17', 'price': '1700', 'color': 'Белый'},
    {'name': 'Iphone 18', 'price': '1800', 'color': 'Черный'},
    {'name': 'Iphone 19', 'price': '1900', 'color': 'Белый'},
    {'name': 'Iphone 20', 'price': '2000', 'color': 'Черный'}]

@lab3.route('/lab3/iphone')
def lab3_iphone():
    errors = {}
    start_p = request.args.get('start_p')
    end_p = request.args.get('end_p')
    phones_filter = []
    if len(request.args) > 0:
        if start_p == '':
            errors['start_p'] = 'Введите значени!'
        elif int(start_p) < 0:
            errors['start_p'] = 'Введите цену начиная от 0 руб.'

        if  end_p == '':
            errors['end_p'] = 'Введите значени!'
        elif int(end_p) < int(start_p):
            errors['end_p'] = 'Введите конечную цену больше начальной.'
        if len(errors) == 0:
            phones_filter = filter_phones(start_p, end_p)
            print(phones_filter)
    resp = make_response(render_template('lab3/iphone.html', start_p=start_p, end_p=end_p, errors=errors, phones_filter=phones_filter))
    return resp

def filter_phones(start_p:str, end_p:str) -> list:
    result = []
    for phone in phones:
        if float(start_p) <= float(phone['price']) <= float(end_p):
            result.append(phone)
    return result