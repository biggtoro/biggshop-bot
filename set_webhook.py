import telegram
import asyncio

TOKEN = '7617313022:AAEYiV2eeepKMAPANBHagQgFsdEg3fmMYXY'
URL = 'https://biggshop-bot.onrender.com/webhook'

bot = telegram.Bot(token=TOKEN)

async def set():
    await bot.delete_webhook()
    await bot.set_webhook(URL)

asyncio.run(set())
