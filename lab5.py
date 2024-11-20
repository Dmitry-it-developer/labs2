from flask import Blueprint, redirect, url_for, render_template, request, make_response, session
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5')
def lab5_main():
    return render_template('lab5/lab5.html', login=session.get('login'))

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
    
    conn, cur = db_connect()

    cur.execute(f"SELECT login FROM users WHERE login='{login}';")
    if cur.fetchone():
        db_close(conn, cur)
        return render_template('lab5/register.html', error='Такой пользователь уже суещствует')

    password_hash = generate_password_hash(password)
    cur.execute(f"INSERT INTO users (login, password) VALUES ('{login}', '{password_hash}');")
    db_close(conn,cur)
    return render_template('lab5/success.html', login=login)

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def lab5_login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    errors = {}
    login = request.form.get('login')
    password = request.form.get('password')

    if login == '' or password == '':
        if login == '':
            errors['login'] = 'Введите значение!'
        if password == '':
            errors['password'] = 'Введите значение!'
        return render_template('lab5/login.html', errors=errors)

    conn, cur = db_connect()

    cur.execute(f"SELECT * FROM users WHERE login='{login}'")
    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return render_template('lab5/login.html', error='Пользователь не найден', login=login, password=password)
    
    if not check_password_hash(user['password'], password):
        db_close(conn, cur)
        return render_template('lab5/login.html', error='Пароль неверный',login=login)

    session['login'] = login
    db_close(conn, cur)
    return render_template('lab5/login.html', login=login, authorized=True)
   
@lab5.route('/lab5/create', methods=['GET', 'POST'])
def lab5_create():
    if not session:
        return redirect('/lab5/login')
    if request.method == 'GET':
        return render_template('lab5/create.html')   
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')

    conn, cur = db_connect()

    cur.execute(f"SELECT * FROM users WHERE login='{session.get('login')}'")
    login_id = cur.fetchone()["id"]

    cur.execute(f"INSERT INTO articles(user_id, title, article_text) VALUES ({login_id}, '{title}', '{article_text}');")
    
    db_close(conn, cur)

    return redirect('/lab5')


@lab5.route('/lab5/list')
def lab5_list():
    if not session:
        return redirect('/lab5/login')
    
    conn, cur = db_connect()

    cur.execute(f"SELECT * FROM users WHERE login='{session.get('login')}'")
    user_id = cur.fetchone()['id']

    cur.execute(f"SELECT * FROM articles WHERE user_id='{user_id}'")
    articles = cur.fetchall()

    db_close(conn, cur)

    return render_template('/lab5/articles.html', articles=articles)


def db_connect():
    conn = psycopg2.connect(host='127.0.0.1', database='web', user='postgres', password='667')

    cur = conn.cursor(cursor_factory=RealDictCursor)

    return  conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()
