import ast


def compare_answers(user_answers, correct_answers):
    correct_answers = ast.literal_eval(correct_answers)
    correct_count_1 = 0
    correct_count_2 = 0
    correct_count_3 = 0
    res = []

    for correct, user in zip(correct_answers, user_answers):
        question = list(correct.keys())[0]

        if correct[question] == user[question]:
            res.append([user[question], 1])
            if int(question) < 31:
                correct_count_1 += 1
            elif 30 < int(question) < 61:
                correct_count_2 += 1
            elif 60 < int(question) < 91:
                correct_count_3 += 1
        else:
            if user[question] == 'error':
                res.append(['-', 0])
            else:
                res.append([user[question], 0])

    find_answers = [correct_count_1, correct_count_2, correct_count_3]
    data = {
        'find_ans': find_answers,
        'result': res
    }
    return data
