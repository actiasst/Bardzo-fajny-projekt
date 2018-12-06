list = odb.sections.keys()

for tmp in list:
	try:
		test = odb.sections[tmp].name
		print "Name: " + odb.sections[tmp].name
		print "Material: " + str(odb.sections[tmp].material)
		print "Thickness: " + str(odb.sections[tmp].thickness)
		print " "
	except AttributeError:
		strangeVariable = 0