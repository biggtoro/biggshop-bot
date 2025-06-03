from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from flask import Flask, request

TOKEN = '7617313022:AAEYiV2eeepKMAPANBHagQgFsdEg3fmMYXY'
WEBHOOK_URL = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/webhook"

WELCOME_MESSAGE = (
    "👋 *BENVENUTI NELLO SHOP DI BIG!*\n\n"
    "QUI POTRETE TROVARE DI TUTTO, DA *VESTITI* A VERI E PROPRI *FORNITORI*.\n\n"
    "🛍️ Scrivici per scoprire di più!"
)

app = Flask(__name__)
bot_app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, parse_mode='Markdown')

bot_app.add_handler(CommandHandler("start", start))

@app.route('/webhook', methods=['POST'])
def webhook():
    return bot_app.update_webhook(request)

@app.before_first_request
def setup():
    bot_app.bot.set_webhook(WEBHOOK_URL)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
