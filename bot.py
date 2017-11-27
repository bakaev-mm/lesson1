# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, settings, ephem
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(bot, update):
    text = '''Привет {}!
Я простой бот и понимаю команду /start'''.format(update.message.chat.first_name)
    logging.info(text)
    update.message.reply_text(text)

def chat(bot, update):
    user_text = update.message.text 
    logging.info(user_text)
    update.message.reply_text(user_text)

def planet(bot, update, args):
    today = '2017/11/25'
    try:
        planet = args[0].lower()
        if planet in ['марс', 'mars']:
            planet = ephem.Mars(today)
            const = ephem.constellation(planet)[1]
        elif planet in ['венера''venus']:
            planet = ephem.Venus(today)
            const = ephem.constellation(planet)[1]
        else:
            const = "Not known"
        
        update.message.reply_text(const)
    except:
        update.message.reply_text("Укажи планету")

def wordcount(bot, update, args):
    user_text = args
    update.message.reply_text(len(user_text))

def calc(bot, update, args):
    calc = args
    text = ('update.message.reply_text(' + calc[0]+')')
    tesult = exec(text)
    update.message.reply_text(str(result))

    

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    updater = Updater(settings.TELEGRAM_API_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_bot))
    dp.add_handler(CommandHandler("planet", planet, pass_args=True))
    dp.add_handler(CommandHandler("wordcount", wordcount, pass_args=True))
    dp.add_handler(CommandHandler("calc", calc, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, chat))
    updater.start_polling()
    updater.idle()

# Вызываем функцию - эта строчка собственно запускает бота
if __name__ == '__main__':
    logging.info('bot_started')
    main()