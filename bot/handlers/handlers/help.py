from telegram import Update
from telegram.ext import CallbackContext

HELP_TEXT = (
    "Доступні команди:\n"
    "/start - почати роботу з ботом\n"
    "/help - показати це повідомлення"
)

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(HELP_TEXT)
