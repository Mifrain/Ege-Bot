# 📚 EGE-Bot — Telegram-бот для подготовки к ЕГЭ

[Перейти в Telegram →](https://t.me/mifege_bot)

Бот помогает школьникам готовиться к ЕГЭ, предоставляя разнообразные материалы, шаблоны заданий и удобную навигацию. Всё в одном месте!

---

## 🚀 Features

- 📂 Много материалов для подготовки к ЕГЭ
- 🧩 Шаблоны заданий (task prototypes)
- 🧾 Вся информация по запросу — в одном сообщении
- ⭐ Возможность сохранять избранные материалы

---

## 🛠️ Технологии

- Python 3.10+
- [Aiogram](https://docs.aiogram.dev/) — асинхронный Telegram-фреймворк
- Машина состояний (FSM)
- Telegram Bot API

---

## 📦 Установка и запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/Mifrain/Ege-Bot.git
cd Ege-Bot
```

### 2. Создай и активируй виртуальное окружение

**На Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**На macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установи зависимости

```bash
pip install -r requirements.txt
```

### 3. Настрой конфигурацию

В файле `bot/config.py` укажи токен своего Telegram-бота:

```python
token = "your_token"
```

Получить токен можно у [@BotFather](https://t.me/BotFather)

### 4. Запусти бота

```bash
python bot/run.py
```

---

## 📁 Структура проекта

```
Ege-Bot/
├── bot/
│   ├── main.py            # Инициализация
│   ├── run.py             # Запуск бота
│   ├── config.py          # Telegram API токен
│   ├── keyboards.py       # Кастомные клавиатуры
│   ├── states.py          # FSM-состояния
│   └── handlers/          # Обработчики логики и команд
│       ├── __init__.py
│       └── ...
├── requirements.txt       # Зависимости проекта
```
