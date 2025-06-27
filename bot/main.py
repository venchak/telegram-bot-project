
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

def main():
    print("Hello from Telegram bot project")


if __name__ == "__main__":
    main()
