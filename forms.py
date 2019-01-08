
def generateForm(question):
	pass

def generateFormPage(question):
	f = open("templates/formPageTemplate.html")
	template = f.read()
	f.close()
	form = generateForm(question)
	page = template.replace("[form]", form)
	f = open("templates/layouts/test.html", "w")
	f.write(page)
	f.close()
