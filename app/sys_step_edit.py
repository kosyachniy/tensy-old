from flask import session, request, render_template, redirect
from app import app, LINK

from requests import post
import json

@app.route('/sys_step_edit', methods=['POST'])
def sys_step_edit():
	x = request.form
	ladder = request.args.get('ladder')
	step = request.args.get('step')

	req = {
		'method': 'step.edit',
		'token': session['token'],
		'name': x['name'],
		'ladder': int(ladder),
		'step': int(step),
		'cont': x['cont'],
		'theory': x['theory'],
		'options': [i for i in x['options'].split(';') if i],
	}

	if 'answers' in x and len(x['answers']):
		req['answers'] = [int(i) for i in x['answers'].split(';') if i]

	req = json.loads(post(LINK, json=req).text)

	if not req['error']:
		return redirect(LINK + 'ladder/' + ladder + '/question/' + step)
	else:
		return render_template('message.html', cont=req['message'])