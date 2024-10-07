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

@lab4.route('/lab4/sum-form/')
def lab4_sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/sum/', methods=['POST'])
def lab4_sum():
    x = request.form.get('x')
    x = int(x) if x != '' else 0
    y = request.form.get('y')
    y = int(y) if y != '' else 0
    result = x + y 
    return render_template('lab4/sum.html', x=x, y=y, result=result)

@lab4.route('/lab4/mult-form/')
def lab4_mult_form():
    return render_template('lab4/mult-form.html')

@lab4.route('/lab4/mult/', methods=['POST'])
def lab4_mult():
    x = request.form.get('x')
    x = int(x) if x != '' else 1
    y = request.form.get('y')
    y = int(y) if y != '' else 1
    result = x * y 
    return render_template('lab4/mult.html', x=x, y=y, result=result)

@lab4.route('/lab4/sub-form/')
def lab4_sub_form():
    return render_template('lab4/sub-form.html')

@lab4.route('/lab4/sub/', methods=['POST'])
def lab4_sub():
    x = request.form.get('x')
    y = request.form.get('y')
    if x == '' or y == '':
        return render_template('lab4/sub.html', x=x, y=y, error='Оба поля должны быть заполнеными!')
    result = int(x) - int(y)
    return render_template('lab4/sub.html', x=x, y=y, result=result)

@lab4.route('/lab4/degree-form/')
def lab4_degeree_form():
    return render_template('lab4/degree-form.html')

@lab4.route('/lab4/degree/', methods=['POST'])
def lab4_degree():
    x = request.form.get('x')
    y = request.form.get('y')
    if x == '' or y == '':
        return render_template('lab4/degree.html', x=x, y=y, error='Оба поля должны быть заполнеными!')
    if x == '0' or y == '0':
        return render_template('lab4/degree.html', x=x, y=y, error='Оба поля должны быть не равны 0!')
    result = int(x) ** int(y) 
    return render_template('lab4/degree.html', x=x, y=y, result=result)


tree_count = 0

@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def lab4_tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    operation = request.form.get('operation')

    if operation == 'plant':
        tree_count += 1
    elif tree_count > 0:
        tree_count -= 1
    else:
        return render_template('lab4/tree.html', tree_count=tree_count, error='Невозможно срубить!')
    return render_template('lab4/tree.html', tree_count=tree_count)