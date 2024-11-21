import os, ast
import random
from datetime import datetime
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, Frame, Spacer, Image, PageTemplate, BaseDocTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from service.functions.answer_form import answer_form
from service.functions.draw_horizoltal_line import draw_horizontal_line
from service.functions.merge_pdf import merge_pdf
from service.functions.mother_and_english_languages_form import mother_and_english_languages_form
from service.functions.placement_of_numbers import placement_of_numbers
from service.functions.revome_file import revome_file
from service.models import Question, Subject, AnswerTest, UserFile, ServiceUser, GenerateTestData, Language, Key, TestControl
from service.serializers import TestGeneratePDFSerializer
from dotenv import load_dotenv

load_dotenv()

"""
    Bu Api foydalanuvchi tomonidan talab qilingan fanlan majmuasi uchun test generatsiya qilish uchun.
"""

project_path = os.getenv('PROJECT_PATH')

# Matnlar uchun yozuv turi
styles = getSampleStyleSheet()
custom_style = ParagraphStyle(name='CustomStyle', parent=styles['Normal'], fontName='Times-Roman', fontSize=12, leading=15)
custom_style.spaceAfter = 1

# Fanlar uchun Qalin yozuv
centered_style_bold = ParagraphStyle(name='CenteredStyleBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=14, alignment=1)


class GenerateTestDefaultKey(GenericAPIView):
    serializer_class = TestGeneratePDFSerializer

    def add_subject_heading(self, elements, subject_name):
        centered_style = ParagraphStyle(name='CenteredStyle', parent=styles['Title'], alignment=1)
        elements.append(Paragraph(subject_name, centered_style_bold))
        elements.append(Spacer(1, 10))

    def build_pdf(self, file_path, elements):
        # PDF faylini yaratish va sahifa shablonini qo'llash
        pdf = BaseDocTemplate(file_path, pagesize=letter, leftMargin=20, bottomMargin=20, rightMargin=10, topMargin=25)

        # Sahifa shabloni
        frame1 = Frame(pdf.leftMargin, pdf.bottomMargin, pdf.width / 2 - 6, pdf.height, id='col1')
        frame2 = Frame(pdf.width / 2 + 30, pdf.bottomMargin, pdf.width / 2 - 6, pdf.height, id='col2')
        template = PageTemplate(id='twoColumn', frames=[frame1, frame2])

        pdf.addPageTemplates([template])
        pdf.build(elements)

    def get_test_questions(self, language, database_type, subject_id, subject):
        all_tests = []
        for index, value in enumerate(subject):
            if value['category_id'] not in (72, 73, 74, 75):  # O'zgaradi !!!
                tests = list(Question.objects.filter(language_id=language, database_type_id=database_type,
                                                     subject_id=subject_id,
                                                     subject_category_id=value['category_id']).order_by('?')[
                             :value['question_limit']])
                all_tests.extend(tests)
        return all_tests

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # POST requestdan datalarni olish
        subject1 = serializer.data['subject1']
        subject2 = serializer.data['subject2']
        database_type = serializer.data['database_type']
        language = serializer.data['language']
        number_books = serializer.data['number_books']
        user = serializer.data['user']

        # Kitobchalar sonini musbatlikka tekshirish
        if number_books < 1:
            return Response({'error': 'Number books cannot be negative or zero'}, status=400)

        # user limitini olish
        user_limit = ServiceUser.objects.get(id=user)

        # User limitini tekshirish
        if user_limit.limit >= number_books:
            user_limit.limit -= number_books
            user_limit.save()
        else:
            return Response({'success': False, 'message': 'Sizda yetarlicha limit mavjud emas!'}, status=400)
        try:
            # Majburiy fanlar id raqamini olish
            maj_fan1 = Subject.objects.get(name='Majburiy Ona tili').id
            maj_fan2 = Subject.objects.get(name='Majburiy Matematika').id
            maj_fan3 = Subject.objects.get(name="Majburiy O'zbekiston tarixi").id

            # Asosiy FAN1 va FAN2 uchun filterlandagan savollar limitini olish
            obj1 = TestControl.objects.filter(subject=subject1).values()
            obj2 = TestControl.objects.filter(subject=subject2).values()

            # Majburiy fanlar uchun filterlangan savollarni olish
            obj3 = TestControl.objects.filter(subject=maj_fan1).values()
            obj4 = TestControl.objects.filter(subject=maj_fan2).values()
            obj5 = TestControl.objects.filter(subject=maj_fan3).values()

            # Asosiy fanlar nomini olish
            subject_name1 = Subject.objects.get(pk=subject1).name
            subject_name2 = Subject.objects.get(pk=subject2).name
            language_name = Language.objects.get(pk=language).name
        except Subject.DoesNotExist as e:
            return Response({'error': str(e)}, status=400)

        # Barcha generatsiya testlarni yozish uchun pdf file ochish
        file_path = 'subject_test.pdf'

        # Katta matli savol uchun
        matnli, fan1, fan2 = False, False, False

        # Katta matnli savol boshlanish index
        start_matnli_1, start_matnli_2 = 0, 0

        # Asosiy fanlar uchun savollarni tugash chegarasi
        first_sub_end, second_sub_end = 61, 91

        # Katta matnli savollarni olish
        if subject_name1 in ("ONA TILI VA ADABIYOT", "INGLIZ TILI", "FRANSUZ TILI", "NEMIS TILI"):  # Talabga qarab o'zgaradi !!!
            if subject_name1 == 'ONA TILI VA ADABIYOT':
                sub_cat = 72  # o'zgaradi !!!
            elif subject_name1 == 'INGLIZ TILI':
                sub_cat = 75  # o'zgaradi !!!
            elif subject_name1 == 'FRANSUZ TILI':
                sub_cat = 74  # o'zgaradi !!!
            elif subject_name1 == 'NEMIS TILI':
                sub_cat = 73  # o'zgaradi !!!
            sub_question = list(Question.objects.filter(language_id=language, database_type_id=database_type,
                                                 subject_id=subject1,
                                                 subject_category_id=sub_cat).order_by('?')[:1])
            tests_subject1, question_quantity1 = mother_and_english_languages_form(sub_question[0].question)
            start_matnli_1 = 61 - question_quantity1  # 61
            first_sub_end = start_matnli_1 + 1
            matnli, fan1 = True, True

        if subject_name2 in ("ONA TILI VA ADABIYOT", "INGLIZ TILI", "FRANSUZ TILI", "NEMIS TILI"):  # Talabga qarab o'zgaradi !!!
            if subject_name2 == 'ONA TILI VA ADABIYOT':
                sub_cat = 72  # o'zgaradi !!!
            elif subject_name2 == 'INGLIZ TILI':
                sub_cat = 75  # o'zgaradi !!!
            elif subject_name2 == 'FRANSUZ TILI':
                sub_cat = 74  # o'zgaradi !!!
            elif subject_name2 == 'NEMIS TILI':
                sub_cat = 73  # o'zgaradi !!!
            sub_question = list(Question.objects.filter(language_id=language, database_type_id=database_type,
                                                             subject_id=subject2,
                                                             subject_category_id=sub_cat).order_by('?')[:1])
            tests_subject2, question_quantity2 = mother_and_english_languages_form(sub_question[0].question)
            start_matnli_2 = 91 - question_quantity2  # 91
            second_sub_end = start_matnli_2 + 1
            matnli, fan2 = True, True

        # Savollar tartib raqami
        numbering_ranges = [range(1, 11), range(11, 21), range(21, 31), range(31, first_sub_end), range(61, second_sub_end)]

        elements = []
        all_tests = []

        # default key lar
        keys = Key.objects.order_by('id').first().keys
        keys = ast.literal_eval(keys)

        # Kitoblar soni bo'yicha generatsiya qilish
        for num in range(number_books):
            # Asosiy fanlar uchun savollar to'plamini olish
            all_tests1 = self.get_test_questions(language, database_type, subject1, obj1)
            all_tests2 = self.get_test_questions(language, database_type, subject2, obj2)
            maj_ona_tili = self.get_test_questions(language, database_type, maj_fan1, obj3)
            maj_matem = self.get_test_questions(language, database_type, maj_fan2, obj4)
            maj_tarix = self.get_test_questions(language, database_type, maj_fan3, obj5)

            # Savollarni random qilish
            random.shuffle(all_tests1)
            random.shuffle(all_tests2)
            random.shuffle(maj_ona_tili)
            random.shuffle(maj_matem)
            random.shuffle(maj_tarix)

            # Fanlar uz-ru variant
            subjects_dict = {
                'Biologiya': 'Биология',
                'Tarix': 'История',
                'Fizika': 'Физика',
                'Matematika': 'Математика',
                'Kimyo': 'Химия',
                'Ona tili': 'Родной язык',
                'Geografiya': 'География',
                'Huquq': 'Юридическая наука',
                'Rus tili': 'Русский язык',
                'Ingliz tili': 'Ingliz tili',
                'Nemis tili': 'Nemis tili',
                'Fransuz tili': 'Fransuz tili'
            }

            if matnli and fan1:
                all_tests1 = all_tests1[:31-question_quantity1]
            if matnli and fan2:
                all_tests2 = all_tests2[:31-question_quantity2]

            if language == 1:
                # PDF filega fanlar nomini yozish
                subject_list = ['Ona tili', 'Matematika', "O'zbekiston tarixi", subject_name1, subject_name2]
                subjects = [maj_ona_tili, maj_matem, maj_tarix, all_tests1, all_tests2]

                elements.append(Paragraph('Majburiy Fanlar', centered_style_bold))
                elements.append(Spacer(1, 8))
            else:
                # PDF filega fanlar nomini yozish
                subject_name1 = subjects_dict[subject_name1]
                subject_name2 = subjects_dict[subject_name2]
                subject_list = ['Родной язык', 'Математика', 'История', subject_name1, subject_name2]
                subjects = [maj_ona_tili, maj_matem, maj_tarix, all_tests1, all_tests2]

                elements.append(Paragraph('Обязательные науки', centered_style_bold))
                elements.append(Spacer(1, 8))
            try:
                # Asosiy generatsiya qismi
                for subject_name, tests, numbering_range in zip(subject_list, subjects, numbering_ranges):
                    self.add_subject_heading(elements, subject_name)

                    for i, test in enumerate(tests):
                        # Matnli savol bo'lsa
                        if matnli and numbering_range[i] == start_matnli_1 or numbering_range[i] == start_matnli_2:
                            # Matnli savollarni joylashtirish uchun tartib raqamni tanlash
                            if numbering_range[i] > 61:
                                start_matnli = start_matnli_2
                                tests_subject = tests_subject2
                            else:
                                start_matnli = start_matnli_1
                                tests_subject = tests_subject1

                            question_txt = tests_subject[0]['question']
                            elements.append(Spacer(1, 5))
                            elements.append(Paragraph(question_txt, custom_style))

                            for test in tests_subject[1:]:
                                t = test['question']
                                text_test = f"{start_matnli}. {t}"
                                elements.append(Spacer(1, 5))
                                elements.append(Paragraph(text_test, custom_style))
                                answers_ = test['answers']
                                answer = test['answer']

                                answers = []
                                for ans in answers_[1:]:
                                    answers.append(ans)

                                random.shuffle(answers)
                                # Javob Formasini tanlash
                                form = answer_form(len(answers[0]), len(answers[1]),
                                                   len(answers[2]), len(answer))

                                ind = start_matnli-1
                                key = str(start_matnli)

                                if keys[ind][key] == 'A':
                                    if form == 'ABCD':
                                        elements.append(Spacer(1, 2))
                                        elements.append(Paragraph(
                                            f"A) {answer}&nbsp;&nbsp;&nbsp;&nbsp; B) {answers[0]}&nbsp;&nbsp;&nbsp;&nbsp; C) {answers[1]}&nbsp;&nbsp;&nbsp;&nbsp; D) {answers[2]}",
                                            custom_style))
                                    elif form == 'ACBD':
                                        elements.append(Spacer(1, 2))
                                        elements.append(
                                            Paragraph(f"A) {answer} &nbsp;&nbsp;&nbsp;&nbsp; B) {answers[1]}",
                                                      custom_style))
                                        elements.append(
                                            Paragraph(
                                                f"C) {answers[0]}&nbsp;&nbsp;&nbsp;&nbsp;  D) {answers[2]}",
                                                custom_style))
                                    elif form == 'DCBA':
                                        elements.append(Spacer(1, 2))
                                        elements.append(Paragraph(f"A) {answer}", custom_style))
                                        elements.append(Paragraph(f"B) {answers[1]}", custom_style))
                                        elements.append(Paragraph(f"C) {answers[2]}", custom_style))
                                        elements.append(Paragraph(f"D) {answers[0]}", custom_style))
                                elif keys[ind][key] == 'B':
                                    if form == 'ABCD':
                                        elements.append(Spacer(1, 2))
                                        elements.append(Paragraph(
                                            f"A) {answers[0]}&nbsp;&nbsp;&nbsp;&nbsp; B) {answer}&nbsp;&nbsp;&nbsp;&nbsp; C) {answers[1]} &nbsp;&nbsp;&nbsp;&nbsp;D) {answers[2]}",
                                            custom_style))
                                    elif form == 'ACBD':
                                        elements.append(Spacer(1, 2))
                                        elements.append(
                                            Paragraph(
                                                f"A) {answers[0]}&nbsp;&nbsp;&nbsp;&nbsp;  B) {answer}",
                                                custom_style))
                                        elements.append(
                                            Paragraph(f"C) {answers[2]} &nbsp;&nbsp;&nbsp;&nbsp; D) {answers[1]}",
                                                      custom_style))
                                    elif form == 'DCBA':
                                        elements.append(Spacer(1, 2))
                                        elements.append(Paragraph(f"A) {answers[0]}", custom_style))
                                        elements.append(Paragraph(f"B) {answer}", custom_style))
                                        elements.append(Paragraph(f"C) {answers[1]}", custom_style))
                                        elements.append(Paragraph(f"D) {answers[2]}", custom_style))
                                elif keys[ind][key] == 'C':
                                    if form == 'ABCD':
                                        elements.append(Spacer(1, 2))
                                        elements.append(Paragraph(
                                            f"A) {answers[0]}&nbsp;&nbsp;&nbsp;&nbsp; B) {answers[1]}&nbsp;&nbsp;&nbsp;&nbsp; C) {answer}&nbsp;&nbsp;&nbsp;&nbsp; D) {answers[2]}",
                                            custom_style))
                                    elif form == 'ACBD':
                                        elements.append(Spacer(1, 2))
                                        elements.append(
                                            Paragraph(f"A) {answers[0]} &nbsp;&nbsp;&nbsp;&nbsp;  B) {answers[1]}",
                                                      custom_style))
                                        elements.append(
                                            Paragraph(
                                                f"C) {answer} &nbsp;&nbsp;&nbsp;&nbsp; D) {answers[2]}",
                                                custom_style))
                                    elif form == 'DCBA':
                                        elements.append(Spacer(1, 2))
                                        elements.append(Paragraph(f"A) {answers[0]}", custom_style))
                                        elements.append(Paragraph(f"B) {answers[1]}", custom_style))
                                        elements.append(Paragraph(f"C) {answer}", custom_style))
                                        elements.append(Paragraph(f"D) {answers[2]}", custom_style))
                                elif keys[ind][key] == 'D':
                                    if form == 'ABCD':
                                        elements.append(Spacer(1, 2))
                                        elements.append(Paragraph(
                                            f"A) {answers[0]} &nbsp;&nbsp;&nbsp;&nbsp;B) {answers[1]}&nbsp;&nbsp;&nbsp;&nbsp; C) {answers[2]}&nbsp;&nbsp;&nbsp;&nbsp; D) {answer}",
                                            custom_style))
                                    elif form == 'ACBD':
                                        elements.append(Spacer(1, 2))
                                        elements.append(
                                            Paragraph(
                                                f"A) {answers[0]}&nbsp;&nbsp;&nbsp;&nbsp;  B) {answers[2]}",
                                                custom_style))
                                        elements.append(
                                            Paragraph(f"C) {answers[1]} &nbsp;&nbsp;&nbsp;&nbsp; D) {answer}",
                                                      custom_style))
                                    elif form == 'DCBA':
                                        elements.append(Spacer(1, 2))
                                        elements.append(Paragraph(f"A) {answers[0]}", custom_style))
                                        elements.append(Paragraph(f"B) {answers[1]}", custom_style))
                                        elements.append(Paragraph(f"C) {answers[2]}", custom_style))
                                        elements.append(Paragraph(f"D) {answer}", custom_style))
                                else:
                                    elements.append(Spacer(1, 3))
                                    elements.append(Paragraph(f"None"))
                                start_matnli += 1
                                i += 1
                        elif test.answers != '?':

                            ind = numbering_range[i] - 1
                            key = str(numbering_range[i])

                            test_text = f"{numbering_range[i]}. {test.question.replace('@', '')}\n\n" if '@' in test.question else f"{numbering_range[i]}. {test.question}\n\n"
                            elements.append(Spacer(1, 5))
                            elements.append(Paragraph(test_text, custom_style))

                            if test.image:
                                test_image = Image(f'{project_path}/media/{test.image}', width=120, height=70)
                                elements.append(Spacer(1, 10))
                                elements.append(test_image)
                                elements.append(Spacer(1, 15))

                            tests_ = test.answers
                            answer_ = test.answer
                            answer = answer_.replace('\n', '')
                            answers_lst1 = []

                            shuffled_answers = tests_.split('#')

                            for k in shuffled_answers[1:]:
                                answers_lst1.append(k)

                            answers_lst = random.sample(answers_lst, 3)

                            # Javob Formasini tanlash
                            form = answer_form(len(answer), len(answers_lst1[0]), len(answers_lst1[1]),
                                               len(answers_lst1[2]))

                            if keys[ind][key] == 'A':
                                if form == 'ABCD':
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(
                                        f"A) {answer}&nbsp;&nbsp;&nbsp;&nbsp; B) {answers_lst[0]}&nbsp;&nbsp;&nbsp;&nbsp; C) {answers_lst[1]}&nbsp;&nbsp;&nbsp;&nbsp; D) {answers_lst[2]}",
                                        custom_style))
                                elif form == 'ACBD':
                                    elements.append(Spacer(1, 2))
                                    elements.append(
                                        Paragraph(f"A) {answer} &nbsp;&nbsp;&nbsp;&nbsp; B) {answers_lst[1]}",
                                                  custom_style))
                                    elements.append(
                                        Paragraph(f"C) {answers_lst[0]} &nbsp;&nbsp;&nbsp;&nbsp; D) {answers_lst[2]}",
                                                  custom_style))
                                elif form == 'DCBA':
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(f"A) {answer}", custom_style))
                                    elements.append(Paragraph(f"B) {answers_lst[0]}", custom_style))
                                    elements.append(Paragraph(f"C) {answers_lst[1]}", custom_style))
                                    elements.append(Paragraph(f"D) {answers_lst[2]}", custom_style))

                            elif keys[ind][key] == 'B':
                                if form == 'ABCD':
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(
                                        f"A) {answers_lst[0]}&nbsp;&nbsp;&nbsp;&nbsp; B) {answer}&nbsp;&nbsp;&nbsp;&nbsp; C) {answers_lst[1]}&nbsp;&nbsp;&nbsp;&nbsp; D) {answers_lst[2]}",
                                        custom_style))
                                elif form == 'ACBD':
                                    elements.append(Spacer(1, 2))
                                    elements.append(
                                        Paragraph(f"A) {answers_lst[0]}&nbsp;&nbsp;&nbsp;&nbsp;  B) {answer}",
                                                  custom_style))
                                    elements.append(
                                        Paragraph(f"C) {answers_lst[1]}&nbsp;&nbsp;&nbsp;&nbsp;  D) {answers_lst[2]}",
                                                  custom_style))
                                elif form == 'DCBA':
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(f"A) {answers_lst[0]}", custom_style))
                                    elements.append(Paragraph(f"B) {answer}", custom_style))
                                    elements.append(Paragraph(f"C) {answers_lst[1]}", custom_style))
                                    elements.append(Paragraph(f"D) {answers_lst[2]}", custom_style))

                            elif keys[ind][key] == 'C':
                                if form == 'ABCD':
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(
                                        f"A) {answers_lst[0]} &nbsp;&nbsp;&nbsp;&nbsp; B) {answers_lst[1]} &nbsp;&nbsp;&nbsp;&nbsp; C) {answer} &nbsp;&nbsp;&nbsp;&nbsp; D) {answers_lst[2]}",
                                        custom_style))
                                elif form == 'ACBD':
                                    elements.append(Spacer(1, 2))
                                    elements.append(
                                        Paragraph(f"A) {answers_lst[0]} &nbsp;&nbsp;&nbsp;&nbsp;  B) {answers_lst[1]}",
                                                  custom_style))
                                    elements.append(
                                        Paragraph(f"C) {answer} &nbsp;&nbsp;&nbsp;&nbsp;  D) {answers_lst[2]}",
                                                  custom_style))
                                elif form == 'DCBA':
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(f"A) {answers_lst[0]}", custom_style))
                                    elements.append(Paragraph(f"B) {answers_lst[1]}", custom_style))
                                    elements.append(Paragraph(f"C) {answer}", custom_style))
                                    elements.append(Paragraph(f"D) {answers_lst[2]}", custom_style))

                            elif keys[ind][key] == 'D':
                                if form == 'ABCD':
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(
                                        f"A) {answers_lst[0]}&nbsp;&nbsp;&nbsp;&nbsp; B) {answers_lst[1]}&nbsp;&nbsp;&nbsp;&nbsp; C) {answers_lst[2]}&nbsp;&nbsp;&nbsp;&nbsp; D) {answer}",
                                        custom_style))
                                elif form == 'ACBD':
                                    elements.append(Spacer(1, 2))
                                    elements.append(
                                        Paragraph(f"A) {answers_lst[0]}&nbsp;&nbsp;&nbsp;&nbsp;  B) {answers_lst[2]}",
                                                  custom_style))
                                    elements.append(
                                        Paragraph(f"C) {answers_lst[1]}&nbsp;&nbsp;&nbsp;&nbsp;  D) {answer}",
                                                  custom_style))
                                elif form == 'DCBA':
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(f"A) {answers_lst[0]}", custom_style))
                                    elements.append(Paragraph(f"B) {answers_lst[1]}", custom_style))
                                    elements.append(Paragraph(f"C) {answers_lst[2]}", custom_style))
                                    elements.append(Paragraph(f"D) {answer}", custom_style))

                            else:
                                elements.append(Spacer(1, 3))
                                elements.append(Paragraph(f"None"))
                        else:
                            test_text = f"{numbering_range[i]}."
                            elements.append(Spacer(1, 3))
                            elements.append(Paragraph(test_text, custom_style))
                            elements.append(Spacer(1, 5))
                            test_image = Image(f'{project_path}/{test.image}', width=200,
                                               height=120)
                            elements.append(test_image)
                            elements.append(Spacer(1, 10))

                    elements.append(Spacer(1, 20))
            except Exception as e:
                return Response({'error': str(e)}, status=400)

            # Ikki kolonka faylni yaratish
            self.build_pdf(file_path, elements)

            data_muqova = placement_of_numbers(subject_name1, subject_name2)
            muqova = data_muqova[0]
            book_code = data_muqova[1]
            test = 'subject_test.pdf'
            test_res = 'draw_horizontal_line.pdf'
            draw_horizontal_line(test, test_res, book_code)

            all_tests.append(f'camtest-{subject_name1}-{subject_name2}{num + 1}.pdf')

            # Fayllarni birlashtirish va yangi faylni saqlash
            merge_pdf([muqova, test_res], f'camtest-{subject_name1}-{subject_name2}{num + 1}.pdf')
            os.remove(file_path)
            os.remove(test_res)

            book_code = data_muqova[1]
            answer_db = AnswerTest(book_code=book_code, answers=keys)
            answer_db.save()

            generate_data = GenerateTestData(subject1=subject_name1, subject2=subject_name2,
                                             language=language_name, number_books=book_code,
                                             user=user)
            generate_data.save()

        # Barcha generatsiya bo'lgan test fayllarini birlashtirish
        test_book_name = (f'{datetime.now().year}{datetime.now().month}{datetime.now().day}{datetime.now().hour}'
                          f'{datetime.now().minute}{datetime.now().second}')
        merge_pdf(all_tests, f'{project_path}/media/userfile/'
                             f'{test_book_name}.pdf')
        data = UserFile(user=user, file=f'userfile/{test_book_name}.pdf')
        data.save()

        revome_file(all_tests)
        os.remove('qr_code_apk.png')
        return Response({'success': True}, status=200)
