def answer_form(a, b, c, d):
    form = None
    if a > 20 or b > 20 or c > 20 or d > 20:
        form = 'DCBA'
    elif 10 < a < 21 or 10 < b < 21 or 10 < c < 21 or 10 < d < 21:
        form = 'ACBD'
    elif a < 11 or b < 11 or c < 11 or d < 11:
        form = 'ABCD'
    return form
