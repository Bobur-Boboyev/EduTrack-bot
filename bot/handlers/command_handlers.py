from telegram import (
    Update,
)
from telegram.ext import (
    CallbackContext
)

class CommandHandler:
    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text("Hello")
    

command_handler = CommandHandler()