
from __future__ import print_function
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for

import io
import os
import uuid
import interactionmanager

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.debug = True
app._static_folder = os.path.abspath("templates/static/")


@app.route('/', methods=['GET','POST'])
def index():
	title = 'Smartphone recommendation'
	data = "/htmlFiles/index.html"
	return render_template('layouts/index.html',
					   title=title, data = data)
	
@app.route('/questions/', methods=['GET', 'POST'])
def questions():
	title = 'Questions'
	data = request.form.getlist("brand")
	data = interactionmanager.getQuestion(request.form)
	return render_template('layouts/index.html',
						   title=title,
						   data=data)
@app.route('/results/', methods=['GET', 'POST'])
def results():
	title = 'Results'
	result = interactionmanager.getResults()
	#print(result)
	return render_template('layouts/index.html', title=title, data="layouts/resultsFinal.html")
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
