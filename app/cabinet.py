from flask import render_template, session, request, redirect
from app import app, LINK, get_preview

from requests import post
from json import loads

@app.route('/cabinet')
@app.route('/cabinet/')
def cabinet():
	categories = loads(post(LINK, json={'method': 'categories.gets'}).text)
	user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text) if 'id' in session else {'id': 0, 'admin': 2}

	x = request.args.get('url')

	if 'token' in session:
		return render_template('cabinet.html',
			title = 'Personal area',
			description = 'Personal area, settings, account, profile',
			url = x if x else 'cabinet',
			categories = categories,
			user = user,
			preview = get_preview,
		)

	else:
		return redirect(LINK + 'login?url=cabinet')