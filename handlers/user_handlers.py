from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import format_kb, time_kb, confirm_kb
from lexicon.lexicon_ru import LEXICON_RU

router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=format_kb)


# Хэндлер выбора формата занятия
@router.message(F.text.in_(['Онлайн', 'В офисе']))
async def process_format_choice(message: Message):
    if message.text == 'Онлайн':
        await message.answer(text=LEXICON_RU['Онлайн'], reply_markup=time_kb)
    else:
        await message.answer(text=LEXICON_RU['В офисе'], reply_markup=time_kb)


# Хэндлер выбора времени занятия
@router.message(F.text.in_(['10:00', '14:00', '18:00']))
async def process_time_choice(message: Message):
    await message.answer(
        text=f'Вы выбрали время: {message.text}\nВсё верно?',
        reply_markup=confirm_kb
    )


# Хэндлер подтверждения записи
@router.message(F.text == '✅ Да')
async def process_confirmation(message: Message):
    await message.answer(
        text='Отлично! Вы записаны. За 30 минут до занятия придет напоминание.'
    )


# Хэндлер на изменение данных
@router.message(F.text == '🔄 Изменить')
async def process_change(message: Message):
    await message.answer(
        text='Давайте начнем заново. Выберите удобный формат занятия:',
        reply_markup=format_kb
    )

# Хэндлер на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer('Я помогу вам записаться на бесплатное пробное занятие.\nЕсли у вас есть вопросы, напишите их.\nЧастые вопросы: "Где офис?" или "Сколько стоит?"')

# Хэндлер на вопрос об адресе
@router.message(F.text.lower().in_(['где офис', 'адрес', 'как найти', 'где вы находитесь']))
async def process_address_question(message: Message):
    await message.answer(LEXICON_RU['FAQ_адрес'])

# Хэндлер на вопрос о стоимости
@router.message(F.text.lower().in_(['сколько стоит', 'цена', 'стоимость', 'платно']))
async def process_price_question(message: Message):
    await message.answer(LEXICON_RU['FAQ_стоимость'])

# Хэндлер на непонятные сообщения
@router.message()
async def process_other_message(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
