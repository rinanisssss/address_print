from reportlab.pdfgen import canvas

c = canvas.Canvas("output_file/hello.pdf")
c.setFont("Courier", 80)
c.drawString(100, 100, "Hello World")
c.showPage()
c.setFontSize(40)
c.drawString(100, 100, "Hello World")
c.showPage()
c.save()
