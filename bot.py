# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, settings
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def start_bot(bot, update):
    text = '''Привет {}!
Я простой бот и понимаю команду /start'''.format(update.message.chat.first_name)
    logging.info(text)
    update.message.reply_text(text)

def chat(bot, update):
    user_text = update.message.text 
    logging.info(user_text)
    update.message.reply_text(user_text)

def main():
    updater = Updater(settings.TELEGRAM_API_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_bot))
    dp.add_handler(MessageHandler(Filters.text, chat))
    updater.start_polling()
    updater.idle()

# Вызываем функцию - эта строчка собственно запускает бота
if __name__ == '__main__':
    logging.info('bot_started')
    main()