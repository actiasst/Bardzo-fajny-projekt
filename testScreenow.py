def viewPlot(plot):
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
    odb = session.odbs['E:/Abaqus/za duze/explosive_3D_DT_Air_H30_H03-ALE.odb']
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



plot1 = "Kinetic energy: ALLKE for Whole Model"
plot2 = "Internal energy: ALLIE for Whole Model"
viewPlot(plot1)
makeScreenshot("jeden")
viewPlot(plot2)
makeScreenshot("dwa")


