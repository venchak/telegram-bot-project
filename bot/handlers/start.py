from telegram import Update
from telegram.ext import CallbackContext

from bot.main import save_new_user

WELCOME_TEXT = (
    "Вітаю! Я бот для підбору автозапчастин.\n"
    "Скористайтесь /help, щоб побачити доступні команди."
)

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    save_new_user(
        user_id=user.id,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
    )
    update.message.reply_text(WELCOME_TEXT)
