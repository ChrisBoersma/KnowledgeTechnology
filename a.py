questions = ["qUsage.html", "qBrand.html", "qPrice.html", "qSize.html"]
i = 0

def parseExpression(expression, specs):
	pass

def updateScores(expression, variable, v):
	for i in range(len(scores)):
		if variable == None or v == None or db[i][variable] == v:
			scores[i] *= parseExpression(expression, db[i])

def handleInput(givenInput):
	global questions
	questionType = givenInput.get("questionType")
	if questionType == "QuestionSelector":
		newQuestionsStrings = givenInput.getList("selected")
		for n in newQuestionsStrings:
			newQuestions = n.split(" ")
			for nq in newQuestions:
				if nq not in questions:
					questions.append(nq)
	elif questionType == "Brandlike":
		variableandvalues = givenInput.getList("variableandvalues")
		variableandvalueslist = variableandvalues.split("\t")
		variable = variableandvalueslist[0]
		values = variableandvalueslist[1:]
		for v in values:
			value = givenInput.get(v)
			updateScores(variable, value, v)

def getNextQuestion():
	global i
	if i == len(questions):
		#results
		return "resultsRedirect.html"
	q = questions[i]
	i += 1
	return "htmlFiles/" + q

def getQuestion(givenInput):
	handleInput(givenInput)
	newQuestion = getNextQuestion()
	return newQuestion

def getResults():
	pass
