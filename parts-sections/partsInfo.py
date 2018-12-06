list = odb.parts.keys()

for tmp in list:
	try:
		test = odb.parts[tmp].name
		print "Name: " + odb.parts[tmp].name
		print "Analytic Surface: " + str(odb.parts[tmp].analyticSurface)
		print "Embedded Space: " + str(odb.parts[tmp].embeddedSpace)
		print "Type: " + str(odb.parts[tmp].type)
		print " "
	except AttributeError:
		strangeVariable = 0