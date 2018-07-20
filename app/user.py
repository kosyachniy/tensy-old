from flask import render_template, session, Markup
from app import app, LINK, get_preview

from requests import post
from json import loads
import markdown

@app.route('/user/<int:id>')
@app.route('/user/<int:id>/')
def user(id):
	users = loads(post(LINK, json={'method': 'users.get', 'id': id}).text)['user']
	users['description'] = Markup(markdown.markdown(users['description']))

	return render_template('user.html',
		title = '',
		description = '',
		tags = [],
		url = 'user/%d' % id,

		user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text)['user'] if 'id' in session else {'id': 0, 'admin': 2},

		preview = get_preview,

		users = users,
	)