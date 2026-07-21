from dotenv import load_dotenv
import os

load_dotenv()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token du bot
TOKEN = os.getenv("8956683379:AAGFOuzE3X6Qxi9VVlp_vbi7OlQAHaaDnz8")

# URL HTTPS de ta Mini App
WEB_APP_URL = "https://ton-application.onrender.com"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton(
            text="🚀 Ouvrir l'application",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
    ]]

    await update.message.reply_text(
        text="Bienvenue ! Clique sur le bouton ci-dessous pour ouvrir l'application.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Ouvrir la Mini App\n"
        "/help - Afficher l'aide"
    )


def main():
    if not TOKEN:
        raise ValueError(
            "La variable d'environnement TELEGRAM_TOKEN n'est pas définie."
        )

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot démarré...")
    app.run_polling()


if __name__ == "__main__":
    main()