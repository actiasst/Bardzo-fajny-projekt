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

def start():
	o7 = session.odbs['E:/Abaqus/za duze/explosive_3D_DT_Air_H30_H03-ALE.odb']
	session.viewports['Viewport: 1'].setValues(displayedObject=o7)
	session.mdbData.summary()

def turnOffMesh():
	session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        visibleEdges=FEATURE)

def changePart(part):
	leaf = dgo.LeafFromPartInstance(partInstanceName=(part, ))
	session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)

def makeScreenshot(path):
	session.printToFile(fileName=path, format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

def addPart(part):
	leaf = dgo.LeafFromPartInstance(partInstanceName=(part, ))
	session.viewports['Viewport: 1'].odbDisplay.displayGroup.add(leaf=leaf)

def changeView(view):
	session.viewports['Viewport: 1'].view.setValues(session.views[view])

def createDirectory(path):
	if not os.path.exists(path):
		os.makedirs(path)

path = "C:\\temp\\skrypty\\allScreens\\"
viewList = ["Front","Back","Top","Bottom","Left","Right","Iso"]
list = odb.rootAssembly.instances.keys()
start()
turnOffMesh()
createDirectory(path+"Front")
createDirectory(path+"Back")
createDirectory(path+"Top")
createDirectory(path+"Bottom")
createDirectory(path+"Left")
createDirectory(path+"Right")
createDirectory(path+"Iso")

for view in range(len(viewList)):
	changeView(viewList[view])
	for tmp in list:
		changePart(tmp)
		makeScreenshot(path+viewList[view]+"\\"+tmp)
	for tmp in list:
		addPart(tmp)
	makeScreenshot(path+viewList[view]+"\\"+"All")














	