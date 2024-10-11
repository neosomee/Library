# -*- coding: utf-8 -*-

# Эта строка в Python означает, что кодировка файла устанавливается на UTF-8

# Эти команды импортируют модули и классы, необходимые для работы с Telegram ботами. telebot-для тг ботов, sqlite3-для работы с базой данных
# from telebot import types: Импортирует модуль types из библиотеки telebot.
import telebot
import sqlite3
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

# Токен тг бота
bot = telebot.TeleBot("7929042954:AAER7AEZ9ZFAgUlJzA_kU60Wx7u__UVXAuQ")

# Открывает соединение с базой данных database.db.
# Указывает, что соединение может использоваться из разных потоков, что полезно для многопоточных приложений.
conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor() #Создает курсор, который используется для выполнения SQL запросов, позволяет взаимодействовать с базой данных, выполняя операции чтения, записи и обновления данных.


# Определение функции, которая принимает четыре аргумента: user_id типа int, user_name и user_surname типа str, а также username типа str.
def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO Users (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
# Выполняет SQL запрос для вставки новой записи в таблицу Users. В данном случае используются параметры (?), чтобы избежать SQL инъекций. Аргументы функции передаются в эти параметры.
    conn.commit() #  Команда для сохранения изменений в базе данных после выполнения запроса.


# Отвечает за обработку команды /start и добавление имени пользователя в базу данных.
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать. Ваше имя добавлено в базу данных!\n\nНавигация:\n'
                                          '/book - Список книг и их описание\n'
                                          '/bookreq - Если не нашел книгу из списка\n'
                                          '/settings - Обратная связь\n'
                                          '/back - Вернуться назад к Навигации')
    us_id = message.from_user.id                # Получение ID пользователя.
    us_name = message.from_user.first_name      # Получение первого имени пользователя.
    us_sname = message.from_user.last_name      # Получение фамилии пользователя.
    username = message.from_user.username       # Получение имени пользователя в Telegram (если оно есть).

    db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username) # Вызов функции db_table_val для добавления информации о пользователе в базу данных.

# Отвечает за создание инлайн клавиатуры с кнопками для выбора книги и отправку её пользователю.
@bot.message_handler(commands=['book'])
def book(message):
        markup = types.InlineKeyboardMarkup(row_width=1) #Создание нового экземпляра класса InlineKeyboardMarkup. Параметр row_width=1 указывает, что каждая кнопка будет занимать одну строку.
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

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)      # Добавление всех созданных кнопок в клавиатуру.
        bot.send_message(message.chat.id, 'Список книг', reply_markup=markup)    # Отправка сообщения с названием списка книг и присвоенной инлайн клавиатурой.

# Регистрация обработчика событий обратного вызова (callback_query). Все вызовы будут перехвачены этой функцией.
@bot.callback_query_handler(func=lambda call: True)
def callback(call):         #  Определение функции callback, которая получает событие обратного вызова в качестве аргумента.
    if call.message.text:       # Проверка наличия текста в сообщении. Если текст присутствует, значит был вызван обратный вызов кнопки инлайн клавиатуры.
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
            bot.send_photo(chat_id=call.message.chat.id, photo=photo10, caption=text10)     # аналогичные команды отправляют фото и подпись к нему.

# Регистрация обработчика сообщений для команды /bookreq. Когда пользователь отправляет команду /bookreq, функция bookreq вызывается автоматически.
@bot.message_handler(commands=['bookreq'])
def bookreq(message):       #  Определение функции bookreq, которая получает сообщение в качестве аргумента.
    bot.send_message(message.chat.id,"Если не нашел книгу из списка, то заполни анкету\n\nСсылка: https://forms.gle/cdZK1h6EFLrxu2u56'") # Отправка сообщения пользователю с ссылкой на форму для добавления книги.

# Регистрация обработчика сообщений для команды /settings. Когда пользователь отправляет команду /settings, функция settings вызывается автоматически.
@bot.message_handler(commands=['settings'])
def settings(message):      # Определение функции settings, которая получает сообщение в качестве аргумента.
    bot.send_message(message.chat.id,'Хочешь получить обратную связь?:\nСсылка: https://t.me/neosome')

# Регистрация обработчика сообщений для команды /back. Когда пользователь отправляет команду /back, функция back вызывается автоматически.
@bot.message_handler(commands=['back'])
def back(message):          # Определение функции back, которая получает сообщение в качестве аргумента.
    bot.send_message(message.chat.id,"Вернул обратно\n\nВот все функции:увидеть список книг(/book) выбрать по клику книгу и увидеть её описание\nЗапросить отсутствующую книгу(/bookreq), чтобы её добавили в библиотеку, раздел настроек(/settings)\nВернуться назад(/back) ")

# Начинает постоянный опрос сервера Telegram для получения новых сообщений и их обработки. none_stop=True означает, что бот будет работать непрерывно, пока не будет остановлен вручную.
bot.polling(none_stop=True)
