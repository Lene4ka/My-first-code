# libraries
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import datetime

# modules
from config import TOKEN, GROUP_ID, key, main, day, link, schedule, EDITORS, ADMIN, admin, subjects, empty, sub, hw
from func import timetable_out, schedule_out, hw_out, day_out, load, save

# init
vk_session = vk_api.VkApi(token=TOKEN, api_version='5.95')
vk = vk_session.get_api()
LongPoll = VkBotLongPoll(vk_session, GROUP_ID)

current_admin_id = 0
lesson = ''
waiter = False


def admin_quit():
    global lesson, current_admin_id, waiter
    current_admin_id = 0
    lesson = ''
    waiter = False


def get_name_by_id(peer_id):
    user_get = vk.users.get(user_ids=peer_id)
    user_get = user_get[0]
    return user_get['first_name'] + ' ' + user_get['last_name']


def send_message(msg, peer_id, keyboard=None):
    vk.messages.send(peer_id=peer_id,
                     message=msg,
                     random_id=get_random_id(),
                     keyboard=keyboard)


def start():
    try:
        global lesson, current_admin_id, waiter

        for event in LongPoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:

                request = event.object.text.lower()
                user_id = event.object.peer_id

                # editor mod
                if user_id == current_admin_id:

                    if request == 'добавить дз':
                        send_message('выберите предмет', user_id, key(subjects))

                    elif request == 'save data':
                        save()
                        send_message('data saved', user_id, key(admin))

                    elif request == 'load data':
                        load()
                        send_message('data loaded', user_id, key(admin))

                    elif request in sub:
                        lesson = request
                        waiter = True
                        send_message('Введите дз', user_id, key(empty))

                    elif request == 'обычный режим':
                        send_message('слушаюсь и повинуюсь', user_id, key(main))
                        admin_quit()

                    elif waiter is True:
                        hw[lesson] = event.object.text
                        save()
                        send_message('дз изменено', user_id, key(admin))
                        waiter = False

                    else:
                        send_message('ты творишь что-то слишком хитрое', user_id, key(admin))

                else:

                    # editor auth
                    if request == 'режим разработчика':
                        if user_id in EDITORS:
                            if current_admin_id == 0:
                                current_admin_id = user_id
                                send_message('слушаюсь и повинуюсь', user_id, key(admin))
                            else:
                                send_message('режим разработчика занят', user_id, key(main))
                        else:
                            send_message('недостаточно прав доступа', user_id, key(main))

                    # common user
                    elif request == 'начать':
                        send_message('Запуск систем.', user_id, key(main))
                        send_message('Генерация ответов на глупые вопросы.', user_id, key(main))
                        send_message('Согласно моим экстрасенсорным способностям, ты хочешь спросить дз.', user_id,
                                     key(main))

                    elif request == 'расписание звонков':
                        send_message(timetable_out(), user_id, key(main))

                    elif request == 'расписание уроков':
                        send_message(schedule_out(), user_id, key(main))

                    elif request == 'дз на день':
                        send_message('выберете день недели', user_id, key(day))

                    elif request == 'всё дз':
                        send_message(hw_out(), user_id, key(main))

                    elif request == 'полезные ссылки':
                        send_message('ok', user_id, key(link))

                    elif request == 'призвать админа':
                        send_message('*звуки дьявольского призыва*', user_id, key(main))
                        send_message(get_name_by_id(user_id) + ' призывает тебя', ADMIN)

                    elif request in schedule.keys():
                        date = list(schedule.keys()).index(request)
                        send_message(day_out(date), user_id, key(main))

                    elif request == 'дз на завтра':
                        send_message(day_out(datetime.datetime.today().isoweekday()), user_id, key(main))

                    elif request == 'назад':
                        send_message('ok', user_id, key(main))

                    elif request == 'reset' and user_id == ADMIN:
                        admin_quit()
                        send_message('reset was successful', user_id, key(main))

                    else:
                        send_message(get_name_by_id(user_id) + ' использует неизвестные команды', ADMIN)

    except Exception as e:
        print('Error:', e)
        start()


start()