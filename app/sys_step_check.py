from flask import session, request, render_template, redirect
from app import app, LINK

from requests import post
import json

@app.route('/sys_step_check', methods=['POST'])
def sys_step_check():
	x = request.form
	ladder = request.args.get('ladder')
	id = request.args.get('step')

	if 'token' not in session:
		return redirect(LINK + 'login?url=ladder/' + ladder + '/question/' + id)

	req = {
		'method': 'step.check',
		'token': session['token'],
		'ladder': int(ladder),
		'step': int(id),
		'answers': [int(i) for i in x if x[i] == '1'],
	}

	correct = json.loads(post(LINK, json=req).text)['correct']

	if correct:
		return redirect(LINK + 'ladder/' + ladder + '/question/' + str(int(id)+1))
	else:
		return redirect(LINK + 'ladder/' + ladder + '/study/' + id)