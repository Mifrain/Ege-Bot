from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

from keyboard.client_kb import *
from keyboard.lessons_kb import *
from db import pydb
from handlers.lessons import objects

async def default_commands(mess: Message):
    if mess.text == '/start':
        if not pydb.check_user(mess.from_user.id):
            pydb.add_user(mess.from_user.id)
        await mess.answer('<b>Привет!\nЭтот бот поможет тебе со сдачей ЕГЭ по разным предметам📚!\nЗдесь ты найдешь много нужных материалов и прототипов📁!\n\nЖелаю хороших результатов!</b>', reply_markup=start_kb)
    await mess.delete()


async def menu_callbackes(call: CallbackQuery):
    # await call.message.delete()
    await call.answer()
    res = call.data.split('_')[1]
    if res == 'main':
        await call.message.edit_text('🏠<b>Главное Меню</b>🏠', reply_markup=await main_kb(call.from_user.id))
    elif res == 'edc':
        await call.message.edit_text('<b>Выбери предмет для получения материалов</b>📚\n\n<i>Предмет ты можешь менять в любое время</i>', reply_markup=lessons_kb)
    elif res == 'prof':
        await call.message.edit_text(f"""<b>• Ваш профиль 👤
  ❯ Имя {(call.from_user.username).replace('<', '').replace('>', '')}
  ❯ ID {call.from_user.id}</b>""", reply_markup=menu_back_kb)
    elif res == 'likes':
        if 'page' in call.data:
            page = call.data.split('_')[3]
        else:
            page = 0
        await call.message.edit_text(f'<b>Избранные Материалы ❤️</b>', reply_markup=await lesson_like_kb(call.from_user.id, page))
    elif res == 'sup':
        await call.message.edit_text('По всем вопросам обращайтесь к @mifrain_pr', reply_markup=menu_back_kb)



async def like_change(call: CallbackQuery):
    type = call.data.split('/')[1]
    less_call = call.data.split('/')[2]
    fromm = call.data.split('/')[3]
    
    less_type = 'prot'
    if 'mat' in less_call: less_type = 'mat'
    
    obj = less_call.split('_')[0]
    txt = objects.get(obj)
    name = pydb.name_lesson(less_call)

    
    if type == 'add':
        await call.answer('✅ Материал добавлен в Избранные ❤️ ✅', show_alert=True)
        pydb.add_like_lesson(call.from_user.id, less_call)
        await call.message.edit_text(f'{txt}\n\n<b>{name}</b>', reply_markup= await lesson_link_kb(less_call, less_type, call.from_user.id, fromm))

    elif type == 'del': 
        await call.answer('❌ Материал удален из Избранных 💔 ❌', show_alert=True)
        pydb.del_like_lesson(call.from_user.id, less_call)
        await call.message.edit_text(f'{txt}\n\n<b>{name}</b>', reply_markup= await lesson_link_kb(less_call, less_type, call.from_user.id, fromm))

    
    else:
        await call.answer()
        await call.message.edit_text(f'{txt}\n\n<b>{name}</b>', reply_markup= await lesson_link_kb(less_call, less_type, call.from_user.id, 'likes'))

 
    
    
    


def client_handlers(dp: Dispatcher):
    dp.register_message_handler(default_commands, commands=['start', 'help'])
    dp.register_callback_query_handler(menu_callbackes, Text(startswith='menu_'))
    dp.register_callback_query_handler(like_change, Text(startswith='like'))
