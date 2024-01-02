print("Приветсвтую на своей викторине посвященной нескольким разделам:")
print("Математика, Биология, Логика")

questions_mathematics = ["1. 21 + 44 = ?",
                         "2. 28 - 15 = ?",
                         "3. 4 * 8 = ?",
                         "4. 8 / 4 = ?",
                         "5. (8 + 12 * 3) / 22 = ?"]

answers_mathematics = ["65",
                       "13",
                       "32",
                       "2",
                       "2"]

questions_biology = ["1. Что изучает ботаника?",
                     "2. Как называют человека, который занимается биологией?",
                     "3. Как называется смерть всех представителей определённого вида?",
                     "4. Правда или ложь? Саламандра является теплокровным животным.",
                     "5. Правда или ложь? Обычная простуда вызывается вирусом.",
                     "6. Как называется оплодотворенная яйцеклетка?"]

answers_biology = ["Растения",
                   "Биолог",
                   "Вымирание",
                   "Ложь",
                   "Правда",
                   "Зигота"]

questions_logics = ["1. Каких камней не бывает в речке?",
                   "2. Что не вместится даже в самую большую кастрюлю?",
                   "3. Что может в одно и то же время стоять и ходить, висеть и стоять, ходить и лежать?",
                   "4. Завязать можно, а развязать нельзя. Что это такое?",
                   "5. Я - вода, и по воде плаваю. Кто я такая?"]

answers_logics = ["Сухих",
                 "Крышка этой кастрюли",
                 "Часы",
                 "Разговор",
                 "Льдинка"]

answers_chapter = ["Математика",
                   "Биология",
                   "Логика"]

answers_error = ["Да", "Нет"]

score = 0

user_answers_chapter = input("Введите название выбранного раздела:")
if user_answers_chapter == answers_chapter[1]:
    print("Выбран раздел Биология:")
    print("В этом разделе могут встречатся вопросы на которые надо ответить Правда или Ложь")
    print("Следите за вопросом")
    print(questions_biology[0])
    user_answers_byology = input("Введите свой ответ:")
    if user_answers_byology == answers_biology[0]:
        print("Правильно!!!")
        score = score + 1
        print("Текущее количество правильных ответов", score)
        print("Следующий вопрос:")
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Правильный ответ: Растения")
            print("Следующий вопрос:")
        else:
            print("Следующий вопрос:")
    print(questions_biology[1])
    user_answers_byology = input("Введите свой ответ:")
    if user_answers_byology == answers_biology [1]:
        print("Правильно!!!")
        score = score + 1
        print("Текущее количество правильных ответов", score)
        print("Следующий вопрос:")
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Праильный ответ: Биолог")
            print("Следующий вопрос:")
        else:
            print("Следующий вопрос:")
    print(questions_biology[2])
    user_answers_byology = input("Введите свой ответ:")
    if user_answers_byology == answers_biology[2]:
        print("Правильно!!!")
        score = score + 1
        print("Текущее количество правильных ответов", score)
        print("Следующий вопрос:")
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
                print("Праильный ответ: Вымирание")
                print("Следующий вопрос:")
        else:
            print("Следующий вопрос:")
    print(questions_biology[3])
    user_answers_byology = input("Введите свой ответ:")
    if user_answers_byology == answers_biology[3]:
        print("Правильно!!!")
        score = score + 1
        print("Текущее количество правильных ответов", score)
        print("Следующий вопрос:")
    else:
        print("Неправилььно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Правильный ответ: Ложь")
            print("Следующий вопрос:")
        else:
            print("Следующий вопрос:")
    print(questions_biology[4])
    user_answers_byology = input("Введите свой ответ:")
    if user_answers_byology == answers_biology[4]:
        print("Правильно!!!")
        print("Следующий вопрос:")
        score = score + 1
        print("Текущее количество правильных ответов", score)
        print("Следующий вопрос:")
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Праильный ответ: Правда")
            print("Следующий вопрос:")
        else:
            print("Следующий вопрос:")
    print(questions_biology[5])
    user_answers_byology = input("Введите свой ответ:")
    if user_answers_byology == answers_biology[5]:
        print("Правильной!!!")
        print("Викторина по разделе Биология, пройдена!!!")
        score = score + 1
        print("Текущее количество правильных ответов", score)
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Праильный ответ: Зигота")
            print("Викторина по разделе Биология, пройдена!!!")
        else:
            print("Викторина по разделе Биология, пройдена!!!")
    if score >= 5:
        print("Отличные знания по биологии")
    elif score >= 3:
        print("Неплохие знания по биологии")
    else:
        print("Стоит подучить разделы биологии!!!")
