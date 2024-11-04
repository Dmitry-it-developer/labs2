from flask import Blueprint, redirect, url_for, render_template, request, make_response, session

lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5')
def lab5_main():
    return render_template('lab5/lab5.html')

