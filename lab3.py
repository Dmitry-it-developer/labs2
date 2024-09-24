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