'''
Main file de l'aplication
'''
import csv
from flask import Flask, request, render_template, redirect, url_for
from flask_ipban import IpBan

APP_FLASK = Flask(__name__)
ip_ban = IpBan(ban_seconds=59)
ip_ban.init_app(APP_FLASK)

@APP_FLASK.after_request
def add_header(response):
    '''
    Ajouter de l'header
    '''
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'max-age=300'
    if 'Access-Control-Allow-Origin' not in response.headers:
        response.headers['Access-Control-Allow-Origin'] = 'Sofiane77.eu.pythonanywhere.com'
    return response


@APP_FLASK.route('/')
def home():
    '''
    Function de la route index
    '''
    return 'Bienvenue !'


@APP_FLASK.route('/gaz', methods=['GET', 'POST'])
def save_gazouille():
    '''
    Function de la route gaz
    '''
    if request.method == 'POST':
        if len(request.form['user-text']) < 281 and request.form['user-text'].count('barre') == 0:
            dump_to_csv(request.form)
        return redirect(url_for('timeline'))
        # return "OK"
    if request.method == 'GET':
        return render_template('formulaire.html')
    return None


@APP_FLASK.route('/timeline', defaults={'user': None}, methods=['GET'])
@APP_FLASK.route('/timeline/<user>/', methods=['GET'])
def timeline(user):
    '''
    Function de la route timeline
    '''
    gaz = parse_from_csv(user)
    return render_template("timeline.html", gaz=gaz)


def parse_from_csv(user):
    '''
    Récuperer les utlisateurs et les tweet
    '''
    gaz = []
    with open('./gazouilles.csv', 'r') as file_csv:
        reader = csv.reader(file_csv)
        for row in reader:
            if len(row[1]) < 281:
                if(user is not None):
                    if (row[0] == user):
                        gaz.append({"user": row[0], "text": row[1]})
                else:
                    gaz.append({"user": row[0], "text": row[1]})
    return gaz


def dump_to_csv(data_form):
    '''
    Enregistre les data dans le csv
    '''
    donnees = [data_form["user-name"], data_form["user-text"]]
    with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(donnees)
