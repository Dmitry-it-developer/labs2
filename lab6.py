from flask import Blueprint, redirect, url_for, render_template, request, make_response, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path
lab6 = Blueprint('lab6', __name__)

@lab6.route('/lab6')
def lab6_main():
    return render_template('lab6/lab6.html', login=session.get('login'))


@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def lab6_json_rpc_api():
    data = request.json
    id = data['id']
    login = session.get('login')

    conn, cur = db_connect()

    
    if data['method'] == 'info':
        cur.execute(f"SELECT * FROM offices ORDER BY number")
        offices = list(cur.fetchall())
        if login:
            cur.execute(f"SELECT SUM(price) FROM offices WHERE tenant = '{login}'")
            price = cur.fetchone()['sum']
            if price == None:
                price = 0
        else:
            price = 0
        db_close(conn,cur)
        return {
            'jsonrpc': 2.0,
            'result': offices,
            'price': price,
            'id': id
        }
    if not login:
        db_close(conn,cur)
        return {
            'jsonrpc': 2.0,
            'error': {
                'code': 1,
                'message': 'Unauthorized'
            }
        }
    if data['method'] == 'booking':
        office_number = data['params']
        cur.execute(f"SELECT * FROM offices WHERE number = {office_number}")
        office = cur.fetchone()
        if office['tenant']:
            db_close(conn,cur)
            return {
                'jsonrpc': 2.0,
                'error': {
                    'code': 2,
                    'message': 'Already booked'
                    }
                }
        else:
            cur.execute(f'''UPDATE offices
                    SET tenant = '{login}'
                    WHERE number = {office_number};''')
            db_close(conn,cur)
            return {
                'jsonrpc': 2.0,
                'result': 'succes',
                'id': id
                }
    elif data['method'] == 'cancellation':
        office_number = data['params']
        cur.execute(f"SELECT * FROM offices WHERE number = {office_number}")
        office = cur.fetchone()
        if not office['tenant']:
            db_close(conn,cur)
            return {
                'jsonrpc': 2.0,
                'error': {
                    'code': 3,
                    'message': 'There is no rent'
                    }
                }
        elif office['tenant'] != login:
            db_close(conn,cur)
            return {
                'jsonrpc': 2.0,
                'error': {
                    'code': 4,
                    'message': "Someone else's rent"
                        }
                }
        else:
            cur.execute(f'''UPDATE offices
                    SET tenant = ''
                    WHERE number = {office_number};''')
            db_close(conn, cur)
            return {
                    'jsonrpc': 2.0,
                    'result': 'succes',
                    'id': id
                }
    else:
        db_close(conn,cur)
        return {
            'jsonrpc': 2.0,
            'error': {
                'code': -32601,
                'message': 'Method not found'
            }
        }

@lab6.route('/lab6/office')
def lab6_office():
    return render_template('lab6/office.html')

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