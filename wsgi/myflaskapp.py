import os, sqlite3
from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='static', static_url_path='')

def queryDB():
	conn = sqlite3.connect("homecare")
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM exame ORDER BY id DESC LIMIT 1")	
	return cursor.fetchall()

@app.route('/')
def index():
	query = queryDB()
	return render_template('index.html', 
				pressure = query[0][1],
				hz = query[0][2],
				oximetry = query[0][3],
				glico = query[0][4] )

app.run(debug = True)
