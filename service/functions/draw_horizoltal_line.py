import fitz


def draw_horizontal_line(pdf_path, output_path, book_code):
    # PDF faylni ochish
    pdf_doc = fitz.open(pdf_path)

    # Har bir sahifada chiziq chizish
    for page_number in range(pdf_doc.page_count):
        # Sahifani olish
        page = pdf_doc.load_page(page_number)

        # Sahifa o'lchamini olish
        width = page.rect.width
        height = page.rect.height

        # Chiziqni chizish uchun qalamni yaratish
        line_color = (0, 0, 0)  # RGB rang (qora)
        line_width = 1  # Chiziq eni

        # Yuqori chiziq
        horiz_line_start_top = (14, 15)
        horiz_line_end_top = (width - 15, 16)
        page.draw_line(horiz_line_start_top, horiz_line_end_top, color=line_color, width=line_width)

        # Sahifalarga kitob raqamini yozish
        page_number_text = book_code
        page.insert_text((20, 12), page_number_text, fontsize=10, color=line_color)

        # Cam Test
        text = 'TestifyHub'
        page.insert_text((width - 60, 12), text, fontsize=10, color=line_color)

        # Talabalik sari olg'a!
        page_text = "Biz bilan yanada osonroq!"
        page.insert_text((width / 2 - 40, 12), page_text, fontsize=10, color=line_color)

        # O'rtasidan vertikal chiziq
        vert_line_start = (width / 2, 25)
        vert_line_end = (width / 2, height - 15)
        page.draw_line(vert_line_start, vert_line_end, color=line_color, width=line_width)

    # Yangi PDF faylni saqlash
    pdf_doc.save(output_path)

    # PDF faylni yopish
    pdf_doc.close()
