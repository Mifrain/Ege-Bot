from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from db import pydb


start_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Продолжить', callback_data='menu_main'))

 # Основное Меню
async def main_kb(user_id):
    kb = InlineKeyboardMarkup(row_width=2).add(
            InlineKeyboardButton('Предметы 📚', callback_data='menu_edc'),
            InlineKeyboardButton('Профиль 👤', callback_data='menu_prof'),
            InlineKeyboardButton('Стастистика Бота 📊', callback_data='menu_stat'),
            InlineKeyboardButton('Поддержка 🆘', callback_data='menu_sup')
        )
    # Клавиша для Админов
    if pydb.user_is_admin(user_id) == 1:
        kb.row(InlineKeyboardButton('⚒ Администрирование ⚒', callback_data='adm_main'))
        
    return kb
        

menu_back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('❌ Назад ❌', callback_data='menu_main'))


# Выбор Предметов
lessons_kb = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton('Математика База 📐', callback_data='mathbase_les'),
    InlineKeyboardButton('Математика Проф 🔢', callback_data='mathprof_les'),
    InlineKeyboardButton('Русский Язык 🇷🇺', callback_data='rus_les'),
    InlineKeyboardButton('Информатика 🖥', callback_data='inf_les'),
    InlineKeyboardButton('Итоговое Сочинение 📖', callback_data='is_les')
)
lessons_kb.row(InlineKeyboardButton('Главное меню 🏠', callback_data='menu_main'))


