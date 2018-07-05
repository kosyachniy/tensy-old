from flask import render_template, session, request, Markup
from app import app, LINK, get_preview

from requests import post
from json import loads
import markdown

@app.route('/ladders/<int:id>')
def ladder(id):
	categories = loads(post(LINK, json={'method': 'categories.gets'}).text)
	user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text) if 'id' in session else {'id': 0, 'admin': 2}

	ladder = loads(post(LINK, json={'method': 'ladders.get', 'id': id}).text)
	ladder2 = dict(ladder)
	ladder2['cont'] = Markup(markdown.markdown(ladder2['cont']))

	category = 0
	subcategory = 0
	for i in categories:
		if i['id'] == ladder['category']:
			if i['parent']:
				category = i['parent']
				subcategory = i['id']
			else:
				category = i['id']
			break

	edit = request.args.get('edit')

	return render_template('edit.html' if edit else 'ladder.html',
		title = ladder['name'],
		description = ladder['description'],
		tags = ladder['tags'],
		url = ladder['id'],
		categories = categories,
		user = user,
		category = category,
		subcategory = subcategory,
		preview = get_preview,

		ladder = ladder if edit else ladder2,
	)