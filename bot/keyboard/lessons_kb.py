from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from db import pydb


async def choose_kb(type):
    return InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton('Прототипы 🧾', callback_data=f'{type}_prot'),
                                    InlineKeyboardButton('Материалы 📁', callback_data=f'{type}_mat')
                                    ).add(InlineKeyboardButton('К Предметам 📚', callback_data='menu_edc'))


async def sort_lessons(lessons):
    for i in range(len(lessons) - 1):
        for j in range(i + 1, len(lessons)):
            try:
                if int(lessons[i][0].split(' ')[1]) >= int(lessons[j][0].split(' ')[1]):
                    lessons[i], lessons[j] =  lessons[j], lessons[i]
            except:
                continue
    
    return lessons


# Клавиатура с заданиями(Адаптирована)
async def lesson_kb(obj, type, page=0):
    kb = InlineKeyboardMarkup(row_width=1)
    lessons_nots = pydb.obj_lesson(obj, type)
    lessons = await sort_lessons(lessons_nots)
        
    page = int(page)

    for btn in range(5*page, 5*page + 5 if 5*page + 5 < len(lessons) else len(lessons)):
        kb.add(InlineKeyboardButton(lessons[btn][0], callback_data=lessons[btn][1]))
        
    kb.row(
        InlineKeyboardButton('⬅' if page-1 >= 0 else '❌', callback_data=f'{obj}_{type}page_{page-1 if page-1 >= 0 else page}'),
        InlineKeyboardButton('🗂Назад🗂', callback_data=f'{obj}_les'),
        InlineKeyboardButton('➡' if 5*(page+1) < len(lessons) else '❌', callback_data=f'{obj}_{type}page_{page+1 if 5*(page+1) < len(lessons) else page}')
    )
    kb.add(InlineKeyboardButton('К Предметам 📚', callback_data='menu_edc'))
    return kb
 
 
# Само задание
async def lesson_link_kb(callback:str, type, user_id=None, fromm=None):
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton('Файл 📄', url=pydb.select_file(callback)),
        InlineKeyboardButton('Добавить в Избранное ❤️', callback_data=f'like/add/{callback}/{fromm}') if not pydb.check_like_lesson(user_id, callback) else InlineKeyboardButton('Удалить из Избранного 💔', callback_data=f'like/del/{callback}/{fromm}'),
        InlineKeyboardButton('❌ Назад ❌', callback_data=f'{callback.split("_")[0]}_{type}' if fromm != 'likes' else 'menu_likes')
    )
    
    
# Избранные задания
async def lesson_like_kb(user_id, page=0):
    
    lessons = pydb.all_like_lesson(user_id)
    kb = InlineKeyboardMarkup()
    page = int(page)
    
    for btn in range(5*page, 5*page + 5 if 5*page + 5 < len(lessons) else len(lessons)):
        kb.add(InlineKeyboardButton(pydb.name_lesson(lessons[btn][1]), callback_data=f'like/num/{lessons[btn][1]}/likes'))
        
    kb.row(
        InlineKeyboardButton('⬅' if page-1 >= 0 else '❌', callback_data=f'menu_likes_page_{page-1 if page-1 >= 0 else page}'),
        InlineKeyboardButton('🗂Назад🗂', callback_data=f'menu_main'),
        InlineKeyboardButton('➡' if 5*(page+1) < len(lessons) else '❌', callback_data=f'menu_likes_page_{page+1 if 5*(page+1) < len(lessons) else page}')
    )
    return kb

                                                      
    
