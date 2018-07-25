from flask import render_template, session, request, Markup
from app import app, LINK, get_preview

from requests import post
from json import loads
import markdown
import re

@app.route('/space')
@app.route('/space/')
def space():
	if 'token' in session:
		try:
			ladder = int(request.args.get('ladder'))
		except:
			ladder = 0

		try:
			step = int(request.args.get('step'))
		except:
			step = 0

		try:
			user = int(request.args.get('user'))
		except:
			user = 0

		req = loads(post(LINK, json={'method': 'step.get', 'ladder': ladder, 'step': step}).text)

		if not user:
			theory = req['step']['theory']
		else:
			theory = 'blabla'

		theory = Markup(markdown.markdown(theory))

		return render_template('space.html',
			title = 'Theory',
			description = re.sub(r'\<[^>]*\>', '', str(theory)),
			tags = ['theory'] + req['tags'],
			url = 'space/?user=%d&ladder=%d&step=%d' % (user, ladder, step),

			user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text)['user'] if 'id' in session else {'id': 0, 'admin': 2},

			preview = get_preview,

			users = 'blabla' if user else 'Bot',
			ladder = req['name'],
			step = req['step']['name'],
			ladder_id = ladder,
			step_id = step,
			theory = theory,
		)
	else:
		return redirect(LINK + 'login?url=space/?user=%d&ladder=%d&step=%d' % (user, ladder, step))