from flask import session, request, render_template, redirect
from app import app, LINK

from requests import post
import json

@app.route('/sys_token_send', methods=['POST'])
def sys_token_send():
	x = request.form
	id = request.args.get('user')

	count = x['count'].strip()
	if not count.isdigit():
		return render_template('message.html', cont='Wrong count of tokens!')

	req = json.loads(post(LINK, json={
		'method': 'tokens.send',
		'token': session['token'],
		'count': int(),
		'user': int(id),
	}).text)

	if not req['error']:
		return redirect(LINK + 'user/' + id)
	else:
		return render_template('message.html', cont=req['message'])