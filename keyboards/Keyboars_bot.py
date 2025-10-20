from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def reply_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='узнать погоду')
    kb.button(text='последние новости')
    kb.button(text='настройки')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='Включить уведомления', callback_data='toggle'))
    builder.add(InlineKeyboardButton(text='Выключить уведомления', callback_data='off'))
    builder.add(InlineKeyboardButton(text='Готово', callback_data='save'))

    return builder.as_markup()