elif user_answers_chapter == answers_chapter[0]:
    print("Отлично, выбран раздел математика!")
    print("Вам предстоит решить несложные примеры")
    print(questions_mathematics[0])
    user_answers_mathematics = input("Введите свой ответ:")
    if user_answers_mathematics == answers_mathematics[0]:
        print("Правильно!!!")
        score = score + 1
        print("Текущее количество очков:", score)
        print("Следующий пример:")
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Правильный ответ: 65")
            print("Следующий пример:")
        else:
            print("Следующий пример:")
    print(questions_mathematics[1])
    user_answers_mathematics = input("Введите свой ответ:")
    if user_answers_mathematics == answers_mathematics[1]:
        print("Правильно!!!")
        score = score + 1
        print("Текущее количество очков:", score)
        print("Следующий пример:")
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Правильный ответ: 13")
            print("Следующий пример:")
        else:
            print("Следующий пример:")
    print(questions_mathematics[2])
    user_answers_mathematics = input("Введите свой ответ:")
    if user_answers_mathematics == answers_mathematics[2]:
        print("Правильно!!!")
        score = score + 1
        print("Текущее количество очков:", score)
        print("Следующий пример:")
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Правильный ответ: 32")
            print("Следующий пример:")
        else:
            print("Следующий пример:")
    print(questions_mathematics[3])
    user_answers_mathematics = input("Введите свой ответ:")
    if user_answers_mathematics == answers_mathematics[3]:
        print("Правильно!!!")
        score = score + 1
        print("Текущее количество очков:", score)
        print("Следующий пример:")
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Правильный ответ: 2")
            print("Следующий пример:")
        else:
            print("Следующий пример:")
    print(questions_mathematics[4])
    user_answers_mathematics = input("Введите свой ответ")
    if user_answers_mathematics == answers_mathematics[4]:
        print("Правильно!!!")
        score = score + 1
        print("Поздравляю, вы прошли викторину по разделу Математика!!!")
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Правильный ответ: 2")
            print("Поздравляю, вы прошли викторину по разделу Математика!!!")
    print("Итоговое количество очков:", score)
    if score == 5:
        print("Хорошее умение решать примеры!")
    elif score >= 3:
        print("Неплохие умения решать примеры, но невнимательно!!!")
    else:
        print("Надо больше тренироваться!!!")
elif user_answers_chapter == answers_chapter[2]:
    print("Отлично, выбран раздел Логика")
    print(questions_logics[0])
    user_answers_logics = input("Введите ответ:")
    if user_answers_logics == answers_logics[0]:
        print("Правильно!!!")
        score = score + 1
        print("Текущее количество правильных ответов:", score)
        print("Следующий вопрос:")
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Праильный ответ: Сухих")
            print("Следующий вопрос:")
        else:
            print("Следующий вопрос:")
    print(questions_logics[1])
    user_answers_logics = input("Введите ответ:")
    if user_answers_logics == answers_logics[1]:
        print("Правильно!!!")
        score = score + 1
        print("Текущее количество правильных ответов:", score)
        print("Следующий вопрос:")
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Праильный ответ: Крышка этой кастрюли")
            print("Следующий вопрос:")
        else:
            print("Следующий вопрос:")
    print(questions_logics[2])
    user_answers_logics = input("Введите ответ:")
    if user_answers_logics == answers_logics[2]:
        print("Правильно!!!")
        score = score + 1
        print("Текущее количество правильных ответов:", score)
        print("Следующий вопрос:")
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Праильный ответ: Часы")
            print("Следующий вопрос:")
        else:
            print("Следующий вопрос:")
    print(questions_logics[3])
    user_answers_logics = input("Введите свой ответ:")
    if user_answers_logics == answers_logics[3]:
        print("Правильно!!!")
        score = score + 1
        print("Текущее количество правильных ответов:", score)
        print("Следующий вопрос:")
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Праильный ответ: Разговор")
            print("Следующий вопрос:")
        else:
            print("Следующий вопрос:")
    print(questions_logics[4])
    user_answers_logics = input("Введите свой ответ:")
    if user_answers_logics == answers_logics[4]:
        print("Правильно!!!")
        score = score + 1
        print("Текущее количество правильных ответов:", score)
    else:
        print("Неправильно!!!")
        user_answers_error = input("Если хотите узнать правильный ответ, напишите Да:")
        if user_answers_error == answers_error[0]:
            print("Праильный ответ: Льдинка")
        else:
            print("Это конец!!!")
    print("Поздравляю, самый необъективный тест пройден!")
    print("Итоговое количество праильных ответов =", score)
    if score == 5:
        print("Отличные навыки, ты смог(ла) решить все мои загадки!!!")
    elif score >= 3:
        print("Неплохо, но стоит уделять больше времени развитию логики!!!")
    else:
        print("В следующий раз повезет(((")