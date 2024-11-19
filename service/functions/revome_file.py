import os

""""
    Bu funksiya: fayllarni joylashgan muhitdan o'chirish uchun.
    Qaytadigan qiymat: 'qiymat qaytmaydi'
"""


def revome_file(files):
    for file in files:
        os.remove(file)
