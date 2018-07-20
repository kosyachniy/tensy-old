from flask import render_template, session, request, Markup
from app import app, LINK, get_preview

from requests import post
from json import loads
import markdown

@app.route('/ladder/<int:id>')
@app.route('/ladder/<int:id>/')
def ladder(id):
	ladder = loads(post(LINK, json={'method': 'ladders.get', 'id': id}).text)['ladder']
	ladder2 = dict(ladder)
	ladder2['description'] = Markup(markdown.markdown(ladder2['description']))

	edit = request.args.get('edit')

	answers = lambda x: ';'.join([str(i) for i in x])

	return render_template('ladder_edit.html' if edit else 'ladder.html',
		title = ladder['name'],
		description = ladder['description'],
		tags = ladder['tags'],
		url = 'ladder/%d' % ladder['id'],

		user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text)['user'] if 'id' in session else {'id': 0, 'admin': 2},

		preview = get_preview,
		enumerate = enumerate,
		answers = answers,

		ladder = ladder if edit else ladder2,
	)