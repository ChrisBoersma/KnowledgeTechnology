import re

questionFiles = [("questions", "q")]

questions = {}
schedule = []

def getQuestion(qid):
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
	global questions
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
