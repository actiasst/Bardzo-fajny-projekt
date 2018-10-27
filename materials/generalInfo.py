def generalInfoFun(material):
	global odb
	try:
		test = odb.materials[material].density.dependencies
		print "Density:"
		print "    Dependencies: " + str(odb.materials[material].density.dependencies)
		print "    Distribution Type: " + str(odb.materials[material].density.distributionType)
		print "    Field Name: " + odb.materials[material].density.fieldName
		print "    Temperature dependency: " + str(odb.materials[material].density.temperatureDependency)
		print "    Table: " + str(odb.materials[material].density.table)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[material].depvar.deleteVar
		print "Depvar:"
		print "    Delete Var: " + str(odb.materials[material].depvar.deleteVar)
		print "    N: " + str(odb.materials[material].depvar.n)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[material].userMaterial.mechanicalConstants
		print "User Material:"
		print "    Mechanical Constants: " + str(odb.materials[material].userMaterial.mechanicalConstants)
		print "    Thermal Constants: " + str(odb.materials[material].userMaterial.thermalConstants)
		print "    Type: " + str(odb.materials[material].userMaterial.type)
		print "    Unsymm: " + str(odb.materials[material].userMaterial.unsymm)
	except AttributeError:
		strangeVariable = 0