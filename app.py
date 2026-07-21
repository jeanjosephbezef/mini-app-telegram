import os
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

app = Flask(__name__)


@app.route("/")
def home():
    return "Serveur actif"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue sur le bot !")


def run_bot():
    bot = ApplicationBuilder().token(TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    bot.run_polling()


if __name__ == "__main__":
    import threading

    threading.Thread(target=run_bot).start()

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)