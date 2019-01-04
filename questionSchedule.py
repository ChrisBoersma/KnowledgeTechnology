import questions

schedule = []
i = 0

def addToSchedule(questions):
	global schedule
	if type(questions) ~= list:
		questions = [questions]
	schedule = questions + schedule

def getNextQuestion():
	global i
	global schedule
	qId = schedule[i]
	i += 1
	return getQuestion(qId)

def readQuestionSchedule():
	global schedule
	F = open("questionSchedule", "r");
	for l in F.readlines():
		schedule.append(l.rstrip())
	F.close()

def init():
	readQuestionSchedule()

init()

