def thermalInfoFun(material):
	global odb
	try:
		test = odb.materials[material].conductivity.dependencies
		print "Conductivity:"
		print "    Dependencies: " + str(odb.materials[material].conductivity.dependencies)
		print "    Table: " + str(odb.materials[material].conductivity.table)
		print "    Temperature Dependency: " + str(odb.materials[material].conductivity.temperatureDependency)
		print "    Type: " + str(odb.materials[material].conductivity.type)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[material].inelasticHeatFraction.fraction
		print"Inelastic Heat Fraction:"
		print "    Fraction: " + str(odb.materials[material].inelasticHeatFraction.fraction)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[material].specificHeat.dependencies
		print"Specific Heat:"
		print "    Dependencies: " + str(odb.materials[material].specificHeat.dependencies)
		print "    Law: " + str(odb.materials[material].specificHeat.law)
		print "    Table: " + str(odb.materials[material].specificHeat.table)
		print "    Temperature Dependency: " + str(odb.materials[material].specificHeat.temperatureDependency)
	except AttributeError:
		strangeVariable = 0