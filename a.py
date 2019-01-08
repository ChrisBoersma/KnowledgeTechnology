questions = ["qUsage.html", "qBrand.html", "qPrice.html", "qSize.html"]
i = 0

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
