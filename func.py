from config import timetable, schedule, hw, sub


def timetable_out():
    answer = ''
    for i in range(len(timetable)):
        answer += timetable[i]
        answer += '\n'

    return answer


def schedule_out():
    answer = ''
    for k, v in schedule.items():
        answer += k.capitalize() + '\n'
        count = 0
        for i in v:
            count += 1
            answer += f'{count}) {i.capitalize()} \n'
        answer += '\n'
    return answer


def day_out(date):
    date %= 7
    if date == 6:
        date = 0
    answer = list(schedule.keys())[date].capitalize()
    answer += '\n' + '\n'
    count = 1
    for i in schedule[list(schedule.keys())[date]]:
        answer += f'{count}) {i.capitalize()}\n'
        answer += hw[i] + '\n' + '\n'
        count += 1

    return answer


def hw_out():
    answer = ''
    for k, v in hw.items():
        answer += k.capitalize() + '\n'
        answer += v + '\n' + '\n'
    return answer


def save():
    with open('data.txt', 'w') as data:
        for v in hw.values():
            data.write(str(v).replace('\n', ' <3 ') + '\n')
        data.close()


def load():
    with open('data.txt', 'r') as data:
        for i in sub:
            hw[i] = data.readline().replace('\n', '')
            hw[i] = hw[i].replace(' <3 ', '\n')
        data.close()