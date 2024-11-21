import fitz  # PyMuPDF
import random
from service.functions.qr_code import qr_code_img

"""
    Bu funksiya: DTM muqova faylini shakklantirish uchun qo'llaniladi.
    Qaytadigan qiymatlar: shakllangan muqova.pdf fayl va test kitob raqami.
"""


def placement_of_numbers(subject1, subject2):
    pdf_path = '/Users/uzmacbook/Portfolio/TestifyHub-Service/media/files/files_Cam-Test-Javoblar-varaqasi_UfXAgF0.pdf'
    image_path = '/Users/uzmacbook/Portfolio/TestifyHub-Service/media/files/2024-06-29 08.38.38.jpg'

    pdf_page = fitz.open(pdf_path)
    page = pdf_page[0]
    book_number = str(random.randint(1000000, 5000000))

    first_column = {1: '44.7/376.4', 2: '44.7/393.4', 3: '44.7/410.2', 4: '44.7/427.4', 5: '44.7/444.4',
                    6: '44.7/461.7',
                    7: '44.7/478.8', 8: '44.7/495.4', 9: '44.7/512.5', 0: '44.7/529.8', 'b_n': '40/395.5'}
    second_column = {1: '63.6/376.4', 2: '63.6/393.4', 3: '63.6/410.2', 4: '63.6/427.4', 5: '63.6/444.4',
                     6: '63.6/461.7',
                     7: '63.6/478.8', 8: '63.6/495.4', 9: '63.6/512.5', 0: '63.6/529.8', 'b_n': '58.6/395.5'}
    third_column = {1: '83.4/376.4', 2: '82.4/393.4', 3: '82.4/410.2', 4: '82.4/427.4', 5: '82.4/444.4',
                    6: '82.4/461.7',
                    7: '82.4/478.8', 8: '82.4/495.4', 9: '82.4/512.5', 0: '82.4/529.8', 'b_n': '76.8/395.5'}
    fourth_column = {1: '101.2/376.4', 2: '101.2/393.4', 3: '101.2/410.2', 4: '101.2/427.4', 5: '101.2/444.4',
                     6: '101.2/461.7',
                     7: '101.2/478.8', 8: '101.2/495.4', 9: '101.2/512.5', 0: '101.2/529.8', 'b_n': '95.4/395.5'}
    fifth_column = {1: '119.9/376.4', 2: '119.9/393.4', 3: '119.9/410.2', 4: '119.9/427.4', 5: '119.9/444.4',
                    6: '119.9/461.7',
                    7: '119.9/478.8', 8: '119.9/495.4', 9: '119.9/512.5', 0: '119.9/529.8', 'b_n': '114.4/395.5'}
    sixth_column = {1: '138.5/376.4', 2: '138.5/393.4', 3: '138.5/410.2', 4: '138.5/427.4', 5: '138.5/444.4',
                    6: '138.5/461.7',
                    7: '138.5/478.8', 8: '138.5/495.4', 9: '138.5/512.5', 0: '138.5/529.8', 'b_n': '133/395.5'}
    seventh_column = {1: '157.2/376.4', 2: '157.2/393.4', 3: '157.2/410.2', 4: '157.2/427.4', 5: '157.2/444.4',
                      6: '157.2/461.7',
                      7: '157.2/478.8', 8: '157.2/495.4', 9: '157.2/512.5', 0: '157.2/529.8', 'b_n': '152/395.5'}

    for i in range(7):
        if i == 0:
            book_num = int(book_number[i])
            x = float(first_column[book_num].split('/')[0])
            y = float(first_column[book_num].split('/')[1])

            x1 = float(first_column['b_n'].split('/')[0])
            y1 = float(first_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 43, x + 51, y + 60)

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 1:
            book_num = int(book_number[i])
            x = float(second_column[book_num].split('/')[0])
            y = float(second_column[book_num].split('/')[1])

            x1 = float(second_column['b_n'].split('/')[0])
            y1 = float(second_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 43, x + 51, y + 60)

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 2:
            book_num = int(book_number[i])
            x = float(third_column[book_num].split('/')[0])
            y = float(third_column[book_num].split('/')[1])

            x1 = float(third_column['b_n'].split('/')[0])
            y1 = float(third_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 43, x + 51, y + 60)

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 3:
            book_num = int(book_number[i])
            x = float(fourth_column[book_num].split('/')[0])
            y = float(fourth_column[book_num].split('/')[1])

            x1 = float(fourth_column['b_n'].split('/')[0])
            y1 = float(fourth_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 43, x + 51, y + 60)

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 4:
            book_num = int(book_number[i])
            x = float(fifth_column[book_num].split('/')[0])
            y = float(fifth_column[book_num].split('/')[1])

            x1 = float(fifth_column['b_n'].split('/')[0])
            y1 = float(fifth_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 43, x + 51, y + 60)

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 5:
            book_num = int(book_number[i])
            x = float(sixth_column[book_num].split('/')[0])
            y = float(sixth_column[book_num].split('/')[1])

            x1 = float(sixth_column['b_n'].split('/')[0])
            y1 = float(sixth_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 43, x + 51, y + 60)

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 6:
            book_num = int(book_number[i])
            x = float(seventh_column[book_num].split('/')[0])
            y = float(seventh_column[book_num].split('/')[1])

            x1 = float(seventh_column['b_n'].split('/')[0])
            y1 = float(seventh_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 43, x + 51, y + 60)

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        else:
            print('Xatolik bor!!!')

    x = 110
    y = 168.6

    x1 = 140
    y1 = -20

    x2 = 390
    y2 = 377.5
    y3 = 397.5
    y4 = 416.5

    x5 = 325
    y5 = 548
    rect = fitz.Rect(x, y, x + 200, y + 50)
    page.insert_textbox(rect, book_number, fontsize=16, fill=(0, 0, 0))

    qr_code_image = qr_code_img(book_number)
    rect = fitz.Rect(x1 - 70, y1 + 50, x1 + 40, y1 + 150)

    rect1 = fitz.Rect(x2, y2, x2 + 200, y2 + 50)
    page.insert_textbox(rect1, 'Majburiy fanlar', fontsize=14, fill=(0, 0, 0), fontname="helv")

    rect1 = fitz.Rect(x2, y3, x2 + 200, y2 + 50)
    page.insert_textbox(rect1, subject1, fontsize=14, fill=(0, 0, 0), fontname="helv")

    rect2 = fitz.Rect(x2, y4, x2 + 200, y3 + 50)
    page.insert_textbox(rect2, subject2, fontsize=14, fill=(0, 0, 0), fontname="helv")

    rect3 = fitz.Rect(370, 675, x5 + 200, 700 + 150)
    page.insert_textbox(rect3, 'uz.camtest.app', fontsize=14, fill=(0, 0, 0), fontname="helv")

    rect_apk = fitz.Rect(x5 - 25, y5 + 90, x5 + 40, y5 + 150)

    image_apk_path = '/Users/uzmacbook/Portfolio/TestifyHub-Service/media/files/qr_code_apk.png'

    page.insert_image(rect_apk, filename=image_apk_path)
    page.insert_image(rect, filename=qr_code_image)

    pdf_page.save('/Users/uzmacbook/Portfolio/TestifyHub-Service/media/files/muqova.pdf')
    pdf_page.close()

    result = ['/Users/uzmacbook/Portfolio/TestifyHub-Service/media/files/muqova.pdf', book_number]

    return result
