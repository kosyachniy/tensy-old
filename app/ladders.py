from flask import render_template, session
from app import app, LINK, get_preview

from requests import post
from json import loads

@app.route('/ladder')
@app.route('/ladder/')
@app.route('/ladders')
@app.route('/ladders/')
@app.route('/ladders/<sub>')
def ladders(sub=''):
	title = 'Ladders' #change with category
	tags = ['ladders', 'courses']

	return render_template('ladders.html',
		title = title,
		description = '',
		tags = tags,
		url = 'ladders/' + sub,

		#categories = loads(post(LINK, json={'method': 'categories.gets'}).text),
		user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text)['user'] if 'id' in session else {'id': 0, 'admin': 2},

		preview = get_preview,

		ladders = loads(post(LINK, json={'method': 'ladders.gets'}).text)['ladders'] #, 'category': subcategory if subcategory else category}).text),
	)