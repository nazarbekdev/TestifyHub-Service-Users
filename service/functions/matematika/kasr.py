from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfgen import canvas

# PDF faylini yaratish
pdf_file = "fraction_example.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)
c = canvas.Canvas(pdf_file, pagesize=letter)

# Kasr matni
fraction_text = "1/2"

# Kasr ustini va tagini joylashtirish
c.drawString(100, 700, "Kasr: ")
c.drawString(100, 680, "1")        # Ustki qismi
c.drawString(100, 660, "2")        # Kasr chizig'i
# c.drawString(100, 640, "2")        # Taglik qismi

# Chizig'ini chizish
c.line(100, 675, 120, 675)  # Kasr chizig'i

# PDFni tugatish
c.save()

print(f"{pdf_file} fayli muvaffaqiyatli yaratildi.")
