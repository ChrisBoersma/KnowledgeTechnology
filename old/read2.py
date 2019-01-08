import re

questionFiles = [("questions", "q")]

questions = {}
schedule = []

i = 0

def getQuestion(qid):
	global i
	global questions
	m = re.split("(\d+)", qid)
	qt = m[0]
	i = int(m[1])
	return questions[qt][i]
	
def getNextQuestion():
	global i
	global schedule
	qId = schedule[i]
	i += 1
	return getQuestion(qId)

def parseQuestion(q):
	parsedQuestion = {}
	q = q.rstrip()
	m = re.split("\t", q)
	if len(m) < 3:
		raise ValueError
	parsedQuestion["question"] = m[0]
	parsedQuestion["variable"] = m[1]
	parsedQuestion["options"] = m[2:]
	return parsedQuestion

def init():
	global schedule
	global questionsch
	F = open("questionSchedule", "r");
	for l in F.readlines():
		schedule.append(l.rstrip())
	F.close()
	
	for fn, qt in questionFiles:
		F = open(fn, "r");
		questions[qt] = []
		for l in F.readlines():
			questions[qt].append(parseQuestion(l))
		F.close()

def generateForm(question):
	string = "<div\"id=\"form\">\n<form method='GET'>\n<p id=\"question\">\n"
	string = string + question["question"] + "</p>\n<p id=\"option\">\n"
	for o in question["options"]:
		string =  string + '<input type="checkbox" name="' + question["variable"] + '" value="' + o + '">' + o + '<br>\n'
	string = string + '</p>\n<input type="submit" value="Submit">\n</form>\n</div>'
	return string
#	global schedule
#	global questions
#	f = open("test.html", "w")
#	f.write("<!DOCTYPE html>\n<html>\n<body>\n<head><link rel=\"stylesheet\" type=\"text/css\" href=\"test.css\">\n<meta charset=\"utf-8\">\n<meta name=\"viewport\"content=\"width=device-width, initial-scale=1\">\n</head>\n<div" id=\"form\">\n<p id=\"question\">\n")
#	q = questions.get("question","No question found")
#	f.write(q+"\n")
#	f.write("</p>\n<p id=\"option\">\n")
#	for o in questions.get("options","No options found"):
#		f.write(o)
#	f.write("\n</p>\n</div>\n</body>\n</html>")
#	f.close()

	
	
	
