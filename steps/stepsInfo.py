list = odb.steps.keys()

for tmp in list:
	try:
		test = odb.steps[tmp].name
		print "STEP:"
		print "Name: " + odb.steps[tmp].name
		print "Acoustic Mass: " + str(odb.steps[tmp].acousticMass)
		print "Acoustic Mass Center: " + str(odb.steps[tmp].acousticMassCenter)
		print "Description: " + str(odb.steps[tmp].description)
		print "Domain: " + str(odb.steps[tmp].domain)
		print "Procedure: " + str(odb.steps[tmp].procedure)
		print "Retained Eigen Modes: " + str(odb.steps[tmp].retainedEigenModes)
		print "Time Period: " + str(odb.steps[tmp].timePeriod)
		print "Total Time: " + str(odb.steps[tmp].totalTime)
		try:
			for tmp2 in range(len(odb.steps[tmp].frames)):
				print "FRAME"
				print "    Frame Id: " + str(odb.steps[tmp].frames[tmp2].frameId)
				print "    Description: " + str(odb.steps[tmp].frames[tmp2].description)
				print "    Associated Frame: " + str(odb.steps[tmp].frames[tmp2].associatedFrame)
				print "    Cyclic Mode Number: " + str(odb.steps[tmp].frames[tmp2].cyclicModeNumber)
				print "    Domain: " + str(odb.steps[tmp].frames[tmp2].domain)
				print "    Frame Value: " + str(odb.steps[tmp].frames[tmp2].frameValue)
				print "    Frequency: " + str(odb.steps[tmp].frames[tmp2].frequency)
				print "    Increment Number: " + str(odb.steps[tmp].frames[tmp2].incrementNumber)
				print "    Is Imaginary: " + str(odb.steps[tmp].frames[tmp2].isImaginary)
				print "    Load Case: " + str(odb.steps[tmp].frames[tmp2].loadCase)
				print "    Mode: " + str(odb.steps[tmp].frames[tmp2].mode)
				try:
					list3 = odb.steps[tmp].frames[tmp2].fieldOutputs.keys()
					for tmp3 in list3:
						test = odb.steps[tmp].frames[tmp2].fieldOutputs[tmp3].name
						print "    FIELD OUTPUT:"
						print "        Name: " + odb.steps[tmp].frames[tmp2].fieldOutputs[tmp3].name
						print "        Base Element Types: " + str(odb.steps[tmp].frames[tmp2].fieldOutputs[tmp3].baseElementTypes)
						print "        Component Labels: " + str(odb.steps[tmp].frames[tmp2].fieldOutputs[tmp3].componentLabels)
						print "        Description: " + str(odb.steps[tmp].frames[tmp2].fieldOutputs[tmp3].description)
						print "        Is Complex: " + str(odb.steps[tmp].frames[tmp2].fieldOutputs[tmp3].isComplex)
						print "        Type: " + str(odb.steps[tmp].frames[tmp2].fieldOutputs[tmp3].type)
						print "        Valid Invariants: " + str(odb.steps[tmp].frames[tmp2].fieldOutputs[tmp3].validInvariants)
				except AttributeError:
					strangeVariable = 0
		except AttributeError:
			strangeVariable = 0
		print " "
	except AttributeError:
		strangeVariable = 0