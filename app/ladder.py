from flask import render_template, session, request, Markup, redirect
from app import app, LINK, get_preview

from requests import post
from json import loads
import markdown

@app.route('/ladder/<int:id>')
@app.route('/ladder/<int:id>/')
def ladder(id):
	edit = request.args.get('edit')

	url = 'ladder/%d' % id
	if edit: url += '?edit=1'

	if edit and 'token' not in session:
		return redirect(LINK + 'login?url=' + url)

	ladder = loads(post(LINK, json={'method': 'ladders.get', 'id': id}).text)['ladder']
	if not edit:
		ladder = dict(ladder)
		ladder['description'] = Markup(markdown.markdown(ladder['description']))

	answers = lambda x: ';'.join([str(i) for i in x])

	return render_template('ladder_edit.html' if edit else 'ladder.html',
		title = ladder['name'],
		description = ladder['description'],
		tags = ladder['tags'],
		url = url,

		user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text)['user'] if 'id' in session else {'id': 0, 'admin': 2},

		preview = get_preview,
		enumerate = enumerate,
		answers = answers,

		ladder = ladder,
	)