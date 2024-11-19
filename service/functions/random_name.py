import random
import string

"""
    Bu funksiya: Random holatda nom generatsiya qilish uchun. 
    Bu funksiyadan foydalanuvchi generatsiya qilgan pdf fileni nomlash uchun foydalanamiz.
    Qaytadigan qiymat: str turida -> ixtiyoriy nom: [ drrpctjr ]
"""


def generate_random_name(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
