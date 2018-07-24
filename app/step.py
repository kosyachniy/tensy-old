from flask import render_template, session, request, Markup
from app import app, LINK, get_preview

from requests import post
from json import loads
import markdown
import re

@app.route('/ladder/<int:ladder>/question/<int:id>')
@app.route('/ladder/<int:ladder>/question/<int:id>/')
def step(ladder, id):
	step = loads(post(LINK, json={'method': 'step.get', 'ladder': ladder, 'id': id}).text)

	if not step['error']:
		step['step']['cont'] = Markup(markdown.markdown(step['step']['cont']))
		for i in range(len(step['step']['options'])):
			step['step']['options'][i] = Markup(markdown.markdown(step['step']['options'][i]))

		return render_template('step.html',
			title = step['step']['name'],
			description = re.sub(r'\<[^>]*\>', '', step['step']['cont']) + '\n' + '; '.join([re.sub(r'\<[^>]*\>', '', i) for i in step['step']['options']]),
			tags = step['tags'],
			url = 'ladder/%d/question/%d' % (ladder, id),

			user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text)['user'] if 'id' in session else {'id': 0, 'admin': 2},

			preview = get_preview,
			enumerate = enumerate,
			str = str,

			step = step['step'],
			ladder = ladder,
			id = id,
		)
	else:
		return render_template('message.html', cont='End.')