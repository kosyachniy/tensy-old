from flask import render_template, session
from app import app, LINK, get_preview

from requests import post
from json import loads

@app.route('/', methods=['GET'])
@app.route('/index')
@app.route('/index/')
def index():
	return render_template('index.html',
		title = 'Main',
		description = '',
		tags = ['main page', 'ladders', 'experts'],
		url = 'index',

		#categories = loads(post(LINK, json={'method': 'categories.gets'}).text),
		user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text)['user'] if 'id' in session else {'id': 0, 'admin': 2},

		preview = get_preview,

		ladders = loads(post(LINK, json={'method': 'ladders.gets'}).text)['ladders'],
		#questions = loads(post(LINK, json={'method': 'questions.gets'}).text),
		experts = loads(post(LINK, json={'method': 'experts.gets'}).text)['users'],
		#news = None,
	)