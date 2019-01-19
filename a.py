from dbio import *
import test2
originalquestions = ["qUsage.html", "qBrand.html", "qPrice.html", "qSize.html"]
questions = []
i = 0
db = []

def updateScores(expression, variable, v):
	for i in range(len(scores)):
		if variable == None or v == None or db[i][variable] == v:
			scores[i] *= test2.parseExpression(expression, db[i])

def handleInput(givenInput):
	global questions
	global db
	questionType = givenInput.get("questiontype")
	if questionType == "questionselector":
		print(questions)
		print(originalquestions)
		newQuestionsStrings = givenInput.getlist("selected")
		for n in newQuestionsStrings:
			print("Questions String ", n)
			newQuestions = n.split(" ")
			for nq in newQuestions:
				if nq not in questions:
					questions.append(nq)
		print(questions)
		print(originalquestions)
	elif questionType == "Brandlike":
	#	variableandvalues = givenInput.getList("variableandvalues")
	#	variableandvalueslist = variableandvalues.split("\t")
	#	variable = variableandvalueslist[0]
	#	values = variableandvalueslist[1:]
		variable = givenInput.get("variable")
		expression = givenInput.get("expression")
		for k in givenInput:
			if k != "questiontype" and k != "expression" and k != "variable":
				v = givenInput.get(k)
				for i in range(len(db)):
					#print("Variable: ", variable, " k: ", k, " db: ", db[i][variable].lower(), " k.lower(): ", k.lower())
					if variable == None or k == None or db[i][variable].lower() == k.lower():
						db[i]["score"] *= test2.getValue(expression.replace("?k?", k).replace("?v?", v), db[i], givenInput, 0, [])["value"]
						#test2.parseExpression(givenInput.get("expression"), db[i], givenInput)
		for r in db:
			print(r["Name"], " ", r["score"])
	elif questionType == "normal":
		for i in range(len(db)):
			print("Budget: ", givenInput.get("Budget"))
			db[i]["score"] *= test2.parseExpression(givenInput.get("expression"), db[i], givenInput)
			print(db[i]["score"])

	elif questionType == "radio":
		variableandvalues = givenInput.get("variableandvalues")
		variableandvalueslist = variableandvalues.split("\t")
		variable = variableandvalueslist[0]
		for i in range(len(db)):
			db[i]["score"] *= test2.parseExpression(givenInput.get(variable), db[i], givenInput)
	
	#elif questionType == "Brandlike":
	#	variableandvalues = givenInput.getList("variableandvalues")
	#	variableandvalueslist = variableandvalues.split("\t")
	#	variable = variableandvalueslist[0]
	#	values = variableandvalueslist[1:]
	#	for v in values:
	#		value = givenInput.get(v)
	#		updateScores(variable, value, v)
	#print(questions)

def getNextQuestion():
	global i
	global questions
	if i == len(questions):
		#results
		return "layouts/results.html"
	q = questions[i]
	i += 1
	return "htmlFiles/" + q

def getQuestion(givenInput):
	global db
	global questions
	global i
	handleInput(givenInput)
	if len(givenInput) == 0:
		print("no given input")

		i = 0
		questions = originalquestions.copy()
		for j in range(len(db)):
			db[j]["score"] = 1
	newQuestion = getNextQuestion()
	#for d in db:
		#print(d)
	return newQuestion

def getResults():
	
	data = ""
	result = db
	result = sorted(result, key=lambda result: result['score'], reverse=True)
	for i in range(len(result)):
		data = data + "<tr><td>" + result[i]["Name"] + "</td><td> " + "<a href=\"" + result[i]["Url"] + "\">Link </a></td><td>" + str(result[i]["score"]) + "</td><td><img src=\"" + str(result[i]["Image"]) + "\"></td></tr>" + "<br>\n"
	
	f = open("templates/layouts/resultsFinal.html", "w")
	f.write("<div class=\"row text-center\"> \n <h1>Results</h1> \n<table>"+ data +"</table>\n </div>")
	f.close
		
	return data
		

def init():
	global db
	db = openDB("dbsavefile0")
	for j in range(len(db)):
		db[j]["score"] = 1
init()
