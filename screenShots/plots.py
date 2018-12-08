list = odb.steps.keys()
odbNameTmp = odb.name

plotsList = []

for tmp in list:
	try:
		test = odb.steps[tmp].name
		print "STEP: "
		print odb.steps[tmp].name
		list2 = odb.steps[tmp].historyRegions.keys()
		for tmp2 in list2:
			try:
				test = odb.steps[tmp].historyRegions[tmp2].name
				print "HISTORY REGIONS: "
				print odb.steps[tmp].historyRegions[tmp2].name
				list3 = odb.steps[tmp].historyRegions[tmp2].historyOutputs.keys()
				for tmp3 in list3:
					try:
						test = odb.steps[tmp].historyRegions[tmp2].historyOutputs[tmp3].name
						tmpString = str(odb.steps[tmp].historyRegions[tmp2].historyOutputs[tmp3].description)
						tmpString += ": "
						tmpString += str(odb.steps[tmp].historyRegions[tmp2].historyOutputs[tmp3].name)
						tmpString += " for Whole Model" ###EWENTUALNIE DO ZMIANY JAK SIE OKAZE ZE JEST WIECEJ
						plotsList.append(tmpString)
					except AttributeError:
						strangeVariable = 0
			except AttributeError:
				strangeVariable = 0
		print " "
	except AttributeError:
		strangeVariable = 0

def viewPlot(plot,odbName):
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
    odb = session.odbs[odbName]
    xy1 = xyPlot.XYDataFromHistory(odb=odb, 
        outputVariableName=plot, 
        suppressQuery=True, __linkedVpName__='Viewport: 1')
    c1 = session.Curve(xyData=xy1)
    xyp = session.xyPlots['XYPlot-1']
    chartName = xyp.charts.keys()[0]
    chart = xyp.charts[chartName]
    chart.setValues(curvesToPlot=(c1, ), )
    session.viewports['Viewport: 1'].setValues(displayedObject=xyp)

def makeScreenshot(plot):
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
    session.printToFile(fileName='C:/temp/skrypty/allScreens/' + plot, format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

for tmp in range(len(plotsList)):
	viewPlot(plotsList[tmp],odbNameTmp)
	makeScreenshot(str(tmp))




















