from vk_api.keyboard import VkKeyboard, VkKeyboardColor

# settings
TOKEN = open('./token.txt', 'r').readline()
GROUP_ID = 198949491
EDITORS = [194751565, 222017399, 437341630, 156440440, 154176195, 184456849, 169860673, 569974359, 231154797, 263709555,
           465268896, 215500548, 276635406, 533867859, 255999212, 420661822, 182808284, 481520353, 436078575, 310876955,
           557997992, 237301009]
ADMIN = 194751565

# schedules
# subjects
sub = [
    'физика',  # 0
    'в.н. англ',  # 1
    'русский_язык',  # 2
    'информатика',  # 3
    'физкультура',  # 4
    'обществознание',  # 5
    'математика',  # 6
    'обж',  # 7
    'литература',  # 8
    'немецкий язык',  # 9
    'химия',  # 10
    'история урала',  # 11
    'русский эк',  # 12
    'история',  # 13
    'н.а. англ',  # 14'
    'география',  # 15
    'астрономия',  # 16
    'биология',  # 17
    'технология',  # 18
    'мхк',  # 19
]

# schedule
schedule = {
    'понедельник': [sub[6],
                    sub[8],
                    sub[15],
                    sub[1],
                    sub[14],
                    sub[17],
                    sub[10],
                    sub[4]],

    'вторник': [sub[6],
                sub[9],
                sub[0],
                sub[5],
                sub[8],
                sub[1],
                sub[14],
                sub[13]],

    'среда': [sub[6],
              sub[3],
              sub[11],
              sub[14],
              sub[2],
              sub[1],
              sub[14]],

    'четверг': [sub[0],
                sub[13],
                sub[16],
                sub[6],
                sub[1],
                sub[14],
                sub[5],
                sub[12]],

    'пятница': [sub[1],
                sub[14],
                sub[18],
                sub[6],
                sub[7],
                sub[8],
                sub[4]],

    'суббота': [sub[9],
                sub[4],
                sub[1],
                sub[14],
                sub[19]]
}

# homework
hw = dict.fromkeys(sub, '-')

# timetable
timetable = ['1) 8:50 - 9:30',
             '2) 9:45 - 10:25',
             '3) 10:40 - 11:20',
             '4) 11:35 - 12:15',
             '5) 12:30 - 13:10',
             '6) 13:15 - 13:55',
             '7) 14:00: - 14:45']

# keyboards
# main keyboard
main = VkKeyboard(inline=False)
main.add_button(label='расписание звонков',
                color=VkKeyboardColor.PRIMARY)
main.add_button(label='расписание уроков',
                color=VkKeyboardColor.PRIMARY)
main.add_line()
main.add_button(label='дз на день',
                color=VkKeyboardColor.PRIMARY)
main.add_button(label='дз на завтра',
                color=VkKeyboardColor.PRIMARY)
main.add_line()
main.add_button(label='полезные ссылки',
                color=VkKeyboardColor.PRIMARY)
main.add_button(label='всё дз',
                color=VkKeyboardColor.PRIMARY)
main.add_line()
main.add_button(label='призвать админа',
                color=VkKeyboardColor.PRIMARY)
main.add_button(label='режим разработчика',
                color=VkKeyboardColor.PRIMARY)

# admin keyboard
admin = VkKeyboard(inline=False)
admin.add_button(label='load data',
                 color=VkKeyboardColor.PRIMARY)
admin.add_button(label='добавить дз',
                 color=VkKeyboardColor.PRIMARY)
admin.add_line()
admin.add_button(label='обычный режим', color=VkKeyboardColor.NEGATIVE)

# link keyboard
link = VkKeyboard(inline=False)
link.add_openlink_button(label='Сайт Школы',
                         link='http://школа91.екатеринбург.рф')
link.add_line()
link.add_openlink_button(label='СГ',
                         link='http://62.245.43.79')
link.add_line()
link.add_openlink_button(label='ответы',
                         link='https://www.google.ru')
link.add_line()
link.add_button(label='назад',
                color=VkKeyboardColor.NEGATIVE)

# day keyboard
day = VkKeyboard(inline=False)
count = 0
for i in schedule.keys():
    day.add_button(label=i, color=VkKeyboardColor.PRIMARY)
    count += 1
    if count % 2 == 0:
        day.add_line()
day.add_button(label='назад', color=VkKeyboardColor.NEGATIVE)

# subjects keyboard
subjects = VkKeyboard(inline=False)
count = 0
for i in sub:
    subjects.add_button(label=i, color=VkKeyboardColor.PRIMARY)
    count += 1
    if count % 3 == 0:
        subjects.add_line()
        count = 0
subjects.add_button(label='обычный режим', color=VkKeyboardColor.NEGATIVE)

# empty keyboard
empty = VkKeyboard(inline=False)
empty.add_button(label='-', color=VkKeyboardColor.PRIMARY)
empty.add_line()
empty.add_button(label='обычный режим', color=VkKeyboardColor.NEGATIVE)


def key(name):
    return name.get_keyboard()