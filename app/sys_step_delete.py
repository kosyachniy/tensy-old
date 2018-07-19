from flask import session, request, render_template, redirect
from app import app, LINK

from requests import post
import re, json, base64

@app.route('/sys_step_delete')
def sys_step_delete():
	print('OKK')

	x = request.form
	id = request.args.get('ladder')

	print('OKK')

	req = post(LINK, json={
		'method': 'step.delete',
		'ladder': int(id),
		'step': int(request.args.get('step')),
	}).text

	print(req)
	
	if req.isdigit():
		return render_template('message.html', cont=req)
	else:
		return redirect(LINK + 'ladder/' + id + '/?edit=1')