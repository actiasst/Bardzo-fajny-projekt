sys.path.append("C:\\temp\\skrypty")

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import portrait
from reportlab.platypus import Image

def generatePDF(list):
	pageNumber = 1
	beggining = 50
	fontSize = 14
	newLine = fontSize + 4
	c = canvas.Canvas("skrypty\\TestPDF.pdf",pagesize=portrait(A4),bottomup=0)
	c.setFont('Helvetica',fontSize, leading=None)
	for tmp in range(len(list)):
		if beggining >= 765:
			c.drawCentredString(300,800,"- " + str(pageNumber) + " -")
			pageNumber += 1
			c.showPage()
			beggining = 50
			c.setFont('Helvetica',fontSize, leading=None)
		c.drawString(50,beggining,list[tmp])
		beggining += newLine
	c.drawCentredString(300,800,"- " + str(pageNumber) + " -")
	c.showPage()
	c.save()
	print "done"