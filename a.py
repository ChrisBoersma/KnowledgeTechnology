from dbio import *
import test2
questions = ["qUsage.html", "qBrand.html", "qPrice.html", "qSize.html"]
i = 0
db = []

def updateScores(expression, variable, v):
	for i in range(len(scores)):
		if variable == None or v == None or db[i][variable] == v:
			scores[i] *= test2.parseExpression(expression, db[i])

def handleInput(givenInput):
	global questions
	global db
	print("Scheisse")
	questionType = givenInput.get("questiontype")
	if questionType == "questionselector":
		newQuestionsStrings = givenInput.getlist("selected")
		for n in newQuestionsStrings:
			newQuestions = n.split(" ")
			for nq in newQuestions:
				if nq not in questions:
					questions.append(nq)
	elif questionType == "Brandlike":
	#	variableandvalues = givenInput.getList("variableandvalues")
	#	variableandvalueslist = variableandvalues.split("\t")
	#	variable = variableandvalueslist[0]
	#	values = variableandvalueslist[1:]
		variable = givenInput.get("variable")
		for k in givenInput:
			if k != "questiontype" and k != "expression" and k != "variable":
				v = givenInput.get(k)
				for i in range(len(db)):
					if variable == None or k == None or db[i][variable] == k:
						db[i]["score"] *= test2.getValue(expression.replace("?k?", k).replace("?v?", v), specs, givenInput, 0, [])["value"]
						#test2.parseExpression(givenInput.get("expression"), db[i], givenInput)
	elif questionType == "normal":
		for i in range(len(db)):
			db[i]["score"] *= test2.parseExpression(givenInput.get("expression"), db[i], givenInput)
	print("QuestionType: ", questionType)
	
	#elif questionType == "Brandlike":
	#	variableandvalues = givenInput.getList("variableandvalues")
	#	variableandvalueslist = variableandvalues.split("\t")
	#	variable = variableandvalueslist[0]
	#	values = variableandvalueslist[1:]
	#	for v in values:
	#		value = givenInput.get(v)
	#		updateScores(variable, value, v)
	print(questions)

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
	global i
	if i == 0:
		for j in range(len(db)):
			db[j]["score"] = 1
	handleInput(givenInput)
	newQuestion = getNextQuestion()
	for d in db:
		print(d)
	return newQuestion

def getResults():
	newDb = db
	newDb = sorted(newDb, key=lambda newDb: newDb['score'])
	return newDb
		

def init():
	global db
	db = openDB("dbsavefile1")[:5]

init()
