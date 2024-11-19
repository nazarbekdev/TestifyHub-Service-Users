from PyPDF2 import PdfReader, PdfWriter

"""
    Bu funksiya: bir nechta pdf fayllarni birlashtirib, bitta pdf faylga keltirish uchun qo'llaniladi
    Foydalanish: merge_pdfs(['file1.pdf', 'file2.pdf', 'file3.pdf'], 'merged_file.pdf')
"""


def merge_pdf(input_paths, output_path):
    pdf_writer = PdfWriter()

    for path in input_paths:
        with open(path, 'rb') as file:
            pdf_reader = PdfReader(file)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)
