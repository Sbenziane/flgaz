from flask import Flask, request, render_template, redirect, url_for
import csv

app = Flask(__name__)

@app.after_request
def add_header(response):
	if 'Cache-Control' not in response.headers:
		response.headers['Cache-Control'] = 'max-age=300'
	if 'Access-Control-Allow-Origin' not in response.headers:
		response.headers['Access-Control-Allow-Origin'] = 'Sofiane77.eu.pythonanywhere.com'
	return response

@app.route('/')
def home():
    return 'Bienvenue !'

@app.route('/gaz', methods=['GET','POST'])
def save_gazouille():
	if request.method == 'POST':
		if (280 > len(request.form['user-text'])):
			dump_to_csv(request.form)
		return redirect(url_for('timeline'))
		#return "OK"
	if request.method == 'GET':
		return render_template('formulaire.html')

@app.route('/timeline', defaults={'user': None}, methods=['GET'])
@app.route('/timeline/<user>/', methods=['GET'])
def timeline(user):
	gaz = parse_from_csv(user)
	return render_template("timeline.html", gaz = gaz)

def parse_from_csv(user):
	gaz = []
	with open('./gazouilles.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			if (280 > len(row[1])):
				if(user != None):
					if (row[0] == user):
						gaz.append({"user":row[0], "text":row[1]})
				else:
					gaz.append({"user":row[0], "text":row[1]})
	return gaz

def dump_to_csv(d):
	donnees = [d["user-name"],d["user-text"] ]
	with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow(donnees)