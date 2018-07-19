from flask import render_template, session, request
from app import app, LINK

from requests import post
from json import loads

@app.route('/admin/add/ladder')
@app.route('/admin/add/ladder/')
def add_ladder():
	# id = request.args.get('i')
	# id = int(id) if id else 0

	return render_template('ladder_add.html',
		title = 'Add ladder',
		description = 'Admin panel: add lader, add course',
		tags = ['admin panel', 'add ladder', 'add course', 'create course'],
		url = 'admin/add/ladder', #?i=%d' % id,

		user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text) if 'id' in session else {'id': 0, 'admin': 2},

		#selected = id,
	)