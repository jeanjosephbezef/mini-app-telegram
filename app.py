import os
import threading

from flask import Flask, send_from_directory
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


TOKEN = os.getenv("TELEGRAM_TOKEN")

app = Flask(__name__, static_folder="webapp")


@app.route("/")
def home():
    return send_from_directory("webapp", "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("webapp", path)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue sur le bot !")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commandes disponibles :\n/start\n/help\n/admin"
    )


async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commande administrateur")


def run_bot():
    import asyncio

    async def main():
        bot = ApplicationBuilder().token(TOKEN).build()

        bot.add_handler(CommandHandler("start", start))
        bot.add_handler(CommandHandler("help", help_command))
        bot.add_handler(CommandHandler("admin", admin_command))

        await bot.initialize()
        await bot.start()
        await bot.updater.start_polling()

        await asyncio.Event().wait()

    asyncio.run(main())


if __name__ != "__main__":
    threading.Thread(target=run_bot).start()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )