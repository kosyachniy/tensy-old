from flask import render_template, session
from app import app, LINK, get_preview

from requests import post
from json import loads

@app.route('/experts')
def experts():
	categories = loads(post(LINK, json={'method': 'categories.gets'}).text)
	user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text) if 'id' in session else {'id': 0, 'admin': 2}

	return render_template('experts.html',
		title = 'Experts',
		description = 'Top users, experts',
		tags = ['Top users', 'experts'],
		url = 'experts',
		categories = categories,
		user = user,
		preview = get_preview,

		experts = loads(post(LINK, json={'method': 'experts.gets'}).text),
	)