import math

def sigmoid(args):
	x = float(args[1]) - float(args[0]) / 100

	if x > 20:
		return 1
	elif x < -20:
		return 0
	else:
		return 1 / (1 + math.exp(-x))

functions = {"sigmoid": sigmoid}

def parseFunctionParameters(expression, i, specs, givenInput):
	parameters = []
	i += 1
	while i in range(len(expression)) and expression[i] != ")":
		if expression[i] == ",":
			i += 1
		else:
			dict = getValue(expression, specs, givenInput, i, [",", ")"])
			parameters.append(dict["value"])
			i = dict["i"]
	return {"parameters": parameters, "i": i + 1}

def parseVariable(expression, i, specs, givenInput):
	variablename = ""
	parameters = []
	while i in range(len(expression)) and (expression[i].isalnum() or expression[i] == "_"):
		variablename += expression[i]
		i += 1
	if i < len(expression) and expression[i] == "(":
		dict = parseFunctionParameters(expression, i, specs, givenInput)
		i = dict["i"]
		parameters = dict["parameters"]
		value = functions[variablename](parameters)
	else:
		print(specs)
		if isinstance(specs[variablename], float):
			value = specs[variablename]
		else:
			value = specs[variablename].split(" ")[0]
	return {"value": value, "i": i}

def parseValue(expression, i, specs, givenInput):
	isDecimal = 0
	result = 0
	div = 10
	while i in range(len(expression)):
		if expression[i].isnumeric():
			if isDecimal:
				result += int(expression[i]) / div
				div *= 10
			else:
				result *= 10
				result += int(expression[i])
		elif expression[i] == ".":
			isDecimal = 1
		else:
			break
		i += 1
	return {"value": result, "i": i}
	
def parseInputVariable(expression, i, givenInput):
	i += 1
	variablename = ""
	while i in range(len(expression)) and expression[i] != ">":
		variablename += expression[i]
		i += 1
	return {"value": givenInput.get(variablename), "i": i + 1}

def parseString(expression, i, givenInput):
	i += 1
	variablename = ""
	while i in range(len(expression)) and expression[i] != "'":
		variablename += expression[i]
		i += 1
	return {"value": variablename, "i": i + 1}

symbols = ["+", "-", "*", "/"]
symbols2 = ["=", "!"]

def getValue(expression, specs, givenInput, i, ends):
	values = []
	while i in range(len(expression)):
		if expression[i] in ends:
			break
		elif expression[i].isalpha():
			dict = parseVariable(expression, i, specs, givenInput)
			values.append(dict["value"])
			i = dict["i"]
		elif expression[i].isnumeric():
			dict = parseValue(expression, i, specs, givenInput)
			values.append(dict["value"])
			i = dict["i"]
		elif expression[i] == " ":
			i += 1
		elif expression[i] == "<":
			dict = parseInputVariable(expression, i, givenInput)
			values.append(dict["value"])
			i = dict["i"]
		elif expression[i] == "'":
			dict = parseString(expression, i, givenInput)
			values.append(dict["value"])
			i = dict["i"]
		elif expression[i] in symbols:
			if(len(values) < 2):
				raise ValueError
			a = float(values[-2])
			b = float(values[-1])
			values = values[:-1]
			if expression[i] == "+":
				values[-1] = a + b
			elif expression[i] == "-":
				values[-1] = a - b				
			elif expression[i] == "*":
				values[-1] = a * b
			elif expression[i] == "/":
				values[-1] = a / b
			i += 1
		elif expression[i] in symbols2:
			if(len(values) < 2):
				raise ValueError
			a = values[-2]
			b = values[-1]
			values = values[:-1]
			if expression[i:i+2] == "==":
				values[-1] = (a == b)
			elif expression[i:i+2] == "!=":
				values[-1] = (a != b)
			i += 2
	return {"value": values[0], "i": i}

def parseExpression(expression, specs, givenInput):
	score = 1
	if "?" in expression:
		for k in givenInput:
			if k != "questiontype" and k != "expression":
				v = givenInput.get(k)
				score *= getValue(expression.replace("?k?", k).replace("?v?", v), specs, givenInput, 0, [])["value"]
	else:
		score *= getValue(expression, specs, givenInput, 0, [])["value"]
	return score
