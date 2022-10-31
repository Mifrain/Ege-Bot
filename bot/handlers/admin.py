from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext


from states import admin_states
from keyboard.client_kb import *
from keyboard.admin_kb import *
from db import pydb



async def admin_menu(call: CallbackQuery):
    await call.message.delete()
    await call.answer()
    res = call.data.split('_')[1]
    if res == 'main':
        await call.message.answer('<b>⚒ Панель Администратора ⚒</b>', reply_markup=await admin_kb(call.from_user.id))
        
    elif res == 'admin':
        opt = call.data.split('_')[2]
        if opt == 'add':
            await call.message.answer('<b>Введите ID нового администратора</b>', reply_markup=admin_back_kb)
            await admin_states.AddAdminState.adm_id.set()
        elif opt == 'del':
            await call.message.answer('<b>Нажмите на ID Администратора, которого собираетесь удалить</b>', reply_markup=await del_adm_kb())
        elif opt == 'delpage':
            page = call.data.split('_')[3]
            await call.message.answer(f'<b>Нажмите на ID Администратора, которого собираетесь удалить</b>', reply_markup= await del_adm_kb(page))
        elif opt == 'delid':
            admin_id = call.data.split('_')[3]
            pydb.user_del_admin(admin_id)
            await call.message.answer('✅ <b>Администратор Удален👤</b> ✅', reply_markup=admin_back_kb)
        
    elif res == 'prot':
        opt = call.data.split('_')[2]
        if opt == 'choose':
            await call.message.answer('<b>Редактирование Прототипов🧾</b>', reply_markup=admin_les_kb('prot'))
        elif opt == 'add':
            await call.message.answer('<b>Введите через запятую тип, имя, callback прототипа</b>\n\n<i>Пример: rus, Номер 8, rus_protnum_8, ссылка на файл</i>\n\nТипы:\nРусский Язык - rus\nМатематика База - mathbase\nМатематика Профиль - mathprof\nИнформатика - inf\nИтоговое Сочинение - is', reply_markup=admin_back_kb)
            await admin_states.AddProtState.new_prot.set()
        elif opt == 'del':
            await call.message.answer('<b>Введите через callback прототипа, чтобы удалить его</b>\n\n<i>Пример: rus_protnum_8</i>', reply_markup=admin_back_kb)
            await admin_states.DelProtState.del_prot.set()
            
    elif res == 'mat':
        opt = call.data.split('_')[2]
        if opt == 'choose':
            await call.message.answer('<b>Редактирование Материалов📁</b>', reply_markup=admin_les_kb('mat'))
        elif opt == 'add':
            await call.message.answer('<b>Введите через запятую тип, имя, callback, файл прототипа</b>\n\n<i>Пример: rus, Номер 8, rus_matnum_8, ссылка на файл</i>\n\nТипы:\nРусский Язык - rus\nМатематика База - mathbase\nМатематика Профиль - mathprof\nИнформатика - inf\nИтоговое Сочинение - is', reply_markup=admin_back_kb)
            await admin_states.AddMatState.new_mat.set()
        elif opt == 'del':
            await call.message.answer('<b>Введите через callback прототипа, чтобы удалить его</b>\n\n<i>Пример: rus_matnum_8</i>', reply_markup=admin_back_kb)
            await admin_states.DelMatState.del_mat.set()



# STATES
async def add_admin(mess: Message, state=FSMContext):
    pydb.user_add_admin(mess.text)
    await mess.answer('✅ <b>Администратор Добавлен👥 </b>✅', reply_markup=admin_back_kb)
    await mess.delete()
    await state.finish()


async def back_admin_state(call: CallbackQuery,state=FSMContext):
    await call.answer()
    await call.message.delete()
    await call.message.answer('<b>⚒ Панель Администратора ⚒</b>', reply_markup=await admin_kb(call.from_user.id))
    await state.finish()


async def change_les(mess: Message, state=FSMContext):
    prot = mess.text.split(',')
    opt =str(await state.get_state(FSMContext)).split(':')[1].split('_')
    if opt[0] == 'new':
        while len(prot) != 4:
            await mess.delete()
            if opt[1] == 'prot':
                await mess.answer('❗️<b>Введите согласно примеру</b>❗️\n\n<i>Пример: rus, Номер 8, rus_protnum_8, ссылка на файл</i>',  reply_markup=admin_back_kb)
            elif opt[1] == 'mat':
                await mess.answer('❗️<b>Введите согласно примеру</b>❗️\n\n<i>Пример: rus, Номер 8, rus_matnum_8, ссылка на файл</i>',  reply_markup=admin_back_kb)                
            await admin_states.AddProtState.first()
            break
        
        else:
            # Привожу к нижнему регистру и убираю пробелы
            prot[0] = prot[0].lower().replace(' ', '')
            prot[1] = prot[1].replace(' ', '', 1)
            prot[2] = prot[2].lower().replace(' ', '')
            prot[3] = prot[3].replace(' ', '')
            
            if opt[1] == 'prot':
                pydb.add_lesson(prot, 'prot')
                await mess.answer('✅ <b>Прототип Добавлен🧾</b>✅', reply_markup=admin_back_kb)
            elif opt[1] == 'mat':
                pydb.add_lesson(prot, 'mat')
                await mess.answer('✅ <b>Материал Добавлен📁</b>✅', reply_markup=admin_back_kb)
            await mess.delete()
            await state.finish()
    elif opt[0] == 'del':
        pydb.del_lesson(prot[0])
        if opt[1] == 'prot':
            await mess.answer('✅ <b>Прототип Удален🧾</b>✅', reply_markup=admin_back_kb)
        elif opt[1] == 'mat':
            await mess.answer('✅ <b>Материал Удален📁</b>✅', reply_markup=admin_back_kb)
        await mess.delete()
        await state.finish()

    





def admin_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(back_admin_state, state = admin_states.AddAdminState.adm_id)
    dp.register_callback_query_handler(back_admin_state, state = admin_states.AddProtState.new_prot)
    dp.register_callback_query_handler(back_admin_state, state = admin_states.DelProtState.del_prot)
    dp.register_callback_query_handler(back_admin_state, state = admin_states.AddMatState.new_mat)
    dp.register_callback_query_handler(back_admin_state, state = admin_states.DelMatState.del_mat)
    
    dp.register_callback_query_handler(admin_menu, Text(startswith='adm_'))
    
    dp.register_message_handler(add_admin, state = admin_states.AddAdminState.adm_id)
    
    dp.register_message_handler(change_les, state = admin_states.AddProtState.new_prot)
    dp.register_message_handler(change_les, state = admin_states.DelProtState.del_prot)
    dp.register_message_handler(change_les, state = admin_states.AddMatState.new_mat)
    dp.register_message_handler(change_les, state = admin_states.DelMatState.del_mat)



