import telebot
import emoji
from config import bot_token
from config import my_id

bot = telebot.TeleBot(bot_token, parse_mode=None)  # , parse_mode=None
user_info = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    sti = open('images/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    msg = bot.send_message(message.chat.id, 'Приветсвтую Вас, Вы уже на 1 шаг ближе к вашему результату'
        ',сейчас заполните пожалуйста анкетку, Вам просто надо отвечать на вопросы'
        ',поехали => Введите Ваши Имя и Фамилию' + emoji.emojize('🤗'))
    bot.register_next_step_handler(msg, fio_step)


def fio_step(message):
    bot.send_message(message.chat.id, f'Супер, идем дальше' + emoji.emojize('💃'))
    user_info['name'] = message.text
    msg = bot.send_message(message.chat.id, 'Взвесьтесь на напольных весах и напишите Ваш вес в кг.'
                           + emoji.emojize('⚖'))
    bot.register_next_step_handler(msg, weight_step)


def weight_step(message):
    user_info['weight'] = message.text
    msg = bot.send_message(message.from_user.id, 'Померяйте объем талии (меряем' + emoji.emojize('📏') +
                           'чуть выше пупка и запишите, что там у Вас получилось по сантиметрам)')
    bot.register_next_step_handler(msg, waist_step)


def waist_step(message):
    user_info['waist'] = message.text
    msg = bot.send_message(message.chat.id, 'Теперь надо измерить объёьм живота, меряем прям по пупку'
                                            ' и тоже запишите сколько см.' + emoji.emojize('📏'))
    bot.register_next_step_handler(msg, belly_step)


def belly_step(message):
    sti2 = open('images/motivation.webp', 'rb')
    bot.send_sticker(message.chat.id, sti2)
    user_info['belly'] = message.text
    msg = bot.send_message(message.chat.id, 'Супер, хорошо идём' + emoji.emojize('😉') + 'далее меряем '
                        'низ живота, немного ниже пупка и тоже записываем сколько см. получается')
    bot.register_next_step_handler(msg, underbelly_step)


def underbelly_step(message):
    user_info['underbelly'] = message.text
    msg = bot.send_message(message.chat.id, 'Давайте еще проведем замер бёдер в самом широком месте'
                           + emoji.emojize('😇') + 'и тоже напишите результат в см.')
    bot.register_next_step_handler(msg, hips_step)


def hips_step(message):
    user_info['hips'] = message.text
    msg = bot.send_message(message.chat.id, 'Осталось не очень много вопросов' + emoji.emojize('🙃') + 'я всеголишь '
        'фитнес бот' + emoji.emojize('🤖') + 'моя задача собрать всю информацию и передать Александру, иначе мне '
        'прийдется делать очень много Бёрпи или приседаний, поэтому потерпите пожалуйста и ответьте на очень важный '
        'вопрос, напишите о СОСТОЯНИИ ВАШЕГО ЗДОРОВЬЯ (желудок, сердце, голова, суставы, пьёте ли какие нибудь таблетки,'
        ' лекарства, гормональные препараты, есть ли травмы' + emoji.emojize('🤔') + 'просто напишите и нажмите отправить')
    bot.register_next_step_handler(msg, health_step)


def health_step(message):
    user_info['health'] = message.text
    msg = bot.send_message(message.chat.id, 'Где Вы будете тренироваться? Дома или в зале? '
                                            'Просто напишите дом или зал' + emoji.emojize('🤔'))
    bot.register_next_step_handler(msg, where_will_you_train)


def where_will_you_train(message):
    user_info['place of trainings'] = message.text
    msg = bot.send_message(message.chat.id, 'Сколько раз в неделю собираетесь тренироваться? '
                                            'Оцениваем свои силы и время реально' + emoji.emojize('🙏'))
    bot.register_next_step_handler(msg, how_many_trainings_in_a_week)


def how_many_trainings_in_a_week(message):
    user_info['amount of trainings in a week'] = message.text
    msg = bot.send_message(message.chat.id, 'Теперь мне нужно узнать о вашем питании' + emoji.emojize('🍜') +
        'Сколько раз в день Вы обычно кушаете? При условии, что даже если Вы съели одну семечку или '
        'укусили яблоко - это уже считается приёмом пищи, даже если сделали глоток капучино - это тоже уже приём пищи! '
        'Посчитайте примерно в среднем сколько приёмов пищи у Вас получается в день? '
        'И напишите, например (3 или 5 или 8)')
    bot.register_next_step_handler(msg, how_many_eat_in_a_day)


