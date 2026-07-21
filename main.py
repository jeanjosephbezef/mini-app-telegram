import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

# Token Telegram récupéré depuis une variable d'environnement
TOKEN = os.getenv("TELEGRAM_TOKEN")

WEB_APP_URL = "https://mini-app-telegram-04nu.onrender.com"


async def start(update, context):

    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Ouvrir la Mini App",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Bienvenue 👋",
        reply_markup=reply_markup
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commandes disponibles :\n"
        "/start\n"
        "/help\n"
        "/admin"
    )


async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commande administrateur"
    )


def main():
    if not TOKEN:
        raise ValueError(
            "La variable d'environnement TELEGRAM_TOKEN n'est pas définie."
        )

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("admin", admin_command))

    print("Bot démarré...")
    app.run_polling()


if __name__ == "__main__":
    main()