import os
import threading

from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


TOKEN = os.getenv("TELEGRAM_TOKEN")

app = Flask(__name__)


@app.route("/")
def home():
    return "Bot Telegram actif"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue sur le bot !")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commandes disponibles :\n/start\n/help\n/admin"
    )


async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commande administrateur")


def run_bot():
    bot = ApplicationBuilder().token(TOKEN).build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("help", help_command))
    bot.add_handler(CommandHandler("admin", admin_command))

    bot.run_polling()


if __name__ != "__main__":
    threading.Thread(target=run_bot).start()