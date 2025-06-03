from flask import Flask, request
import telegram
import os
import asyncio

TOKEN = '7617313022:AAEYiV2eeepKMAPANBHagQgFsdEg3fmMYXY'
URL = 'https://biggshop-bot.onrender.com/webhook'

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    bot.send_message(chat_id=chat_id, text="BENVENUTI NELLO SHOP DI BIG, QUI POTRETE TROVARE DI TUTTO, DA VESTITI A VERI E PROPRI FORNITORI")
    return 'OK'

@app.route('/')
def index():
    return 'Bot attivo!'

async def set_webhook():
    await bot.delete_webhook()
    await bot.set_webhook(URL)


asyncio.run(set_webhook())

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        print("Webhook chiamato!")
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        print(f"Messaggio da chat_id: {chat_id}")
        bot.send_message(chat_id=chat_id, text="BENVENUTI NELLO SHOP DI BIG...")
    except Exception as e:
        print(f"Errore nel webhook: {e}")
    return 'OK'


