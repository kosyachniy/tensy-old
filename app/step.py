from flask import render_template, session, request, Markup
from app import app, LINK, get_preview

from requests import post
from json import loads
import markdown

@app.route('/ladder/<int:ladder>/question/<int:id>')
@app.route('/ladder/<int:ladder>/question/<int:id>/')
def step(ladder, id):
	step = loads(post(LINK, json={'method': 'step.get', 'ladder': ladder, 'id': id}).text)
	step['step']['cont'] = Markup(markdown.markdown(step['step']['cont']))
	for i in range(len(step['step']['options'])):
		step['step']['options'][i] = str(Markup(markdown.markdown(step['step']['options'][i]))).replace('<p>', '').replace('</p>', '')

	return render_template('step.html',
		title = step['step']['name'],
		description = step['step']['cont'] if step['step']['cont'] else '; '.join(step['step']['options']),
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