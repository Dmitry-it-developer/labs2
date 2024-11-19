from flask import Blueprint, redirect, url_for, render_template, request, make_response, session
import psycopg2
lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5')
def lab5_main():
    return render_template('lab5/lab5.html')

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def lab5_registe():
    if request.method == 'GET':
        return render_template('lab5/register.html')

    errors = {}
    login = request.form.get('login')
    password = request.form.get('password')

    if login == '' or password == '':
        if login == '':
            errors['login'] = 'Введите значение!'
        if password == '':
            errors['password'] = 'Введите значение!'
        return render_template('lab5/register.html', errors=errors)
    
    conn = psycopg2.connect(host='127.0.0.1', database='web', user='postgres', password='667')

    cur = conn.cursor()

    cur.execute(f"SELECT login FROM users WHERE login='{login}';")
    if cur.fetchone():
        cur.close()
        conn.close()
        return render_template('lab5/register.html', error='Такой пользователь уже суещствует')

    cur.execute(f"INSERT INTO users (login, password) VALUES ('{login}', '{password}');")
    conn.commit()
    cur.close()
    conn.close()
    return render_template('lab5/success.html', login=login)

