import os
import threading
import asyncio

from flask import Flask, send_from_directory
from telegram.ext import ApplicationBuilder, CommandHandler


TOKEN = os.getenv("TELEGRAM_TOKEN")

app = Flask(__name__, static_folder="webapp")


@app.route("/")
def home():
    return send_from_directory("webapp", "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("webapp", path)


async def start(update, context):
    await update.message.reply_text("Bot actif ✅")


async def help_command(update, context):
    await update.message.reply_text("/start\n/help")


def run_bot():

    async def bot_main():

        bot = ApplicationBuilder().token(TOKEN).build()

        bot.add_handler(CommandHandler("start", start))
        bot.add_handler(CommandHandler("help", help_command))

        await bot.initialize()
        await bot.start()
        await bot.updater.start_polling()

        await asyncio.Event().wait()

    asyncio.run(bot_main())


# Lance le bot une seule fois
threading.Thread(target=run_bot).start()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )