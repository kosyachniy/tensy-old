from flask import render_template, session, request, Markup, redirect
from app import app, LINK, get_preview

from requests import post
from json import loads
import markdown
from time import strftime, gmtime

def time(x):
	return strftime('%d.%m.%Y %H:%M:%S', gmtime(x))

@app.route('/wallet')
@app.route('/wallet/')
def wallet():
	if 'token' in session:
		return render_template('wallet.html',
			title = 'Wallet',
			description = 'Wallet, tokens, transaction history',
			tags = ['wallet', 'tokens', 'transaction history'],
			url = 'wallet',

			user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text)['user'] if 'id' in session else {'id': 0, 'admin': 2},

			preview = get_preview,
			time = time,

			history = loads(post(LINK, json={'method': 'tokens.history', 'token': session['token']}).text)['history'][::-1],
		)

	else:
		return redirect(LINK + 'login?url=wallet')