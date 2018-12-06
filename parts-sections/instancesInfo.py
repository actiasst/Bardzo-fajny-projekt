list = odb.rootAssembly.instances.keys()

for tmp in list:
	try:
		test = odb.rootAssembly.instances[tmp].name
		print "INSTANCE: "
		print "Name: " + odb.rootAssembly.instances[tmp].name
		print "Analytic Surface: " + str(odb.rootAssembly.instances[tmp].analyticSurface)
		print "Embedded Space: " + str(odb.rootAssembly.instances[tmp].embeddedSpace)
		print "Type: " + str(odb.rootAssembly.instances[tmp].type)
		list2 = odb.rootAssembly.instances[tmp].elementSets.keys()
		for tmp2 in list2:		
			try:
				test = odb.rootAssembly.instances[tmp].elementSets[tmp2].name
				print "ELEMENT SET:"
				print "    Name: " + odb.rootAssembly.instances[tmp].elementSets[tmp2].name
				print "    Faces: " + str(odb.rootAssembly.instances[tmp].elementSets[tmp2].faces)
				print "    Instance Names: " + str(odb.rootAssembly.instances[tmp].elementSets[tmp2].instanceNames)
				print "    Instances: " + str(odb.rootAssembly.instances[tmp].elementSets[tmp2].instances)
				print "    Is Internal: " + str(odb.rootAssembly.instances[tmp].elementSets[tmp2].isInternal)
				print "    Nodes: " + str(odb.rootAssembly.instances[tmp].elementSets[tmp2].nodes)
			except AttributeError:
				strangeVariable = 0
		number = len(odb.rootAssembly.instances[tmp].sectionAssignments)
		for number in range(number):
			try:
				test = odb.rootAssembly.instances[tmp].sectionAssignments[number].sectionName
				print "SECTION ASSIGMENT:"
				print "    Section Name: " + odb.rootAssembly.instances[tmp].sectionAssignments[number].sectionName
				print "    Offset: " + str(odb.rootAssembly.instances[tmp].sectionAssignments[number].offset)
				try:
					test = odb.rootAssembly.instances[tmp].sectionAssignments[number].region.name
					print "    REGION: "
					print "        Name: " + odb.rootAssembly.instances[tmp].sectionAssignments[number].region.name
					print "        Faces: " + str(odb.rootAssembly.instances[tmp].sectionAssignments[number].region.faces)
					print "        Instance Names: " + str(odb.rootAssembly.instances[tmp].sectionAssignments[number].region.instanceNames)
					print "        Instances: " + str(odb.rootAssembly.instances[tmp].sectionAssignments[number].region.instances)
					print "        Is Internal: " + str(odb.rootAssembly.instances[tmp].sectionAssignments[number].region.isInternal)
					print "        Nodes: " + str(odb.rootAssembly.instances[tmp].sectionAssignments[number].region.nodes)
				except AttributeError:
					strangeVariable = 0
			except AttributeError:
				strangeVariable = 0
		print " "
	except AttributeError:
		strangeVariable = 0