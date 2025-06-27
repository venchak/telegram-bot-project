
from dotenv import load_dotenv
import os
from database import init_db, SessionLocal, User

init_db()

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")


def save_new_user(user_id, username, first_name=None, last_name=None):
    """Зберегти нового користувача, якщо його ще немає в БД."""
    session = SessionLocal()
    if not session.query(User).filter_by(id=user_id).first():
        new_user = User(
            id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        session.add(new_user)
        session.commit()
    session.close()


def main():
    print("Hello from Telegram bot project")


if __name__ == "__main__":
    main()
