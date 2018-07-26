from flask import render_template, session, request, Markup
from app import app, LINK, get_preview

from requests import post
from json import loads
import markdown
import re

@app.route('/ladder/<int:ladder>/question/<int:step>')
@app.route('/ladder/<int:ladder>/question/<int:step>/')
def step(ladder, step):
	edit = request.args.get('edit')

	url = 'ladder/%d/question/%d' % (ladder, step)
	if edit: url += '?edit=1'

	if edit and 'token' not in session:
		return redirect(LINK + 'login?url=' + url)

	answers = lambda x: ';'.join([str(i) for i in x])

	req = loads(post(LINK, json={'method': 'step.get', 'ladder': ladder, 'step': step}).text)

	if not req['error']:
		if not edit:
			req['step']['cont'] = Markup(markdown.markdown(req['step']['cont']))
			for i in range(len(req['step']['options'])):
				req['step']['options'][i] = Markup(markdown.markdown(req['step']['options'][i]))

		return render_template('step_edit.html' if edit else 'step.html',
			title = req['step']['name'],
			description = re.sub(r'\<[^>]*\>', '', req['step']['cont']) + '\n' + '; '.join([re.sub(r'\<[^>]*\>', '', i) for i in req['step']['options']]),
			tags = req['tags'],
			url = url,

			user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text)['user'] if 'id' in session else {'id': 0, 'admin': 2},

			preview = get_preview,
			enumerate = enumerate,
			str = str,
			answers = answers,

			step = req['step'],
			ladder = ladder,
			id = step,
		)
	else:
		return render_template('message.html', cont='End.')