from flask import Blueprint, redirect, url_for, render_template, request, make_response, session, current_app, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path
lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8')
def lab8_main():
    return render_template('lab7/lab7.html', login=session.get('login'))
