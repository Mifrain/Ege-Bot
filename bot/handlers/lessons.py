from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

from keyboard.lessons_kb import lesson_kb, lesson_link_kb, choose_kb
from db import pydb

objects = {'rus': '🇷🇺 <b>Русский Язык</b> 🇷🇺', 'mathbase': '📐 <b>Математика База</b> 📐', 'mathprof': '🔢 <b>Математика Проф</b> 🔢', 'inf': '🖥 <b>Информатика</b> 🖥', 'is': '📖 <b>Итоговое Сочинение</b> 📖'}

async def les_call(call: CallbackQuery):
    await call.answer()
    # await call.message.delete()
    res = call.data.split('_')[1]
    obj = call.data.split('_')[0]
    txt = objects.get(obj)
    
    if res == 'les':
        await call.message.edit_text(f'{txt}', reply_markup=await choose_kb(obj))
        
    # Прототипы
    elif res == 'prot':
        await call.message.edit_text(f'{txt}\n\n<b>Прототипы🧾:</b>', reply_markup= await lesson_kb(obj, 'prot'))
        
    elif res == 'protpage':
        page = call.data.split('_')[2]
        await call.message.edit_text(f'{txt}\n\n<b>Прототипы🧾:</b>', reply_markup= await lesson_kb(obj, 'prot', page))
        
    elif res == 'protnum':
        await call.message.edit_text(f'{txt}\n\n<b>Номер {call.data.split("_")[2]}\n</b>', reply_markup= await lesson_link_kb(call.data, 'prot', call.from_user.id))


    # Материалы
    elif res == 'mat':
        await call.message.edit_text(f'{txt}\n\n<b>Материалы 📁:</b>', reply_markup= await lesson_kb(obj, 'mat'))
        
    elif res == 'matpage':
        page = call.data.split('_')[2]  
        await call.message.edit_text(f'{txt}\n\n<b>Материалы 📁:</b>', reply_markup= await lesson_kb(obj, 'mat', page))

    elif res == 'matnum':
        name = pydb.name_lesson(call.data)
        await call.message.edit_text(f'{txt}\n\n<b>{name}</b>', reply_markup= await lesson_link_kb(call.data, 'mat', call.from_user.id))

    
    
    # Тесты 
    elif res == 'test':
        await call.message.edit_text(f'{txt}', reply_markup=await choose_kb(obj))


        

def lessons_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(les_call)

