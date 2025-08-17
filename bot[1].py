
import logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Read token from environment variable
TOKEN = os.environ.get("TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

START_TEXT = (
    "✅ GoldPowerSignalsBot активирован и готов слать тестовые сигналы.\n"
    "Команды:\n"
    "/signal — прислать тестовую карту/прогноз.\n"
    "/help — помощь."
)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(START_TEXT)

def help_cmd(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(START_TEXT)

def signal(update: Update, context: CallbackContext) -> None:
    # Simple test message that imitates the morning pack
    msg = (
        "✨ GoldPower AI (ТЕСТ)\n"
        "• Buy zone: 3336.5+\n"
        "• Sell zone: 3330.8-\n"
        "• Вероятность пробоя вверх: 38%\n"
        "• Вероятность пробоя вниз: 62%\n"
        "• План 15–30 мин: ждать выход из диапазона 3331–3338.\n"
        "\n"
        "Это тестовое сообщение. Когда подключим AI-сигналы — сюда будет приходить реальный прогноз."
    )
    update.message.reply_text(msg)

def main() -> None:
    if not TOKEN:
        raise RuntimeError("Не найден TOKEN в переменных окружения. Задайте TOKEN на платформе деплоя.")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_cmd))
    dp.add_handler(CommandHandler("signal", signal))

    # Long polling
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
