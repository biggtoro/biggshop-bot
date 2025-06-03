from flask import Flask, request
import telegram
import os

TOKEN = '7617313022:AAEYiV2eeepKMAPANBHagQgFsdEg3fmMYXY'
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    bot.send_message(
        chat_id=chat_id,
        text="BENVENUTI NELLO SHOP DI BIG, QUI POTRETE TROVARE DI TUTTO, DA VESTITI A VERI E PROPRI FORNITORI"
    )
    return 'OK'

@app.route('/')
def index():
    return 'Bot attivo!'

if __name__ == '__main__':
  @app.route('/setwebhook', methods=['GET']

def set_webhook():
    webhook_url = 'https://big-shop-bot.onrender.com/webhook'
    print(f"Impostando webhook a: {webhook_url}")
    success = bot.set_webhook(webhook_url)
    print(f"Risultato set_webhook: {success}")
    if success:
        return "Webhook impostato: True"
    else:
        return "Webhook impostato: False"

