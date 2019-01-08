questions = {}

def getQuestion(qid):
	global questions
	m = re.split("(\d+)", qid)
	qt = m[0]
	i = int(m[1])
	return questions[qt][i]

def parseQuestion(m):
	parsedQuestion = {}
	if len(m) < 3:
		raise ValueError
	parsedQuestion["question"] = m[0]
	parsedQuestion["variable"] = m[1]
	parsedQuestion["options"] = m[2:]
	return parsedQuestion

questionFiles = [("questions", "q", parseQuestion)]

def readQuestions():
	global questions
	for fn, qt, pf in questionFiles:
		F = open(fn, "r");
		questions[qt] = []
		for l in F.readlines():
			arguments = l.rstrip().split("\t")
			questions[qt].append(pf(arguments))
		F.close()

def init():
	readQuestions()

init()
