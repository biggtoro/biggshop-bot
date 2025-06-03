
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '7617313022:AAEYiV2eeepKMAPANBHagQgFsdEg3fmMYXY'

WELCOME_MESSAGE = (
    "👋 *BENVENUTI NELLO SHOP DI BIG!*\n\n"
    "QUI POTRETE TROVARE DI TUTTO, DA *VESTITI* A VERI E PROPRI *FORNITORI*.\n\n"
    "🛍️ Scrivici per scoprire di più!"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, parse_mode='Markdown')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
