
from __future__ import print_function
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for

import io
import os
import uuid
#import read
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import a

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.debug = True
app._static_folder = os.path.abspath("templates/static/")

@app.route('/', methods=['GET'])
def index():
	title = 'Hello world'
	#read.init()
	#q = read.getNextQuestion()
	#data = read.generateForm(q)
	data = "htmlFiles/qBrand.html"
	return render_template('layouts/index.html',
						   title=title, data = data)
@app.route('/questions/', methods=['GET', 'POST'])
def questions():
	title = 'Question'
	data = request.form.getlist("brand")
	data = a.getQuestion(request.form)
	return render_template('layouts/results.html',
						   title=title,
						   data=data)
@app.route('/results/', methods=['GET', 'POST'])
def results():
	title = 'Result'
	data = a.getResults()
	return render_template('layouts/results.html',
						   title=title,
						   data=data)
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
