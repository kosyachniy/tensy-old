from flask import render_template, session, request
from app import app, LINK

from requests import post
from json import loads

@app.route('/login')
@app.route('/login/')
def login():
	redirect = request.args.get('url')

	return render_template('login.html',
		title = 'Account',
		description = 'Sign Up / Log In',
		tags = ['Sign Up', 'Log In'],
		url = 'login?url=' + redirect,

		user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text)['user'] if 'id' in session else {'id': 0, 'admin': 2},

		without_menu = True,

		redirect = redirect,
	)