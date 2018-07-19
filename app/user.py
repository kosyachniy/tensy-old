from flask import render_template, session
from app import app, LINK, get_preview

from requests import post
from json import loads

@app.route('/user/<int:id>')
def user(id):
	return render_template('user.html',
		title = '',
		description = '',
		tags = [],
		url = 'index',

		#categories = loads(post(LINK, json={'method': 'categories.gets'}).text),
		user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text) if 'id' in session else {'id': 0, 'admin': 2},

		preview = get_preview,

		users = loads(post(LINK, json={'method': 'users.get', 'id': id}).text),
	)