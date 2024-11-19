# from sympy import symbols, Integral
# from sympy.printing.latex import latex
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import cm
#
# x = symbols('x')
# integral_expr = Integral(x**2, x)
# integral_latex = latex(integral_expr)
#
# # PDF fayl yaratish
# c = canvas.Canvas("math.pdf")
# c.drawString(100, 750, f"Matematik amal: {integral_latex}")
# c.showPage()
# c.save()



import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Matplotlib yordamida matematik amal yaratish
fig, ax = plt.subplots()
ax.text(0.5, 0.5, r"$\int x^{3} \, dx$", fontsize=20, ha='center')
ax.axis('off')
plt.savefig('integral.png', bbox_inches='tight')

# ReportLab bilan PDF yaratish
c = canvas.Canvas("test.pdf", pagesize=letter)
c.drawImage("integral.png", 100, 700, width=200, height=100)
c.showPage()
c.save()
