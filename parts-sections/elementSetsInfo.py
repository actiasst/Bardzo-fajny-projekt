list = odb.rootAssembly.elementSets.keys()

for tmp in list:
	try:
		test = odb.rootAssembly.elementSets[tmp].name
		print "ELEMENT SET: "
		print "Name: " + odb.rootAssembly.elementSets[tmp].name
		print "Instance Names: " + str(odb.rootAssembly.elementSets[tmp].instanceNames)
		print "Is Internal: " + str(odb.rootAssembly.elementSets[tmp].isInternal)
		print "Nodes: " + str(odb.rootAssembly.elementSets[tmp].nodes)
		print " "
	except AttributeError:
		strangeVariable = 0