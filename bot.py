from dotenv import load_dotenv
import os

load_dotenv()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token du bot
TOKEN = os.getenv("TELEGRAM_TOKEN")

# URL HTTPS de ta Mini App
WEB_APP_URL = "https://mini-app-telegram-04nu.onrender.com"

# Administrateurs du bot (ID Telegram)
ADMIN_IDS = [
    8906241208,  # ton ID
    8702997904   # ID du deuxième administrateur
]

async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ Tu n'es pas administrateur.")
        return

    await update.message.reply_text("✅ Bienvenue dans le panneau admin.")


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