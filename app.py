
from __future__ import print_function
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for

import io
import os
import uuid
import read
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.debug = True
app._static_folder = os.path.abspath("templates/static/")

@app.route('/', methods=['GET'])
def index():
	title = 'Hello world'
	read.init()
	q = read.getNextQuestion()
	data = read.generateForm(q)
	return render_template('layouts/index.html',
						   title=title, data = data)

@app.route('/results/', methods=['GET', 'POST'])
def results():
	title = 'Result'
	#data = get_file_content(uuid)
	data = request.form.getlist("brand")
	#for d in data:
	#	print(d)
	#print(data)
	return render_template('layouts/results.html',
						   title=title,
						   data=data)

#@app.route('/postmethod', methods = ['POST'])
#def post_javascript_data():
#	jsdata = request.form['canvas_data']
#	unique_id = create_csv(jsdata)
#	params = { 'uuid' : unique_id }
#	return jsonify(params)



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
