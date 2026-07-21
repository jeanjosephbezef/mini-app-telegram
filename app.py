import os
import threading
import asyncio

from flask import Flask, send_from_directory
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


TOKEN = os.getenv("TELEGRAM_TOKEN")

WEB_APP_URL = "https://mini-app-telegram-04nu.onrender.com"


app = Flask(__name__, static_folder="webapp")


# ----------------------
# MINI APP
# ----------------------

@app.route("/")
def home():
    return send_from_directory("webapp", "index.html")


@app.route("/<path:path>")
def files(path):
    return send_from_directory("webapp", path)



# ----------------------
# BOT TELEGRAM
# ----------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [[
        InlineKeyboardButton(
            "🚀 Ouvrir la boutique",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
    ]]

    await update.message.reply_text(
        "Bienvenue 👋\nOuvre ta boutique ici :",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "/start\n/help"
    )


async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Admin OK ✅"
    )



def run_bot():

    async def bot_main():

        bot = ApplicationBuilder().token(TOKEN).build()

        await bot.bot.delete_webhook(
            drop_pending_updates=True
        )

        bot.add_handler(
            CommandHandler("start", start)
        )

        bot.add_handler(
            CommandHandler("help", help_command)
        )

        bot.add_handler(
            CommandHandler("admin", admin_command)
        )

        print("Bot Telegram démarré ✅")

        await bot.initialize()
        await bot.start()
        await bot.updater.start_polling()

        await asyncio.Event().wait()


    asyncio.run(bot_main())



# Lancer le bot une seule fois
threading.Thread(
    target=run_bot,
    daemon=True
).start()



# ----------------------
# RENDER
# ----------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )