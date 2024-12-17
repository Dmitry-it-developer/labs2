from flask import Blueprint, redirect, url_for, render_template, request, make_response, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path
lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7')
def lab7_main():
    return render_template('lab7/lab7.html', login=session.get('login'))

films = [
    {
        "title": "Interstellar",
        "title_ru": "Интерстеллар",
        "year": 2014,
        "description": "Когда засуха, пыльные бури и вымирание растений приводят человечество к продовольственному кризису, коллектив исследователей и учёных отправляется сквозь червоточину (которая предположительно соединяет области пространства-времени через большое расстояние) в путешествие, чтобы превзойти прежние ограничения для космических путешествий человека и найти планету с подходящими для человечества условиями."
    },
    {
        "title": "The Shawshank Redemption",
        "title_ru": "Побег из Шоушенка",
        "year": 1994,
        "description": "Бухгалтер Энди Дюфрейн обвинён в убийстве собственной жены и её любовника. Оказавшись в тюрьме под названием Шоушенк, он сталкивается с жестокостью и беззаконием, царящими по обе стороны решётки. Каждый, кто попадает в эти стены, становится их рабом до конца жизни. Но Энди, обладающий живым умом и доброй душой, находит подход как к заключённым, так и к охранникам, добиваясь их особого к себе расположения."
    },
    {
        "title": "Inception",
        "title_ru": "Начало",
        "year": 2010,
        "description": "Кобб – талантливый вор, лучший из лучших в опасном искусстве извлечения: он крадёт ценные секреты из глубин подсознания во время сна, когда разум наиболее уязвим. Редкие способности Кобба сделали его востребованным игроком в мире промышленного шпионажа, но они же превратили его в вечного беглеца и лишили всего, что он когда-либо любил. И вот у Кобба появляется шанс исправить ошибки. Его последнее дело может вернуть всё, но для этого ему нужно совершить невозможное – инициацию."
    },
    {
        "title": "The Dark Knight",
        "title_ru": "Тёмный рыцарь",
        "year": 2008,
        "description": "Бэтмен поднимает ставки в войне с преступностью. С помощью лейтенанта Джима Гордона и прокурора Харви Дента он намерен очистить улицы Готэма от оставшихся преступников. Сотрудничество оказывается эффективным, но вскоре они оказываются в центре хаоса, устроенного восходящим криминальным гением, известным как Джокер."
    },
    {
        "title": "Forrest Gump",
        "title_ru": "Форрест Гамп",
        "year": 1994,
        "description": "Форрест Гамп – добрый, искренний человек с ограниченными умственными способностями, но удивительно сильным духом. Он случайно становится свидетелем и участником важных событий в истории США, неизменно сохраняя оптимизм и веру в лучшее. Его история – это рассказ о любви, дружбе и чудесах, которые случаются в жизни каждого из нас."
    }
]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def lab7_films():
    return films

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def lab7_add_film():
    new_film = request.get_json()
    films.append(new_film)
    return str(len(films) - 1)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def lab7_film(id):
    if id > len(films) - 1:
        return 'Фильм не найден!', 404
    return films[id]

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def lab7_def_film(id):
    if id > len(films) - 1:
        return 'Фильм не найден!', 404
    del films[id]
    return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def lab7_put_film(id):
    if id > len(films) - 1:
        return 'Фильм не найден!', 404
    film = request.get_json()
    films[id] = film
    return films[id]