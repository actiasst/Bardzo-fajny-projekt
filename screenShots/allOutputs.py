import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior
from abaqusConstants import *
import time
time1 = time.time()

def startAllOutputs():
	o7 = session.odbs['E:/Abaqus/za duze/explosive_3D_DT_Air_H30_H03-ALE.odb']
	session.viewports['Viewport: 1'].setValues(displayedObject=o7)
	session.mdbData.summary()
	session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(DEFORMED, ))
	session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF, ))

def changeType(name,outputPosition,type = "none",type2 = "none"):
	if type != "none":
		if type == "INVARIANT":
			session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(variableLabel=name, outputPosition=outputPosition,
			refinement=(INVARIANT, type2), )
		if type == "COMPONENT":
			session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(variableLabel=name, outputPosition=outputPosition,
			refinement=(COMPONENT, type2), )
	else:
		session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        	variableLabel=name, outputPosition=outputPosition, )


def makeScreenshot(path):
	session.printToFile(fileName=path, format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

def createDirectory(path):
	if not os.path.exists(path):
		os.makedirs(path)

def translate(string):
	if string == MAGNITUDE:
		return "Magnitude"
	elif string == MISES:
		return "Mises"
	elif string == MAX_PRINCIPAL:
		return "Max. Principal"
	elif string == MID_PRINCIPAL:
		return "Mid. Principal"
	elif string == MIN_PRINCIPAL:
		return "Min. Principal"
	elif string == TRESCA:
		return "Tresca"
	elif string == PRESS:
		return "Pressure"
	elif string == INV3:
		return "Third Invariant"

def changeFrame(step,frame):
	session.viewports[session.currentViewportName].odbDisplay.setFrame(step=step, frame=frame)

def changePart(part):
	leaf = dgo.LeafFromPartInstance(partInstanceName=(part, ))
	session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)

def addPart(part):
	leaf = dgo.LeafFromPartInstance(partInstanceName=(part, ))
	session.viewports['Viewport: 1'].odbDisplay.displayGroup.add(leaf=leaf)

viewList = ["Front","Back","Top","Bottom","Left","Right","Iso"]
listPart = odb.rootAssembly.instances.keys()

startAllOutputs()
path = "C:\\temp\\skrypty\\allScreens\\"
list = odb.steps.keys()
for tmp in list:
	stepData = odb.steps[tmp]
	for tmp2 in range(len(stepData.frames)):
	#for tmp2 in range(1):
		changeFrame(stepData.name,tmp2)
		frameData = stepData.frames[tmp2]
		path = "C:\\temp\\skrypty\\allScreens\\" + stepData.name+ "\\" + str(tmp2)
		createDirectory(path)
		list2 = frameData.fieldOutputs.keys()
		for tmp3 in list2:
			fieldTmp = frameData.fieldOutputs[tmp3]
			name = fieldTmp.name
			for invariant in range(len(fieldTmp.validInvariants)):
				changeType(name,fieldTmp.locations[0].position,"INVARIANT",translate(fieldTmp.validInvariants[invariant]))
				createDirectory(path+"\\"+name+"\\"+str(fieldTmp.validInvariants[invariant]))
				for view in range(len(viewList)):
					changeView(viewList[view])
					for tmp4 in listPart:
						changePart(tmp4)
						makeScreenshot(path+"\\"+name+"\\"+str(fieldTmp.validInvariants[invariant])+"\\"+tmp4)
					for tmp4 in listPart:
						addPart(tmp4)
					makeScreenshot(path+"\\"+name+"\\"+str(fieldTmp.validInvariants[invariant])+"\\"+"All")
			for componentLabes in range(len(fieldTmp.componentLabels)):
				changeType(name,fieldTmp.locations[0].position,"COMPONENT",fieldTmp.componentLabels[componentLabes])
				createDirectory(path+"\\"+name+"\\"+str(fieldTmp.componentLabels[componentLabes]))
				for view in range(len(viewList)):
					changeView(viewList[view])
					for tmp4 in listPart:
						changePart(tmp4)
						makeScreenshot(path+"\\"+name+"\\"+str(fieldTmp.componentLabels[componentLabes])+"\\"+tmp4)
					for tmp4 in listPart:
						addPart(tmp4)
					makeScreenshot(path+"\\"+name+"\\"+str(fieldTmp.componentLabels[componentLabes])+"\\"+"All")
			if len(fieldTmp.componentLabels) == 0 and len(fieldTmp.componentLabels) == 0:
				changeType(name,fieldTmp.locations[0].position)
				createDirectory(path+"\\"+name)
				for view in range(len(viewList)):
					changeView(viewList[view])
					for tmp4 in listPart:
						changePart(tmp4)
						makeScreenshot(path+"\\"+name+"\\"+tmp4)
					for tmp4 in listPart:
						addPart(tmp4)
					makeScreenshot(path+"\\"+name+"\\"+"All")

				

time2 = time.time()
print "Duration: " + str(time2 - time1)











