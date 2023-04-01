import json


with open('skillbox_json_messages.log', 'r') as file:
    levels = {}
    hours = {}
    warn_dict = {}
    messages = []
    warning_messages = []
    max_log_count = 0
    max_log_hour = ''
    critical_timing_count = 0
    for line in file:
        line = json.loads(line)
        levels[line['level']] = levels.setdefault(line['level'], 0) + 1
        hour, minute = line['time'].split(':')[0], line['time'].split(':')[1]
        hours[hour] = hours.setdefault(hour, 0) + 1
        if max_log_count < hours[hour]:
            max_log_count = hours[hour]
            max_log_hour = hour
        if line['level'] == 'CRITICAL' and int(hour) == 5 and 0 < int(minute) < 20:
            critical_timing_count += 1
        messages.append(line['message'])
        if line['level'] == 'WARNING':
            warning_messages.append(line['message'])

    warn_word_max = 0
    warn_word = ''
    for mes in warning_messages:
        for word in mes.split():
            warn_dict[word] = warn_dict.setdefault(word, 0) + 1
            if warn_dict[word] > warn_word_max:
                warn_word_max = warn_dict[word]
                warn_word = word

    [print(f'Логи типа {level} зафиксированы в количестве {count}') for level, count in levels.items()]
    print(f'Наибольшее число логов было в {max_log_hour} час')
    print(f'В период с 05:00:00 по 05:20:00 было {critical_timing_count} логов')
    print(f'Число сообщений, в которых присутствует слово dog: {len([item for item in messages if "dog" in item])}')
    print(f'Чаще всего в логах типа WARNING встречалось слово: {warn_word}')
