import os
from dotenv import load_dotenv

import json

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

with open("games.json", "r", encoding="utf-8") as file:
    games = json.load(file)

TOKEN=os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6845995826:AAFI2WAEwA2Wn2hpDlMH2dQWi3plFctGDkE')
dp = Dispatcher(bot, storage=MemoryStorage())

ADMINS = [557997323]


@dp.message_handler(commands='start')
async def start(message: types.Message):
    game_choice = InlineKeyboardMarkup()
    for game in games:
        button = InlineKeyboardButton(text=game, callback_data=game)
        game_choice.add(button)
    await message.answer(text='Привіт! Я - ігробот🎮\nОбери гру, про яку хочеш дізнатись.😉', reply_markup=game_choice)

@dp.message_handler(commands='list_games')
async def list_games(message: types.Message):
    game_choice = InlineKeyboardMarkup()
    for game in games.keys():
        button = InlineKeyboardButton(text=game, callback_data=game)
        game_choice.add(button)
    await message.answer(text='Список наявних ігор🎮:', reply_markup=game_choice)

@dp.callback_query_handler()
async def get_game_into(callback_query: types.CallbackQuery):
    if callback_query.data in games.keys():
        await bot.send_photo(callback_query.message.chat.id, games[callback_query.data]['photo'])
        url= games[callback_query.data]['site_url']
        game_ratting = games[callback_query.data]['rating']
        game_description = games[callback_query.data]["description"]
        message = f'<b>Game url:</b> {url}\n\n<b>About:</b> {game_description}\n\n<b>Rate:</b> {game_ratting}'
        await bot.send_message(callback_query.message.chat.id, message, parse_mode='html')
    else:
        await bot.send_message(callback_query.message.chat.id, 'Гру не знайдено.😥')

@dp.message_handler(commands='add_game')
async def add_new_game(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id in ADMINS:
        await message.answer(text='Введіть назву гри, щоб додати нову:')
        await state.set_state('set_game_name')
    else:
        await message.answer(text='Ви неможете додати гру: недостатньо прав для цієї дії.😢')

@dp.message_handler(commands='cancel_add_remove', state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    await message.answer('Додавання/Видалення гри скасовано.🚫')
    await state.finish()
    
@dp.message_handler(commands='remove_game')
async def remove_game(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id in ADMINS:
        await message.answer('Введіть назву гри, яку ви хочете видалити:')
        await state.set_state('confirm_remove_game')
    else:
        await message.answer('Ви не маєте прав для видалення гри.😢')

@dp.message_handler(state='confirm_remove_game')
async def confirm_remove_game(message: types.Message, state: FSMContext):
    game_to_remove = message.text
    if game_to_remove in games:
        del games[game_to_remove]
        with open("games.json", "w", encoding="utf-8") as file:
            json.dump(games, file, indent=4, ensure_ascii=False)
        await message.answer(f'Гру "{game_to_remove}" видалено з бібліотеки.😎')
    else:
        await message.answer('Гру не знайдено.😥')
    await state.finish()


game_name = ''

@dp.message_handler(state='set_game_name')
async def set_game_name(message: types.Message, state: FSMContext):
    global game_name
    if len(message.text) > 64:
        await message.answer(text='На жаль я не можу додати цю гру: довжина назви не має перевищувати 64 символи.🙁')
    else:
        game_name = message.text
        games[game_name] = {}
        await state.set_state('set_site_url')
        await message.answer(text='Чудово. Тепер введи посилання з інформацією на вебсайт:')
        
@dp.message_handler(state='set_site_url')
async def set_site_url(message: types.Message, state: FSMContext):
    global game_name
    game_site_url = message.text
    games[game_name]['site_url'] = game_site_url
    await state.set_state('set_description')
    await message.answer(text='Чудово. Розкажи щось цікаве про цю гру:')

@dp.message_handler(state='set_description')
async def set_description(message: types.Message, state: FSMContext):
    global game_name
    game_description = message.text
    games[game_name]['description'] = game_description
    await state.set_state('set_rating')
    await message.answer(text='Чудово. Який рейтинг у цієї гри?')

@dp.message_handler(state='set_rating')
async def set_rating(message:types.Message, state: FSMContext):
    global game_name
    game_rating = message.text
    games[game_name]['rating'] = game_rating
    await state.set_state('set_photo')
    await message.answer(text='Чудово. Тепер введи посилання на фото цієї гри:')

@dp.message_handler(state='set_photo')
async def set_photo(message: types.Message, state: FSMContext):
    global game_name
    game_photo = message.text
    games[game_name]['photo']= game_photo
    with open("games.json", "w", encoding="utf-8") as file:
        json.dump(games, file, indent=4, ensure_ascii=False)
    await message.answer(text='Супер! Нову гру успішно додано до бібліотеки.😎')
    await state.finish()

async def set_default_commands(dp):
    await bot.set_my_commands(
        [
            types.BotCommand('start', 'Запустити бота'),
            types.BotCommand('list_games', 'Список ігор'),
            types.BotCommand('add_game', 'Додати нову гру'),
            types.BotCommand('remove_game', 'Видалення гри з списку'),
            types.BotCommand('cancel_add_remove', 'Скасувати додавання/видалення гри')
        ]
    )
                
async def on_startup(dp):
    await set_default_commands(dp)
    
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

