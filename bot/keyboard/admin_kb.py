from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from db import pydb


# Администраторы
async def admin_kb(user_id):    
    kb = InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton('Прототипы 📝', callback_data='adm_prot_choose'),
        InlineKeyboardButton('Материалы 📁', callback_data='adm_mat_choose')
    )
    if pydb.user_is_main_admin(user_id):
        kb.row(
            InlineKeyboardButton('✅ Добавить Админа 👥', callback_data='adm_admin_add'),
            InlineKeyboardButton('❌ Удалить Админа 👤', callback_data='adm_admin_del')).add(InlineKeyboardButton('🔔 Оповестить всех 🔔', callback_data='adm_send'))
    kb.add(InlineKeyboardButton('Главное меню 🏠', callback_data='menu_main'))
    return kb

admin_back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('❌ Назад ❌', callback_data='adm_main'))

async def del_adm_kb(page=0):
    kb = InlineKeyboardMarkup(row_width=1)
    admins = pydb.all_admins()
    
    page = int(page)
    
    for btn in range(5*page, 5*page + 5 if 5*page + 5 < len(admins) else len(admins)):
        kb.add(InlineKeyboardButton(f'❌ {admins[btn][0]} ❌', callback_data=f'adm_admin_delid_{admins[btn][0]}'))
        
    kb.row(
        InlineKeyboardButton('⬅' if page-1 >= 0 else '❌', callback_data=f'adm_admin_delpage_{page-1 if page-1 >= 0 else page}'),
        InlineKeyboardButton('Назад', callback_data=f'adm_main'),
        InlineKeyboardButton('➡' if 5*(page+1) <= len(admins) else '❌', callback_data=f'adm_admin_delpage_{page+1 if 5*(page+1) <= len(admins) else page}')
    )
    return kb

# ПРОТИТИПЫ
def admin_les_kb(type):
    return InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton('✅ Добавить ✅', callback_data=f'adm_{type}_add'), InlineKeyboardButton('❌ Удалить ❌', callback_data=f'adm_{type}_del'), InlineKeyboardButton('Назад', callback_data='adm_main'))

