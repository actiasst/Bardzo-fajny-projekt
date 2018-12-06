sys.path.append("C:\\temp\\skrypty")
sys.path.append("C:\\temp\\skrypty\\materials")
from odbAccess import*
from textRepr import*

odb = openOdb("E:\Abaqus\za duze\explosive_3D_DT_Air_H30_H03-ALE.odb")
#odb = openOdb("C:\\temp\\CantileverBeamJob.odb")
global odb