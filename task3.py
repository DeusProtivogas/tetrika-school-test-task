def appearance(intervals):
    times = []
    for key in intervals:
        times_temp = []
        data = intervals[key]
        # Добавляю каждому таймстампу статус: +1 (если это начало отрезка), или -1 (если это конец)
        for ind in range(len(data)):
            times_temp.append(
                (data[ind], (-1) ** (ind % 2), key)
            )
        # Проверяю на пересекающиеся сегменты для сущности
        # Т.е. если ученик зашел во время t1, зашел во время t2, вышел во время t3, вышел во время t4
        # Считаю отрезок t1 - t4
        times_temp.sort()

        status = 0
        # Для суммы промежуточных статусов - если 0, то сущность не присутствует на уроке
        # если 1, то присутствует
        # если >1, то отрезки пересекаются
        time_corr = []
        for ind in range(len(times_temp)):
            prev_stat = status
            status += times_temp[ind][1]
            if prev_stat == 0 and status:  # Сущность появилась на уроке, время начала отрезка
                time_corr.append(times_temp[ind])
            if prev_stat and status == 0:  # Сущность ушла с урока, время конца отрезка
                time_corr.append(times_temp[ind])
        times.extend(time_corr)

    # Такая же логика
    # Когда промежуточный статус == 3, урок идет, ученик и учитель присутствуют, записываем начало
    # Когда кто-то уходит, записываем время конца
    res_status = 0
    total_time = 0
    lesson_happened = 0  # Флаг идущего урока
    start_time = 0
    times.sort()
    for time, status, label in times:

        res_status += status
        if res_status == 3 and not lesson_happened:
            start_time = time
            lesson_happened = 1
        if lesson_happened and res_status == 2:
            end_time = time
            total_time += (end_time - start_time)
            lesson_happened = 0
    # Возвращаю полное время присутствия
    return total_time


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'