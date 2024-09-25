from flask import Blueprint, redirect, url_for, render_template, request, make_response

lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab3_main():
    name = request.cookies.get('name')
    color = request.cookies.get('color')
    return render_template('lab3/lab3.html', name=name, color=color)


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