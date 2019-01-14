from dbio import *
questions = ["qUsage.html", "qBrand.html", "qPrice.html", "qSize.html"]
i = 0
db = []

def getValue(expression, specs, givenInput, k, v):
	expression = expression.replace("?k?", k).replace("?v?", v)

def parseExpression(expression, specs, givenInput):
	score = 1
	print("Nothing lasts forever")
	if "?" in expression:
		print("I got so faaar")
		print(givenInput)
		for k in givenInput:
			print("Nation controlled by the media")
			v = givenInput.get(k)
			print(k + ", " + v)
			getValue(expression, specs, givenInput, k, v)
	return 1
			

def updateScores(expression, variable, v):
	for i in range(len(scores)):
		if variable == None or v == None or db[i][variable] == v:
			scores[i] *= parseExpression(expression, db[i])

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
	else:
		for i in range(len(db)):
			db[i]["score"] *= parseExpression("?", db[i], givenInput)
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
	return newQuestion

def getResults():
	newDb = db
	newDb = sorted(newDb, key=lambda newDb: newDb['score'])
	return newDb
		

def init():
	global db
	db = openDB("dbsavefile1")

init()
