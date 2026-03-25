from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Вставьте сюда токен своего бота
TOKEN = "8719448745:AAFd-QjsODV4b3XiPUELHOtMUF00_vDdcc8"

# Словарь команд с HTML-разметкой
COMMANDS = {
    "💸 РЕКЛАМА": """💸 <b>Реклама в</b> @MagicTitans

📊 <b>Средние просмотры</b>: Х+

📦 <b>Форматы</b>:
— Пост 24 часа
— Закреп 12 часов

💰 <b>Цена</b>: Х₽

📩 <b>Пиши для покупки</b>: @Scryze""",

    "📦 ФОРМАТЫ": """📦 <b>Форматы рекламы</b>:

1️⃣ <b>Стандарт</b> — Х₽:
— Пост 24 часа
— Закреп 12 часов

2️⃣ <b>Долгий</b> — Х₽:
— Пост 48 часов
— Закреп 24 часа

3️⃣ <b>VIP</b> — Х₽:
— Закреп 48 часов
— + лучший слот по времени 🔥

📩 Напиши @Scryze — помогу выбрать формат""",

    "🔥 СКИДКИ": """🔥 <b>АКЦИИ</b>:

🎁 После покупки 2 реклам — бонус времени
🎁 Скидка 20% на всё (до 31.03.2026)

⚡ <b>Иногда делаю скидки</b> — уточняй в ЛС

📩 @Scryze""",

    "❓ FAQ": """❓ <b>Частые вопросы</b>:

— <b>Есть ли гарантия?</b>
👉 Да, пост держится указанное время

— <b>Можно ли удалить пост раньше?</b>
👉 Нет

— <b>Какие темы берёшь?</b>
👉 Игры / развлечения / телеграм проекты

— <b>Когда публикуешь?</b>
👉 По договорённости

📩 Остались вопросы? → @Scryze""",

    "📊 СТАТИСТИКА": """📊 <b>Статистика канала</b>:

👥 <b>Подписчики</b>: Х
👁 <b>Просмотры</b>: ~Х

📈 <b>Актив</b>: Х

📩 Могу скинуть скрины в ЛС → @Scryze""",

    "📩 СВЯЗЬ": """📩 <b>Связь</b>:

👉 @Scryze

⚡ Отвечаю обычно быстро"""
}

# Клавиатура с тегами
KEYBOARD = [
    ["💸 РЕКЛАМА", "📦 ФОРМАТЫ"],
    ["🔥 СКИДКИ", "❓ FAQ"],
    ["📊 СТАТИСТИКА", "📩 СВЯЗЬ"]
]

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_text = """🔥 <b>Привет! Я — бот. Я помогу тебе купить рекламу</b>

⚡ Я могу подсказать:
— 💰 Цену рекламы
— 📊 Статистику канала
— 📦 Выгодные предложения
— 🔥 Акции и скидки  
— ❓ Ответы на частые вопросы """
    
    reply_markup = ReplyKeyboardMarkup(KEYBOARD, resize_keyboard=True)
    await update.message.reply_text(start_text, reply_markup=reply_markup, parse_mode="HTML")

# Обработка нажатий кнопок
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in COMMANDS:
        await update.message.chat.send_action(action="typing")  # Показываем, что бот «печатает»
        await update.message.reply_text(COMMANDS[text], parse_mode="HTML")
    else:
        await update.message.reply_text("❌ Неизвестная команда. Выбери вариант из меню.")

# Создание приложения и запуск
import asyncio

if __name__ == "__main__":
    async def main():
        app = ApplicationBuilder().token(TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        print("Бот успешно запущен!")
        await app.run_polling()

    asyncio.run(main())
