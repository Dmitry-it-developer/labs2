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

offices = []

for i in range(1,11):
    offices.append({'number':i, 'tenant':"", 'price': i*100})

@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def lab6_json_rpc_api():
    data = request.json
    id = data['id']
    login = session.get('login')
    if data['method'] == 'info':
        price = 0
        for office in offices:
            if login:
                if office['tenant'] == login:
                    price += office['price']
            else:
                price = 0
        return {
            'jsonrpc': 2.0,
            'result': offices,
            'price': price,
            'id': id
        }
    if not login:
        return {
            'jsonrpc': 2.0,
            'error': {
                'code': 1,
                'message': 'Unauthorized'
            }
        }
    if data['method'] == 'booking':
        office_number = data['params']
        for office in offices:
            if office['number'] == office_number:
                if office['tenant'] != '':
                    return {
                        'jsonrpc': 2.0,
                        'error': {
                            'code': 2,
                            'message': 'Already booked'
                        }
                    }
                office['tenant'] = login
                return {
                    'jsonrpc': 2.0,
                    'result': 'succes',
                    'id': id
                }
    elif data['method'] == 'cancellation':
        office_number = data['params']
        for office in offices:
            if office['number'] == office_number:
                if office['tenant'] == '':
                    return {
                        'jsonrpc': 2.0,
                        'error': {
                            'code': 3,
                            'message': 'There is no rent'
                        }
                    }
                elif office['tenant'] != login:
                    return {
                        'jsonrpc': 2.0,
                        'error': {
                            'code': 4,
                            'message': "Someone else's rent"
                        }
                    }
                else:
                    office['tenant'] = ''
                    return {
                    'jsonrpc': 2.0,
                    'result': 'succes',
                    'id': id
                }
    else:
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