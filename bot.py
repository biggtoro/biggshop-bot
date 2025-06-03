from flask import Flask, request
import telegram
import os

TOKEN = '7617313022:AAEYiV2eeepKMAPANBHagQgFsdEg3fmMYXY'
URL = 'https://biggshop-bot.onrender.com/webhook'

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Webhook chiamato!")
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    print(f"Messaggio da chat_id: {chat_id}")
    bot.send_message(chat_id=chat_id, text="BENVENUTI NELLO SHOP DI BIG...")
    return 'OK'

@app.route('/')
def index():
    return 'Bot attivo!'

@app.before_first_request
def set_webhook():
    bot.delete_webhook()
    bot.set_webhook(f'{URL}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


