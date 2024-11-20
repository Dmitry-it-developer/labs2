from flask import Blueprint, redirect, url_for, render_template, request, make_response, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path
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
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT login FROM users WHERE login=%s;", (login, ))
    else:
        cur.execute(f"SELECT login FROM users WHERE login=?;", (login, ))
    if cur.fetchone():
        db_close(conn, cur)
        return render_template('lab5/register.html', error='Такой пользователь уже суещствует')

    password_hash = generate_password_hash(password)
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"INSERT INTO users (login, password) VALUES (%s, %s);", (login, password_hash))
    else:
        cur.execute(f"INSERT INTO users (login, password) VALUES (?, ?);", (login, password_hash))
    session['login'] = login
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
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT * FROM users WHERE login=%s;", (login, ))
    else:
        cur.execute(f"SELECT * FROM users WHERE login=?;", (login, ))
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

@lab5.route('/lab5/quit')
def lab5_quit():
    session.pop('login', None)
    return redirect('/lab5')

   
@lab5.route('/lab5/create', methods=['GET', 'POST'])
def lab5_create():
    if not session:
        return redirect('/lab5/login')
    if request.method == 'GET':
        return render_template('lab5/create.html')   
    errors = {}
    login = session['login']
    title = request.form.get('title')
    article_text = request.form.get('article_text')

    if title == '' or article_text == '':
        if title == '':
            errors['title'] = 'Введите значение!'
        if article_text == '':
            errors['article_text'] = 'Введите значение!'
        return render_template('lab5/create.html', errors=errors, title=title)
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT * FROM users WHERE login=%s;", (login, ))
    else:
        cur.execute(f"SELECT * FROM users WHERE login=?;", (login, ))
    login_id = cur.fetchone()["id"]
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"INSERT INTO articles(user_id, title, article_text) VALUES (%s, %s, %s);", (login_id, title, article_text))
    else:
        cur.execute(f"INSERT INTO articles(user_id, title, article_text) VALUES (?, ?, ?);", (login_id, title, article_text))
    db_close(conn, cur)

    return redirect('/lab5')


@lab5.route('/lab5/list')
def lab5_list():
    if not session:
        return redirect('/lab5/login')
    
    conn, cur = db_connect()

    cur.execute(f"SELECT * FROM users WHERE login='{session.get('login')}'")
    user_id = cur.fetchone()['id']
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT * FROM articles WHERE user_id=%s ORDER BY id", (user_id, ))
    else: 
        cur.execute(f"SELECT * FROM articles WHERE user_id=? ORDER BY id", (user_id, ))
    articles = cur.fetchall()

    db_close(conn, cur)

    return render_template('/lab5/articles.html', articles=articles)

@lab5.route('/lab5/delete_article', methods=['GET'])
def lab5_delete_article():
    if not session:
        redirect('/lab5')
    id = request.args.get('id')
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"DELETE FROM articles WHERE id=%s", (id, ))
    else:
        cur.execute(f"DELETE FROM articles WHERE id=?", (id, ))
    db_close(conn, cur)
    return redirect('/lab5/list')

@lab5.route('/lab5/edit_article', methods=['GET', 'POST'])
def lab5_edit_article():
    if not session:
        redirect('/lab5')

    id = request.args.get('id')
    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT * FROM articles WHERE id=%s", (id, ))
    else:
        cur.execute(f"SELECT * FROM articles WHERE id=?", (id, ))

    article = cur.fetchone()
    if request.method == 'GET':
        return render_template('lab5/edit.html', article=article)

    login = session['login']
    title = request.form.get('title')
    article_text = request.form.get('article_text')

    if title == '' or article_text == '':
        if title == '':
            errors['title'] = 'Введите значение!'
        if article_text == '':
            errors['article_text'] = 'Введите значение!'
        return render_template('lab5/create.html', errors=errors, title=title)
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"UPDATE articles SET title=%s, article_text=%s WHERE id=%s;", (title, article_text, id))
    else:
        cur.execute(f"UPDATE articles SET title=?, article_text=? WHERE id=?;", (title, article_text, id))
    db_close(conn, cur)
    return redirect('/lab5/list')


def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(host='127.0.0.1', database='web', user='postgres', password='667')

        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path =  path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
    return  conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()
