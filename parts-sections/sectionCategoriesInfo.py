list = odb.sectionCategories.keys()

for tmp in list:
	try:
		test = odb.sectionCategories[tmp].name
		print "Name: " + odb.sectionCategories[tmp].name
		print "Description: " + str(odb.sectionCategories[tmp].description)
		print " "
	except AttributeError:
		strangeVariable = 0