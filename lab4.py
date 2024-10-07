from flask import Blueprint, redirect, url_for, render_template, request, make_response

lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4')
def lab4_main():
    return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form/')
def lab4_div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div/', methods=['POST'])
def lab4_div():
    x = request.form.get('x')
    y = request.form.get('y')
    if x == '' or y == '':
        return render_template('lab4/div.html', x=x, y=y, error='Оба поля должны быть заполнеными!')
    elif y == '0':
        return render_template('lab4/div.html', x=x, y=y, error='На ноль делить нельзя!')
    result = int(x) / int(y) 
    return render_template('lab4/div.html', x=x, y=y, result=result)