def how_many_eat_in_a_day(message):
    stik3 = open('images/eat_joke_1.webp', 'rb')
    bot.send_sticker(message.chat.id, stik3)
    user_info['amount of food intake in a day'] = message.text
    msg = bot.send_message(message.chat.id, 'Сейчас может быть интересно' + emoji.emojize('🍜') + 'напишите какую еду '
        'или продукты вы больше всего любите, что чаще всего кушаете и в чём ваша слабость в еде?')
    bot.register_next_step_handler(msg, favorite_food)


def favorite_food(message):
    user_info['favorite food'] = message.text
    msg = bot.send_message(message.chat.id, 'Осталось несколько вопросов, напишите о Ваших целях, '
    'где Ваши проблемные зоны, например (хочу похудеть, убрать живот,бока...Ваш вариант)' + emoji.emojize('🧐'))
    bot.register_next_step_handler(msg, goal_step)

@bot.message_handler(content_types=['document'])
def goal_step(message):
    user_info['goal'] = message.text
    # file = open('Прочитайте_меня.txt', 'rb')
    # bot.send_document(message.chat.id, file)
    msg = bot.send_message(message.chat.id, 'Супер, теперь напишите свои вопросы или поставьте '
                                            'прочерк "-" если вопросов нет' + emoji.emojize('😇'))
    bot.register_next_step_handler(msg, final_step)  # , user_info

@bot.message_handler(type=['text'])
def final_step(message):  # , user_info
    user_info['questions'] = message.text
    user_name = message.from_user.first_name  # узнаем айди пользователя
    user_info['customer name'] = user_name
    bot.send_message(message.chat.id, '*Примеры того, как нужно сделать стартовые фото*', parse_mode='MarkdownV2')
    stik4 = open('images/example1.webp', 'rb')
    bot.send_sticker(message.chat.id, stik4)
    stik5 = open('images/example2.webp', 'rb')
    bot.send_sticker(message.chat.id, stik5)
    stik6 = open('images/example3.webp', 'rb')
    bot.send_sticker(message.chat.id, stik6)
    stik7 = open('images/example4.webp', 'rb')
    bot.send_sticker(message.chat.id, stik7)
    bot.send_message(message.chat.id, '*Обязательно прочитайте файлы, '
            'которые находятся ниже, там очень НУЖНАЯ, ПОЛЕЗНАЯ и '
            'ПОДГОТОВИТЕЛЬНАЯ ИНФОРМАЦИЯ, которая Вам нужна, '
            'что бы быстрее добиться результата*', parse_mode='MarkdownV2')
    file = open('useful_information/Прочитайте_меня.txt', 'rb')
    bot.send_document(message.chat.id, file)
    file2 = open('useful_information/И_меня_прочти_обязательно.txt', 'rb')
    bot.send_document(message.chat.id, file2)
    file3 = open('useful_information/Полезная_информация.txt', 'rb')
    bot.send_document(message.chat.id, file3)
    # bot.forward_message(user_id, message.chat.id, message.message_id) отправляет от имени пользователя как эхо бот
    bot.send_message(message.chat.id, 'Супер, Вы прошли анкетирование и я уже отправил анкету тренеру Александру'
        + emoji.emojize('🥳') + '\nЕсли у вашего тренера появятся дополнительные вопросы, он свяжется с Вами '
        'в течении 24 часов. Если дополнительных вопросов не будет, тогда Александр свяжется с Вами '
        'через 2-3 рабочих дня и отправит Вам готовую программу в личные сообщения'+ emoji.emojize('👌'))
    bot.send_message(my_id, f'{list(user_info.keys())[0]} => {user_info.get("name")}\n'
                            f'{list(user_info.keys())[1]} => {user_info.get("weight")}\n'
                     f'{list(user_info.keys())[2]} => {user_info.get("waist")}\n'
                     f'{list(user_info.keys())[3]} => {user_info.get("belly")}\n'
                     f'{list(user_info.keys())[4]} => {user_info.get("underbelly")}\n'
                     f'{list(user_info.keys())[5]} => {user_info.get("hips")}\n'
                     f'{list(user_info.keys())[6]} => {user_info.get("health")}\n'
                     f'{list(user_info.keys())[7]} => {user_info.get("place of trainings")}\n'
                     f'{list(user_info.keys())[8]} => {user_info.get("amount of trainings in a week")}\n'
                     f'{list(user_info.keys())[9]} => {user_info.get("amount of food intake in a day")}\n'
                     f'{list(user_info.keys())[10]} => {user_info.get("favorite food")}\n'
                     f'{list(user_info.keys())[11]} => {user_info.get("goal")}\n'
                     f'{list(user_info.keys())[12]} => {user_info.get("questions")}\n'
                     f'{list(user_info.keys())[13]} => {user_info.get("customer name")}')
    print(user_info.items())
    print(user_name)


# @bot.message_handler(func=lambda m: True)
# def echo_message(message):
#     bot.reply_to(message, 'Super///')

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
# bot.infinity_polling()