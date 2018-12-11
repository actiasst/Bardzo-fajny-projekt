import time
time1 = time.time()

list = odb.steps.keys()
for tmp in list:
	try:
		stepData = odb.steps[tmp]
		test = stepData.name
		print "STEP:"
		print "Name: " + stepData.name
		print "Acoustic Mass: " + str(stepData.acousticMass)
		print "Acoustic Mass Center: " + str(stepData.acousticMassCenter)
		print "Description: " + str(stepData.description)
		print "Domain: " + str(stepData.domain)
		print "Procedure: " + str(stepData.procedure)
		print "Retained Eigen Modes: " + str(stepData.retainedEigenModes)
		print "Time Period: " + str(stepData.timePeriod)
		print "Total Time: " + str(stepData.totalTime)
		try:
			for tmp2 in range(len(stepData.frames)):
				frameData = stepData.frames[tmp2]
				print "FRAME"
				print "    Frame Id: " + str(frameData.frameId)
				print "    Description: " + str(frameData.description)
				print "    Associated Frame: " + str(frameData.associatedFrame)
				print "    Cyclic Mode Number: " + str(frameData.cyclicModeNumber)
				print "    Domain: " + str(frameData.domain)
				print "    Frame Value: " + str(frameData.frameValue)
				print "    Frequency: " + str(frameData.frequency)
				print "    Increment Number: " + str(frameData.incrementNumber)
				print "    Is Imaginary: " + str(frameData.isImaginary)
				print "    Load Case: " + str(frameData.loadCase)
				print "    Mode: " + str(frameData.mode)
				try:
					list3 = frameData.fieldOutputs.keys()
					for tmp3 in list3:
						fieldData = frameData.fieldOutputs[tmp3]
						test = fieldData.name
						print "    FIELD OUTPUT:"
						print "        Name: " + fieldData .name
						print "        Base Element Types: " + str(fieldData .baseElementTypes)
						print "        Component Labels: " + str(fieldData .componentLabels)
						print "        Description: " + str(fieldData .description)
						print "        Is Complex: " + str(fieldData .isComplex)
						print "        Type: " + str(fieldData .type)
						print "        Valid Invariants: " + str(fieldData.validInvariants)
				except AttributeError:
					strangeVariable = 0
		except AttributeError:
			strangeVariable = 0
		print " "
	except AttributeError:
		strangeVariable = 0

time2 = time.time()
print "Duration: " + str(time2 - time1)