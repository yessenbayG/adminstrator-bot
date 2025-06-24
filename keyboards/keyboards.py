from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Клавиатура выбора формата занятия -------

button_online = KeyboardButton(text='Онлайн')
button_office = KeyboardButton(text='В офисе')

format_kb = ReplyKeyboardMarkup(
    keyboard=[[button_online, button_office]],
    resize_keyboard=True
)

# ------- Клавиатура выбора времени занятия -------

button_10 = KeyboardButton(text='10:00')
button_14 = KeyboardButton(text='14:00')
button_18 = KeyboardButton(text='18:00')

time_kb = ReplyKeyboardMarkup(
    keyboard=[[button_10, button_14, button_18]],
    resize_keyboard=True
)

# ------- Клавиатура подтверждения записи -------

button_yes = KeyboardButton(text='✅ Да')
button_change = KeyboardButton(text='🔄 Изменить')

confirm_kb_builder = ReplyKeyboardBuilder()
confirm_kb_builder.row(button_yes, button_change, width=2)

confirm_kb = confirm_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)
