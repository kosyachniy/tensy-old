from flask import render_template, session, redirect, Markup
from app import app, LINK, get_preview

from requests import post
from json import loads
import markdown

@app.route('/ladder/<int:ladder>/study/<int:step>')
@app.route('/ladder/<int:ladder>/study/<int:step>/')
def study(ladder, step):
	if 'token' in session:
		req = loads(post(LINK, json={
			'method': 'step.study',
			'token': session['token'],
			'ladder': ladder,
			'step': step,
		}).text)

		return render_template('study.html',
			title = 'Study',
			description = '',
			tags = ['study', 'ladder', 'online course'],
			url = 'ladder/%d/study/%d' % (ladder, step),

			user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text)['user'] if 'id' in session else {'id': 0, 'admin': 2},

			preview = get_preview,

			ladder = ladder,
			step = step,
			bot = req['bot'], #Markup(markdown.markdown(loads(post(LINK, json={'method': 'step.get', 'ladder': ladder, 'step': step}).text)['step']['theory'])),
			teachers = req['teachers'],
			users = req['users'],
		)
	else:
		return redirect(LINK + 'login?url=ladder/%d/study/%d' % (ladder, step))