from dbio import *
import expressionparser as ep
originalquestions = ["qUsage.html", "qBrand.html", "qPrice.html", "qSize.html"]
questions = []
i = 0
db = []

def handleInput(givenInput):
	global questions
	global db
	questionType = givenInput.get("questiontype")
	if questionType == "questionselector":
		newQuestionsStrings = givenInput.getlist("selected")
		for n in newQuestionsStrings:
			newQuestions = n.split(" ")
			for nq in newQuestions:
				if nq not in questions:
					questions.append(nq)
	elif questionType == "Brandlike":
		variable = givenInput.get("variable")
		expression = givenInput.get("expression")
		for k in givenInput:
			if k != "questiontype" and k != "expression" and k != "variable":
				v = givenInput.get(k)
				for i in range(len(db)):
					if variable == None or k == None or db[i][variable].lower() == k.lower():
						db[i]["score"] *= ep.getValue(expression.replace("?k?", k).replace("?v?", v), db[i], givenInput, 0, [])["value"]
	elif questionType == "normal":
		for i in range(len(db)):
			db[i]["score"] *= ep.parseExpression(givenInput.get("expression"), db[i], givenInput)

	elif questionType == "radio":
		variableandvalues = givenInput.get("variableandvalues")
		variableandvalueslist = variableandvalues.split("\t")
		variable = variableandvalueslist[0]
		for i in range(len(db)):
			db[i]["score"] *= ep.parseExpression(givenInput.get(variable), db[i], givenInput)

def getNextQuestion():
	global i
	global questions
	if i == len(questions):
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
		i = 0
		questions = originalquestions.copy()
		for j in range(len(db)):
			db[j]["score"] = 1
	newQuestion = getNextQuestion()
	return newQuestion

def getResults():
	
	data = ""
	result = db
	result = sorted(result, key=lambda result: result['score'], reverse=True)
	i = 0
	while i in range(len(result)):
		j = 0
		row1 = "<tr>"
		row2 = "<tr>"
		row3 = "<tr>"
		while i + j in range(len(result)) and j in range(3):
			row1 = row1 + "<td><a href=\"" + result[i + j]["Url"] + "\"><img src=\"" + str(result[i + j]["Image"]) + "\"></a></td>"
			row2 = row2 + "<td><a href=\"" + result[i + j]["Url"] + "\">" + result[i + j]["Name"] + "</a></td>"
			row3 = row3 + "<td><a href=\"" + result[i + j]["Url"] + "\">Rank: " + str(i + j + 1) + " Score:" + str(result[i + j]["score"]) + " Price: €" + str(result[i + j]["Price"]) + "</a></td>"
			j += 1
		row1 += "</tr>\n"
		row2 += "</tr>\n"
		row3 += "</tr>\n"
		data += row1 + row2 + row3
		i += 3
	
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
