def basicInfoFun(material):
	global odb
	try:
		test = odb.materials[material].name
		print "Name: " + odb.materials[material].name
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[material].description
		print "Description: " + odb.materials[material].description
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[material].materialIdentifier
		print "Material Identifier: " + odb.materials[material].materialIdentifier
	except AttributeError:
		strangeVariable = 0
