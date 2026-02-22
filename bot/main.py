from telegram.ext import (Updater,
                          MessageHandler,
                          CommandHandler)
from bot.handlers.command_handlers import command_handler
from bot.config.settings import settings

def main() -> None:
    updater = Updater(settings.BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', callback=command_handler.start)
    )

    updater.start_polling()
    updater.idle()