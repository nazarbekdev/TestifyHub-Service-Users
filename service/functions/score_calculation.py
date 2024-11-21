def score_calculator(compulsory_sub_ans, sub1_ans, sub2_ans, language, blok1, blok_2):
    if language == 'ingliz':
        if blok1 == 'Inliz tili':
            ball = compulsory_sub_ans * 1.1 + 30 * 3.1 + sub2_ans * 2.1
            result = {
                'ball': float(ball),
                'compulsory': compulsory_sub_ans,
                'sub1': 30,
                'sub2': sub2_ans,
                'lan_status': 1,
                'description': ''
            }
            return result
        elif blok_2 == 'Inliz tili':
            ball = compulsory_sub_ans * 1.1 + sub1_ans * 3.1 + 30 * 2.1
            result = {
                'ball': float(ball),
                'compulsory': compulsory_sub_ans,
                'sub1': sub1_ans,
                'sub2': 30,
                'lan_status': 2,
                'description': ''
            }
            return result
        else:
            ball = 0
            result = {
                'ball': float(ball),
                'compulsory': compulsory_sub_ans,
                'sub1': 0,
                'sub2': 0,
                'lan_status': 0,
                'description': """Abituriyent tomonidan belgilangan 'Chet tili' tanlangan 'Asosiy fan' larga mos kelmadi!
                               Ushbu sababga ko'ra tanlangan fanlar javobini tekshirish imkoni yo'q.
                               Abiturentlardan hushyorlikni so'rab qolamiz!"""
            }
            return result
    elif language == 'nemis':
        if blok1 == 'Nemis tili':
            ball = compulsory_sub_ans * 1.1 + 30 * 3.1 + sub2_ans * 2.1
            result = {
                'ball': float(ball),
                'compulsory': compulsory_sub_ans,
                'sub1': 30,
                'sub2': sub2_ans,
                'lan_status': 1,
                'description': ''
            }
            return result
        elif blok_2 == 'Nemis tili':
            ball = compulsory_sub_ans * 1.1 + sub1_ans * 3.1 + 30 * 2.1
            result = {
                'ball': float(ball),
                'compulsory': compulsory_sub_ans,
                'sub1': sub1_ans,
                'sub2': 30,
                'lan_status': 2,
                'description': ''
            }
            return result
        else:
            ball = 0
            result = {
                'ball': float(ball),
                'compulsory': compulsory_sub_ans,
                'sub1': 0,
                'sub2': 0,
                'lan_status': 0,
                'description': """Abituriyent tomonidan belgilangan 'Chet tili' tanlangan 'Asosiy fan' larga mos kelmadi!
                               Ushbu sababga ko'ra tanlangan fanlar javobini tekshirish imkoni yo'q.
                               Abiturentlardan hushyorlikni so'rab qolamiz!"""
            }
            return result
    elif language == 'fransuz':
        if blok1 == 'Fransuz tili':
            ball = compulsory_sub_ans * 1.1 + 30 * 3.1 + sub2_ans * 2.1
            result = {
                'ball': float(ball),
                'compulsory': compulsory_sub_ans,
                'sub1': 30,
                'sub2': sub2_ans,
                'lan_status': 1,
                'description': ''
            }
            return result
        elif blok_2 == 'Fransuz tili':
            ball = compulsory_sub_ans * 1.1 + sub1_ans * 3.1 + 30 * 2.1
            result = {
                'ball': float(ball),
                'compulsory': compulsory_sub_ans,
                'sub1': sub1_ans,
                'sub2': 30,
                'lan_status': 2,
                'description': ""
            }
            return result
        else:
            ball = 0
            result = {
                'ball': float(ball),
                'compulsory': compulsory_sub_ans,
                'sub1': 0,
                'sub2': 0,
                'lan_status': 0,
                'description': """Abituriyent tomonidan belgilangan 'Chet tili' tanlangan 'Asosiy fan' larga mos kelmadi!
                               Ushbu sababga ko'ra tanlangan fanlar javobini tekshirish imkoni yo'q.
                               Abituriyentlardan hushyorlikni so'rab qolamiz!"""
            }
            return result
    elif language == 'error':
        ball = compulsory_sub_ans * 1.1 + sub1_ans * 3.1 + sub2_ans * 2.1
        result = {
            'ball': float(ball),
            'compulsory': compulsory_sub_ans,
            'sub1': sub1_ans,
            'sub2': sub2_ans,
            'lan_status': 3,
            'description': ""
        }
        return result
