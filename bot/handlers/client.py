from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

from keyboard.client_kb import *
from db import pydb

async def default_commands(mess: Message):
    if mess.text == '/start':
        if not pydb.check_user(mess.from_user.id):
            pydb.add_user(mess.from_user.id)
        await mess.answer('<b>Добро Пожаловать в Бота для подготовки к ЕГЭ</b>\n\n<b>Хороших результатов!</b>', reply_markup=start_kb)
    await mess.delete()


async def menu_callbackes(call: CallbackQuery):
    await call.message.delete()
    await call.answer()
    res = call.data.split('_')[1]
    if res == 'main':
        await call.message.answer('🏠<b>Главное Меню</b>🏠', reply_markup=await main_kb(call.from_user.id))
    elif res == 'edc':
        await call.message.answer('<b>Выбери предмет для получения материалов</b>📚\n\n<i>Предмет ты можешь менять в любое время</i>', reply_markup=lessons_kb)
    elif res == 'prof':
        await call.message.answer(f"""<b>• Ваш профиль 👤
  ❯ Имя {call.from_user.username}
  ❯ ID {call.from_user.id}
  ❯ Решено тестов - 0</b>""", reply_markup=menu_back_kb)
    elif res == 'stat':
        await call.message.answer(f'<b>• Статистика Бота: 📊\n  ❯ Пользователей с нами - {len(pydb.all_users())}</b>', reply_markup=menu_back_kb)
    elif res == 'sup':
        await call.message.answer('По всем вопросам обращайтесь к @mifrain_pr', reply_markup=menu_back_kb)


def client_handlers(dp: Dispatcher):
    dp.register_message_handler(default_commands, commands=['start', 'help'])
    dp.register_callback_query_handler(menu_callbackes, Text(startswith='menu_'))
