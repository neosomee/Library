import telebot
from telebot import types


# Ссылки на фото произведений
photo1 = 'https://avatars.mds.yandex.net/i?id=8ce1b6d52ee21aab585d66780a448fab_l-3760959-images-thumbs&n=13'
photo2 = "https://static.onlinetrade.ru/img/items/m/kniga_anna_karenina_tolstoy_l.n_1675449271_1.jpg"
photo3 = "https://booksrus.fr/upload/iblock/31b/31b9429f7b972ed3f688c2ffda10a332.jpg"
photo4 = "https://main-cdn.sbermegamarket.ru/big2/hlr-system/1725198/100023060788b0.jpg"
photo5 = "https://cdn1.ozone.ru/s3/multimedia-x/6597669093.jpg"
photo6 = "https://cdn1.ozone.ru/s3/multimedia-3/6425865963.jpg"
photo7 = "https://cdn1.ozone.ru/s3/multimedia-2/6443697230.jpg"
photo8 = "https://main-cdn.sbermegamarket.ru/big2/hlr-system/1517622/100023053219b0.jpg"
photo9 = "https://cdn1.ozone.ru/s3/multimedia-q/6013415030.jpg"
photo10 = "https://cdn1.ozone.ru/multimedia/1015719610.jpg"

# Информация о произведений
text1 = ("Роман-эпопея, который описывает жизнь русского общества в период наполеоновских войн."
         "Книга охватывает события с 1805 по 1812 год и включает в себя множество персонажей, "
         "таких как Пьер Безухов, Наташа Ростова, Андрей Болконский и другие. Роман также рассматривает философские вопросы, такие как свобода, судьба и человеческие отношения.")
text2 = ('Роман Льва Николаевича Толстого, опубликованный в 1877 году. '
         'Сюжет повествует о судьбе Анны Карениной, молодой замужней женщины, которая испытывает страсть к офицеру Алексею Вронскому.'
         'Роман затрагивает темы любви, брака, социального положения и морали.')
text3 = ('Роман о бедном студенте, который убил старуху-процентщицу,'
         'чтобы проверить свою теорию о праве некоторых людей на преступления. После убийства герой мучается от угрызений совести и ищет искупления.')
text4 = ('Роман о Дмитрии Карамазове, которого обвиняют в убийстве отца. Помимо суда, роман поднимает философские и религиозные вопросы, такие как свобода воли и нравственность')
text5 = ('Роман о писателе и его возлюбленной. Мастер написал роман о Понтии Пилате и Иешуа, '
         'который стал причиной его страданий. Маргарита помогает ему, используя помощь дьявола Воланда и его свиты.')
text6 = ('Роман, описывающий события Гражданской войны на Украине в конце 1918 года.'
         'Роман повествует о семье русских интеллигентов и их друзьях, которые переживают социальный катаклизм гражданской войны.')
text7 = ('Сатирическая повесть, критикующая советское общество и научный прогресс через историю профессора, который пересадил гипофиз человеку собаке, создав опасного человека.')
text8 = ('Роман в стихах о молодом дворянине, разочарованном в светской жизни, и его сложных отношениях с Татьяной Лариной.')
text9 = ('Исторический роман о молодом офицере Петре Гриневе, его любви к дочери капитана и участии в Пугачевском бунте. Роман исследует темы морали, чести и долга.')
text10 = ('Сборник рассказов Пушкина, каждый из которых представлен как написанный другим человеком. Истории разнообразны и касаются разных аспектов жизни.')

# токен бота
bot = telebot.TeleBot("8094035741:AAFWYPGy75zklMjziu3rYFkc9d7wbw_bQ5s")
@bot.message_handler(commands=['start'])
def welcome(message):
    if message.text == '/start':
        # Отправляю приветственный текст
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\n\nУ меня ты сможешь увидеть список книг(/book) выбрать по клику книгу и увидеть её описание\nЗапросить отсутствующую книгу(/bookreq), чтобы её добавили в библиотеку, раздел настроек(/settings)\nВернуться назад(/back)\n\nКонтакт для связи: https://t.me/neosome')
    else:
        bot.send_message(message.chat.id, 'Перекинул тебя в главном меню! ')

@bot.message_handler(commands=['book'])
def book(message):
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Война и мир Л.Н. Толстой", callback_data='война_мир')
        item2 = types.InlineKeyboardButton('Анна Каренина Л.Н. Толстой', callback_data='анна_карелина')
        item3 = types.InlineKeyboardButton('Преступление и наказание Ф.М. Достоевский', callback_data='преступ_наказ')
        item4 = types.InlineKeyboardButton('Братья Карамазовы Ф. Достоевский', callback_data='братья')
        item5 = types.InlineKeyboardButton("Мастер и Маргарита М.А. Булгаков", callback_data='Мастер_Маргарита')
        item6 = types.InlineKeyboardButton('Белая гвардия М. Булгаков', callback_data='белая гвардия')
        item7 = types.InlineKeyboardButton('Собачье сердце М. Булгаков', callback_data='Собачье сердце')
        item8 = types.InlineKeyboardButton('Евгений Онегин А.С. Пушкин', callback_data='Онегин')
        item9 = types.InlineKeyboardButton('Капитанская дочка А.С. Пушкин', callback_data='Капит_дочка')
        item10 = types.InlineKeyboardButton('Повести Белкина А.С. Пушкин', callback_data='повести Белкина')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
        bot.send_message(message.chat.id, 'Список книг', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message.text:
        if call.data == 'война_мир':
            bot.send_photo(chat_id=call.message.chat.id, photo=photo1, caption=text1)
        elif call.data == 'анна_карелина':
            bot.send_photo(chat_id=call.message.chat.id, photo=photo2, caption=text2)
        elif call.data == 'преступ_наказ':
            bot.send_photo(chat_id=call.message.chat.id, photo=photo3, caption=text3)
        elif call.data == 'братья':
            bot.send_photo(chat_id=call.message.chat.id, photo=photo4, caption=text4)
        elif call.data == 'Мастер_Маргарита':
            bot.send_photo(chat_id=call.message.chat.id, photo=photo5, caption=text5)
        elif call.data == 'белая гвардия':
            bot.send_photo(chat_id=call.message.chat.id, photo=photo6, caption=text6)
        elif call.data == 'Собачье сердце':
            bot.send_photo(chat_id=call.message.chat.id, photo=photo7, caption=text7)
        elif call.data == 'Онегин':
            bot.send_photo(chat_id=call.message.chat.id, photo=photo8, caption=text8)
        elif call.data == 'Капит_дочка':
            bot.send_photo(chat_id=call.message.chat.id, photo=photo9, caption=text9)
        elif call.data == 'повести Белкина':
            bot.send_photo(chat_id=call.message.chat.id, photo=photo10, caption=text10)

@bot.message_handler(commands=['bookreq'])
def bookreq(message):
    bot.send_message(message.chat.id,"Если не нашел книгу из списка, то заполни анкету\n\nСсылка: https://forms.gle/cdZK1h6EFLrxu2u56'")

@bot.message_handler(commands=['settings'])
def settings(message):
    bot.send_message(message.chat.id,'Хочешь получить обратную связь?:\nСсылка: https://t.me/neosome')

@bot.message_handler(commands=['back'])
def back(message):
    bot.send_message(message.chat.id,"Вернул обратно\n\nВот все функции:увидеть список книг(/book) выбрать по клику книгу и увидеть её описание\nЗапросить отсутствующую книгу(/bookreq), чтобы её добавили в библиотеку, раздел настроек(/settings)\nВернуться назад(/back) ")

bot.polling(none_stop=True)