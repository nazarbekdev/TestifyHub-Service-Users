# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics
#
# # PDF fayl yaratish
# pdf_file = "ruscha_matn.pdf"
# c = canvas.Canvas(pdf_file, pagesize=A4)
#
# # Kirill alifbosi uchun fontni yuklab olish (masalan, Arial)
# pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
#
# # Matn joylashuvi
# c.setFont("Arial", 12)
# ruscha_matn = "Программирование — это искусство решения проблем."
#
# # Matnni PDFga yozish
# c.drawString(100, 750, ruscha_matn)
#
# # PDFni saqlash
# c.save()

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph

# PDF faylini yaratish
file_path = 'ruscha_test.pdf'
doc = SimpleDocTemplate(file_path, pagesize=letter, leftMargin=20, bottomMargin=20, rightMargin=10, topMargin=25)

# Kirill alifbosini qo'llab-quvvatlaydigan fontni ro'yxatdan o'tkazish
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))  # Arial.ttf fontini kerakli yo'ldan yuklang

# Matnlar uchun style yaratish
styles = getSampleStyleSheet()

# Custom Style yaratish (Arial font bilan)
custom_style_ru = ParagraphStyle(
    name='CustomStyle',
    parent=styles['Normal'],
    fontName='Arial',  # Arial fontidan foydalanamiz
    fontSize=12
)

custom_style_en = ParagraphStyle(
    name='CustomStyle',
    parent=styles['Normal'],
    fontName='Times-Roman',  # Times-Roman fontidan foydalanamiz
    fontSize=12
)

# Ruscha matn
ruscha_matn = "Программирование — это искусство решения проблем."
inglizcha_matn = "Hello, guys. What's up."

# Matnni Paragraph orqali yaratish
elements = [Paragraph(ruscha_matn, custom_style_ru), Paragraph(inglizcha_matn, custom_style_en)]

# PDFga yozish
doc.build(elements)
