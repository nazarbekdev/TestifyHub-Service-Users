from pprint import pprint as pp


def mother_and_english_languages_form(request):
    question = request.split('&')[0]
    question_lst = request.split('&')[1].split('#')
    all_question = [{'question': question}]

    pp(question_lst[1:])
    for elem in question_lst[1:]:
        all_question.append({'question': elem.split('//')[0], 'answer': elem.split('//')[1], 'answers':
             [elem.split('//')[1], elem.split('//')[2], elem.split('//')[3], elem.split('//')[4]]
                             })
    return all_question, len(all_question)-1


# Olingan natija
result = [{'question': "She'r matnini o'qish va ushbu matnga asoslangan topshiriqlarni "
              'bajaring.\r\n'
              '\r\n'
              '<i>Tong.</i>\r\n'
              '<i>Quyoshli ufq. </i> \r\n'
              '<i>Maysazor.  </i>\r\n'
              "<i>Maysazorda kunni go'dakligi.  </i>\r\n"
              '<i>Emaklaydi qiyqirib. </i>\r\n'
              "<i>Yuragida umid g'unchasi, </i>\r\n"
              '<i>Yuzlarida quvonch chechagi. </i>\r\n'
              "<i>Ko'zlarida omad shulasi.  (N.Norqul) </i>\r\n"},
 {'answer': ' 5 ta\r\n ',
  'answers': [' 6 ta\r\n ', ' 4 ta\r\n ', ' 7 ta\r\n\r\n '],
  'question': " Yuqoridagi she'rda ishtirok etgan yasovchi\r\n"
              " qo'shimchalar miqdori?\r\n"
              '\r\n'
              ' '},
 {'answer': " she'r matnida uchta so'zda fonetik hodisaga\r\n kuzatilgan.\r\n ",
  'answers': [" she'r matnida ikkita soʻzda imloviy xatolik bor.\r\n ",
              " she'r matnida ikkita so'zda qator undosh mavjud\r\n ",
              " she'r matnida bitta so'zda kelishik bilan bog'liq\r\n"
              ' xatolik uchraydi.'],
  'question': " Ushbu she'r matnida qatnashgan so'zlar haqida\r\n"
              " qaysi fikr(lar) noto'g'ri.\r\n"
              '\r\n'
              ' '}]
