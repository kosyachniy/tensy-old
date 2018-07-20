from flask import session, request, render_template, redirect
from app import app, LINK

from requests import post
import json

@app.route('/sys_step_add', methods=['POST'])
def sys_step_add():
	x = request.form
	id = request.args.get('ladder')

	req = {
		'method': 'step.add',
		'name': x['name'],
		'ladder': int(id),
		'cont': x['cont'],
		'options': x['options'].split(';'),
	}

	if 'answers' in x and len(x['answers']):
		req['answers'] = [int(i) for i in x['answers'].split(';')]

	req = json.loads(post(LINK, json=req).text)

	if not req['error']:
		return redirect(LINK + 'ladder/' + id + '/?edit=1')
	else:
		return render_template('message.html', cont=req['message'])