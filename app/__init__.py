from flask import Flask, redirect
import os, re

app = Flask(__name__)
app.config.from_object('config')

LINK = 'http://167.99.128.56/'

def get_url(url, rep='competions'):
	if not url: url = rep
	if url == 'index': url = ''
	return redirect(LINK + url)

def get_preview(url, num=0):
	url = '/static/load/' + url + '/'
	for i in os.listdir('app' + url):
		if str(num) + '.' in i:
			return url + i
	return url + '0.png'

from app import api

from app import index
from app import admin

from app import login
from app import cabinet

from app import errors

from app import sys_sign_up
from app import sys_sign_in
from app import sys_sign_out
from app import sys_profile_edit
from app import sys_ladder_add
from app import sys_ladder_edit
from app import sys_step_add
from app import sys_step_edit
from app import sys_step_delete

from app import user
from app import experts

from app import ladder
from app import ladders
from app import ladder_add