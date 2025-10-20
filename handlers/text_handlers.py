import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F, Router
from keyboards.Keyboars_bot import reply_keyboard
from keyboards.Keyboars_bot import inline_keyboard
import random

router = Router()
cities = {
    'Москва': '15°С',
    'Грозный': '7°С',
    'Махачкала': '12°C',
}

news = [
    'Европейская комиссия запустит программу "Космический Щит" во второй половине 2026 года. \n'
    'Проект защитит спутники ЕС от глушения сигналов и подделки данных. \n'
    'На реализацию потребуется несколько лет и миллиарды евро.',
    'Палеонтологи обнаружили в Аргентине кости одного из древнейших динозавров возрастом около 230-225 млн лет. \n'
    'Новый вид получил название Huayracursor jaguensis, \n'
    'он отличается длинной шеей и крупным размером — длина особи достигает двух метров.',
    'Продажи портативных колонок в России этим летом сократились на восемь процентов. \n'
    'Россияне приобрели 870 тысяч устройств на четыре миллиарда рублей. \n'
    'Важным критерием выбора стала возможность голосового управления через ИИ-ассистентов.',
    'Дагестанские учёные усердно потрудились и в итоге открыли огонь по нефрам',
    'Расскрыта величайшая тайна. Барсук Евгений...'
]

user = {}
nott = {}

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        'Выберите пункт!',
        reply_markup=reply_keyboard()
    )

@router.message(F.text.lower() == 'узнать погоду')
async def check_weather(message: types.Message):
    user_id = message.from_user.id
    user[user_id] = 'wait'
    await message.answer(
        'Введите город: ',
        reply_markup=types.ReplyKeyboardRemove()
    )

@router.message(F.text.in_(cities.keys()))
async def get_cities(message: types.Message):
    city = message.text.lower()
    user_id = message.from_user.id

    if user.get(user_id) == 'wait':

        found_city = None
        for city1 in cities.keys():
            if city1.lower() == city.lower():
                found_city = city1
                break

        if found_city:
            await message.answer(f'В {found_city} - {cities[found_city]}')
        else:
            message.answer('Город не найден. Повторите попытку')

@router.message(Command("cancel"))
async def cancel(message: types.Message):
    user_id = message.from_user.id
    if user_id in user:
        user[user_id] = None
        await message.answer(
            'Просмотр погоды отключён'
        )

@router.message(F.text.lower() == 'последние новости')
async def chech_news(message: types.Message):
    ran = random.randint(1, len(news) - 1)
    if ran == 4:
        msg = await message.answer(
            f'Новость года! - {news[ran]}')
        await asyncio.sleep(2)
        await msg.delete()
        await message.answer(
            'Неважно'
        )
    else:
        await message.answer(
            f'Новости - {news[ran]}')

@router.message(F.text.lower() == 'настройки')
async def settings(message: types.Message):
    user_id = message.from_user.id
    status = nott.get(user_id, True)
    text = 'Уведомления включены' if status else 'Уведомления выключены'


    await message.answer(
        text,
        reply_markup=inline_keyboard()
    )

@router.callback_query(F.data.in_(['toggle', 'off']))
async def toggle(call: types.CallbackQuery):
    await call.answer()

    user_id = call.from_user.id

    if call.data.lower() == 'toggle':
        nott[user_id] = True
        text = 'Уведомления включены'
    else:
        nott[user_id] = False
        text = 'Уведомления выключены'

    await call.message.edit_text(text, reply_markup=inline_keyboard())

@router.callback_query(F.data == 'save')
async def save(call: types.CallbackQuery):
    await call.answer('Настройки завершены')
    await call.message.delete()