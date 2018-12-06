sys.path.append("C:\\temp\\skrypty")

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image


def generatePDF():
	c = canvas.Canvas("TestPDF.pdf",pagesize=landscape(letter))

	c.setFont('Helvetica',48, leading=None)
	c.drawCentredString(415,500,"Bardzo ladny string")
	c.showPage()
	c.save()
generatePDF()
print "done"