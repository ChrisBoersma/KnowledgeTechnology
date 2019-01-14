import math

def sigmoid(args):
	#print("Sigmoid args: " + str(args))
	x = float(args[1]) - float(args[0])
	print(x)
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
	#		print("ParseFunctionParameters: " + expression[i])
			dict = getValue(expression, specs, givenInput, i, [",", ")"])
			parameters.append(dict["value"])
			i = dict["i"]
	#		print(i)
	#print(expression[i])
	return {"parameters": parameters, "i": i + 1}
	#pass

def parseVariable(expression, i, specs, givenInput):
	variablename = ""
	parameters = []
	while i in range(len(expression)) and (expression[i].isalnum() or expression[i] == "_"):
		print("Expression: " + expression + " i: " + str(i) + " expression[i]: " + expression[i])
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
			
	#if parameters == []:
	#else:
	#print({"value": value, "i": i})
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
		#elif expression[i] == " ":
		#	break
		else:
			break			
			#raise ValueError
		i += 1
	return {"value": result, "i": i}
	
def parseInputVariable(expression, i, givenInput):
	i += 1
	variablename = ""
	while i in range(len(expression)) and expression[i] != ">":
		print("parseInputVariable : Expression: " + expression + " i: " + str(i) + " expression[i]: " + expression[i])
		variablename += expression[i]
		i += 1
	return {"value": givenInput.get(variablename), "i": i + 1}

def parseString(expression, i, givenInput):
	i += 1
	variablename = ""
	while i in range(len(expression)) and expression[i] != '"':
		print("Expression: " + expression + " i: " + str(i) + " expression[i]: " + expression[i])
		variablename += expression[i]
		i += 1
	return {"value": variablename, "i": i + 1}

symbols = ["+", "-", "*", "/"]
symbols2 = ["=", "!"]

def getValue(expression, specs, givenInput, i, ends):
	values = []
	while i in range(len(expression)):
		print("getValue : Expression: " + expression + " i: " + str(i) + " expression[i]: " + expression[i])
		#print("getValue " + expression[i])
		if expression[i] in ends:
			break
		elif expression[i].isalpha():
			dict = parseVariable(expression, i, specs, givenInput)
		#	print("Dict:" + str(dict))
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
		elif expression[i] == '"':
			dict = parseString(expression, i, givenInput)
			values.append(dict["value"])
			i = dict["i"]
		elif expression[i] in symbols:
		#	print("VALUES: ", values)
			if(len(values) < 2):
				raise ValueError
			a = float(values[-2])
			b = float(values[-1])
			values = values[:-1]
			#print("VALUES2: ", values)
			if expression[i] == "+":
				values[-1] = a + b
			elif expression[i] == "-":
				values[-1] = a - b				
			elif expression[i] == "*":
				values[-1] = a * b
			elif expression[i] == "/":
				values[-1] = a / b
			#print("VALUES3: ", values)
			i += 1
		elif expression[i] in symbols2:
			print("VALUES: ", values)
			if(len(values) < 2):
				raise ValueError
			a = values[-2]
			b = values[-1]
			values = values[:-1]
			print("Substring: ", expression[i:i+2])
			if expression[i:i+2] == "==":
				values[-1] = (a == b)
			elif expression[i:i+2] == "!=":
				values[-1] = (a != b)
			i += 2
	return {"value": values[0], "i": i}

def parseExpression(expression, specs, givenInput):
	score = 1
	#print("Nothing lasts forever")
	if "?" in expression:
	#	print("I got so faaar")
	#	print(givenInput)
		for k in givenInput:
	#		print("Nation controlled by the media")
			if k != "questiontype" and k != "expression":
				v = givenInput.get(k)
	#			print(k + ", " + v)
				score *= getValue(expression.replace("?k?", k).replace("?v?", v), specs, givenInput, 0, [])["value"]
	else:
		score *= getValue(expression, specs, givenInput, 0, [])["value"]
	#print("SCOOOORE ", score)
	return score

#p = parseValue("92.2", 0, {}, {})
#print(p)
#p = parseVariable("heyo ", 0, {"heyo": 12}, {})
#print(p)
p = parseExpression('"What" a ==', {"a": "What"}, {})
print(p)
#print(p)
