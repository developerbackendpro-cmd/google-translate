import logging
from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
from deep_translator import GoogleTranslator
logging.basicConfig(level=logging.INFO)

API_TOKEN = ""

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def translate_text(text, target_langs):
    translations = {}
    for lang in target_langs:
        translated = GoogleTranslator(source='auto', target=lang).translate(text)
        translations[lang] = translated
    return translations

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Здравствуйте ! Отправьте текст, и я переведу его на узбекский, русский и английский языки.")

@dp.message_handler()
async def translate_message(message: types.Message):
    text = message.text
    target_langs = ['uz', 'ru', 'en']
    translations = translate_text(text, target_langs)
    response = "\n\n".join([f"{lang.upper()}:\n{translations[lang]}" for lang in target_langs])
    await message.reply(response)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)