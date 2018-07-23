from flask import session, request, render_template, redirect
from app import app, LINK

from requests import post
import json

@app.route('/sys_step_check', methods=['POST'])
def sys_step_check():
	x = request.form
	ladder = request.args.get('ladder')
	id = request.args.get('step')

	step = json.loads(post(LINK, json={
		'method': 'step.get',
		'token': session['token'],
		'ladder': int(ladder),
		'id': int(id),
	}).text)['step']

	print([[str(i) in x] for i in range(len(step['options']))])

	if any((i in step['answers'] and (str(i) not in x or x[str(i)] != '1')) or (i not in step['answers'] and str(i) in x and x[str(i)] == '1') for i in range(len(step['options']))):
		return redirect(LINK + 'ladder/' + ladder + '/study/' + id)
	else:
		return redirect(LINK + 'ladder/' + ladder + '/question/' + str(int(id)+1))