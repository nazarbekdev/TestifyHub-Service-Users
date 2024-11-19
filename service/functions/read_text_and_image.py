import os
import string
import random
from pypdf import PdfReader

"""
    Bu   test_pdf_read_text   funksiya pdf fayldagi text larni o'qib olish va kerakli natijani qaytarish uchun.
    Qaytadigan qiymat: list 
    
    Bu   test_pdf_read_image  funksiya pdf fayldagi rasmlarni o'qib olish va media/images ga saqlab olish uchun.
    Qaytadigan qiymat: list
"""


def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))


def test_pdf_read_text(document_url):
    reader = PdfReader(document_url)
    text = ''
    for i in range(len(reader.pages)):
        text += reader.pages[i].extract_text()

    text_list = []
    for i in text.split('#'):
        text_list.append(i.strip())

    images_in_test = []
    no_images_in_test = []
    for i in text_list[1:]:
        if '@' in i.split('//')[0]:
            images_in_test.append(i)
        else:
            no_images_in_test.append(i)
    data = images_in_test + no_images_in_test
    return data


def test_pdf_read_image(document_url):
    reader = PdfReader(document_url)
    image_data = []
    existing_images = set()

    for filename in os.listdir("media/images"):
        if filename.endswith(('.jpg', '.png', '.jpeg', '.bmp', '.tiff')):
            existing_images.add(filename)

    for i in range(0, len(reader.pages)):
        page = reader.pages[i]
        for j in page.images:
            rdn = generate_random_string(10)
            image_filename = f"media/images/{rdn}{os.path.splitext(j.name)[1]}"
            while image_filename in existing_images:
                image_filename = f"media/images/{rdn}{os.path.splitext(j.name)[1]}"
            with open(image_filename, 'wb') as fl:
                fl.write(j.data)
                image_data.append(image_filename)
    return image_data
