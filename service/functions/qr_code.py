import qrcode


"""
    Bu funksiya: DTM test kitobi raqami uchun QR-Code yaratish uchun.
    Qaytadigan qiymat: qr-code.png [rasm]
"""


def qr_code_img(book_number):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(book_number)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qr_code_apk.png')
    return 'qr_code_apk.png'
