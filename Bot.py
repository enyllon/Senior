import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = "7881405359:AAFTh8D-jgY53YAcS2r_ngdqcIlGgC792ag"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def get_gift_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("💝 или 🧸"))
    keyboard.add(KeyboardButton("🌹 или 🎁"))
    keyboard.add(KeyboardButton("💐 или 🍾"))
    keyboard.add(KeyboardButton("🏆 или 💍"))
    return keyboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Выбери пару символов:",
        reply_markup=get_gift_keyboard()
    )

@dp.message_handler(lambda message: message.text in ["💝 или 🧸", "🌹 или 🎁", "💐 или 🍾", "🏆 или 💍"])
async def gift_choice(message: types.Message):
    gift_info = {
        "💝 или 🧸": {"price": 7, "chance": 47.238},
        "🌹 или 🎁": {"price": 12, "chance": 47.238},
        "💐 или 🍾": {"price": 24, "chance": 47.238},
        "🏆 или 💍": {"price": 50, "chance": 47.238}
    }

    gift = gift_info[message.text]
    price = gift["price"]
    chance = gift["chance"]

    # Информация о стоимости и шансе
    await message.answer(
        f"Оплата: {price} звёзд для игры за подарок.\nШанс на победу: {chance}%.",
        reply_markup=types.ReplyKeyboardRemove()
    )
    
    # Генерация результата игры (с одинаковым шансом)
    result = random.choices(["win", "lose"], weights=[chance, 100 - chance])[0]
    
    if result == "win":
        await message.answer("🎉 Поздравляю! Ты выиграл!")
    else:
        await message.answer("😢 Ты проиграл.")
    
    # Опция для повторного старта
    await message.answer("Попробуй снова /start")

if name == "main":
    executor.start_polling(dp, skip_updates=True)