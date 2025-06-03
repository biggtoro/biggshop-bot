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
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
