# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import SimpleDocTemplate, Paragraph
#
# # Unicode almashtirish
# greeks = {'alpha': u'\u03b1'}  # GREEK SMALL LETTER ALPHA
#
# # Test matn
# text = "a alpha"
#
# # Agar text 'alpha' bo'lsa, uni α ga almashtiramiz
# if text in greeks:
#     text = text.replace('alpha', greeks['alpha'])
#
# # PDF faylni yaratish
# doc = SimpleDocTemplate("greek_test.pdf")
# styles = getSampleStyleSheet()
# flowables = []
#
# # Paragraph ichida yunoncha harfni ishlatamiz
# flowables.append(Paragraph(f"The Greek small gamma: \u03b3 and small alpha: \u03b1", styles['Normal']))
#
# # PDFni yaratish
# doc.build(flowables)
#
# # text = 'Salom dunyo, a alpha'
# # print(text.replace('alpha', greeks['alpha']))

#
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import Paragraph, SimpleDocTemplate
#
# doc = SimpleDocTemplate("example.pdf")
# styles = getSampleStyleSheet()
#
# story = []
#
# # Paragraph ichida yangi qator uchun <br/> ishlatiladi
# text = "Bu birinchi qator.<br/>Bu yangi qator."
# p = Paragraph(text, styles["Normal"])
# story.append(p)
#
# doc.build(story)

import logging
from datetime import datetime
logging.basicConfig(filename='app.log', level=logging.ERROR)

try:
    with open('file_does_not_exist.txt') as f:
        contents = f.read()
except Exception as e:
    logging.error(f"Xato[{datetime.now().strftime('%d.%m.%y | %H:%M:%S')}]: {e}")
