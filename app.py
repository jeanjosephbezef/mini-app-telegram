import os
import threading
import asyncio

from flask import Flask, send_from_directory
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update


# Token Telegram depuis Render Environment
TOKEN = os.getenv("TELEGRAM_TOKEN")


# Mini App Flask
app = Flask(__name__, static_folder="webapp")


# Page de la boutique
@app.route("/")
def home():
    return send_from_directory("webapp", "index.html")


# Fichiers CSS / JS / images
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("webapp", path)


# -------------------------
# COMMANDES DU BOT TELEGRAM
# -------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bienvenue 👋\n"
        "Ta boutique est disponible via la Mini App."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commandes :\n"
        "/start\n"
        "/help\n"
        "/admin"
    )


async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commande administrateur ✅"
    )


# -------------------------
# LANCEMENT DU BOT
# -------------------------

def run_bot():

    async def bot_main():

        if not TOKEN:
            print("ERREUR : TELEGRAM_TOKEN manquant")
            return

        bot = ApplicationBuilder().token(TOKEN).build()

        bot.add_handler(CommandHandler("start", start))
        bot.add_handler(CommandHandler("help", help_command))
        bot.add_handler(CommandHandler("admin", admin_command))

        print("Bot Telegram démarré ✅")

        await bot.initialize()
        await bot.start()
        await bot.updater.start_polling()

        await asyncio.Event().wait()


    asyncio.run(bot_main())


# Démarrer le bot une seule fois
threading.Thread(
    target=run_bot,
    daemon=True
).start()


# -------------------------
# SERVEUR RENDER
# -------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )