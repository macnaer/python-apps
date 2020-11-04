import datetime

import requests
import telebot
from telebot import types

# from lib.Search import CountriesSearh, GlobalCovid, date

bot = telebot.TeleBot('1359393651:AAGzyqe6piRB_BE-TageT7TttBxc1SNsdLY')

URL = "https://api.covid19api.com/summary"
covid19 = requests.get(URL)
covid19 = covid19.json()
# Global countries
covid_global = covid19['Global']
date = covid19['Date']
date = datetime.datetime.fromisoformat(
    covid19['Date'].replace('Z', '+00:00')).strftime("%H год. %M хв. %d.%m.%Y")

covid_countries = covid19['Countries']
# Sort countries by New confirmed
sort_countries = sorted(covid_countries, key=lambda k: k["NewConfirmed"])
sort_countries.reverse()
n = 0
while n < len(sort_countries):
    sort_countries[n].pop('Country')
    sort_countries[n].pop('CountryCode')
    sort_countries[n].pop('Date')
    sort_countries[n].pop('Premium')
    n += 1
th_country = ["Країна🌍", "Нові підтверджені🆕 ", "Загальна к-ть",
              "Нові смерті💀", "Заг. к-ть смертей⚰️", "Нові одужані💪", "Заг. одужало😊"]

th_global = ["Нові підтверджені🆕", "Загальна к-ть", "Нові смерті💀",
             "Загальна к-ть смертей⚰️", "Нові одужані💪", "Загалом одужало😊"]


class GlobalCovid:

    def covid_view(self):
        global_str = ''
        i = 0
        for key in covid_global:
            global_str += f"🔹 <b>{th_global[i]}</b> ➖ <pre>{covid_global[key]}</pre>\n\n"
            i += 1
        return global_str


class CountriesSearh:

    def slected_country(self):
        countries_dict = sort_countries
        country_str = ''
        i = 0
        td = []
        country_name = 'Ukraine'
        while i < len(countries_dict):
            if countries_dict[i]["Slug"].lower() == country_name.lower():
                selected_country = countries_dict[i]
                for key in selected_country:
                    td.append(selected_country[key])
            i += 1
        n = 0
        while n < len(td):
            country_str += f"🔹 <b>{th_country[n]}</b> ➖ <pre>{td[n]}</pre>\n\n"
            n += 1
        return country_str


@bot.message_handler(commands=['start'])
def start(message):
    print("Start message")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn_1 = types.KeyboardButton("Ukraine")
    btn_2 = types.KeyboardButton("Belarus")
    btn_3 = types.KeyboardButton("Poland")
    btn_4 = types.KeyboardButton("Russia")
    btn_5 = types.KeyboardButton("Germany")
    btn_6 = types.KeyboardButton("Czech-Republic")
    btn_7 = types.KeyboardButton("Italy")
    btn_8 = types.KeyboardButton("Spain")
    btn_9 = types.KeyboardButton("United-States")
    btn_10 = types.KeyboardButton("Global")
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5,
               btn_6, btn_7, btn_8, btn_9, btn_10)
    send_mess = f"<b>Привіт {message.from_user.first_name} !</b>\nНатисни відповідну кнопку чи введи назву країни, поки тільки англійською"
    bot.send_message(message.chat.id, send_mess,
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ''
    get_message_bot = message.text.strip().lower()
    print(get_message_bot, " - ", message.from_user.first_name)
    if message.from_user.first_name != "ops_rv":
        access_file = open("access.log", "a")
        access_file.write(
            f"{datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')} - {message.from_user.first_name} {message.from_user.last_name} : {get_message_bot}\n")
    if get_message_bot == "global":
        global_inf = GlobalCovid()
        global_inf.covid_view()
        final_message = f'🦠 <b>Загальна статистика:</b>\n<i>інформація станом на: {date}</i>\n\n\n{global_inf.covid_view()}'
    elif get_message_bot == "ukraine":
        country_inf = CountriesSearh()
        final_message = f'🇺🇦\nМОЗ України:\n<i>інформація станом на: {date}</i>\n\n\n{country_inf.slected_country()}'
        # bot.send_photo(message.chat.id, open('images.png', 'rb'))
        # ПРИКЛАД ЯК РОБИТИ НЕ ТРЕБА!
    else:
        def slected_country():
            countries_dict = sort_countries
            country_str = ''
            i = 0
            td = []
            while i < len(countries_dict):
                if countries_dict[i]["Slug"].lower() == get_message_bot.lower():
                    selected_country = countries_dict[i]
                    for key in selected_country:
                        td.append(selected_country[key])
                i += 1
            n = 0
            while n < len(td):
                country_str += f"🔹 <b>{th_country[n]}</b> ➖ <pre>{td[n]}</pre>\n\n"
                n += 1
            return country_str
        final_message = f"{slected_country()}"
    bot.send_message(message.chat.id, final_message, parse_mode="html")


bot.polling(none_stop=True, interval=0)
