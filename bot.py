import os

from dotenv import load_dotenv

load_dotenv()

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)


# Token Telegram
TOKEN = os.getenv("TELEGRAM_TOKEN")


# URL de ta Mini App Render
WEB_APP_URL = "https://mini-app-telegram-04nu.onrender.com"


# Administrateurs
ADMIN_IDS = [
    8906241208,
    8702997904
]


# -------------------------
# COMMANDES
# -------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                text="🚀 Ouvrir la boutique",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]

    await update.message.reply_text(
        "Bienvenue 👋\n\n"
        "Clique sur le bouton pour accéder à la boutique :",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Commandes disponibles :\n"
        "/start - Ouvrir la boutique\n"
        "/help - Aide\n"
        "/admin - Administration"
    )


async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if user_id not in ADMIN_IDS:
        await update.message.reply_text(
            "❌ Accès refusé."
        )
        return

    await update.message.reply_text(
        "✅ Bienvenue dans le panneau administrateur."
    )


# -------------------------
# DEMARRAGE BOT
# -------------------------

def main():

    if not TOKEN:
        raise ValueError(
            "TELEGRAM_TOKEN manquant dans les variables d'environnement"
        )


    app = ApplicationBuilder().token(TOKEN).build()


    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("admin", admin_command))


    print("Bot Telegram démarré ✅")


    app.run_polling()


if __name__ == "__main__":
    main()