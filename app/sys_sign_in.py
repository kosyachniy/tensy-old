from flask import session, request, render_template
from app import app, LINK, get_url

from requests import post
import json

@app.route('/sys_sign_in', methods=['POST'])
def signin():
	x = request.form

	if not all([i in x for i in ('login', 'pass')]):
		return render_template('message.html', cont='3')

	req = json.loads(post(LINK, json={'method': 'profile.auth', 'login': x['login'], 'pass': x['pass']}).text)

	if not req['error']:
		session['token'] = req['token']
		session['id'] = req['id']
		return get_url(request.args.get('url'))
	else:
		return render_template('message.html', cont=req['message'])