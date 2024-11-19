from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
# PDF faylini yaratish
doc = SimpleDocTemplate("integrals_paragraph.pdf", pagesize=letter)
font_path = os.path.join(os.path.dirname(__file__), 'DejaVuSans.ttf')
# Matn uslublarini olish
styles = getSampleStyleSheet()
style = styles['Normal']

# Integral belgilarini yaratish
integrals_text = (
    "Asosiy integral: ∫<br/>"
    "Ikki marta integral: ∫∫<br/>"
    "Kontur integral: ∮<br/>"
    "Limit: lim (x → 0) f(x) = ∞"
)

# Paragraph yaratish
paragraph = Paragraph(integrals_text, style)

# PDFga qo'shish
doc.build([paragraph])
