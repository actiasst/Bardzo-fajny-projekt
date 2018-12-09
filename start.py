sys.path.append("C:\\temp\\skrypty")
sys.path.append("C:\\temp\\skrypty\\materials")
from odbAccess import*
from textRepr import*

odb = openOdb("E:\Abaqus\za duze\\2D_ECAP_CP_1_290410.odb")
#odb = openOdb("C:\\temp\\CantileverBeamJob.odb")
global odb

#explosive_3D_DT_Air_H30_H03-ALE
#2D_ECAP_CP_1_290410