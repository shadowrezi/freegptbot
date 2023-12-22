from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from g4f.Provider import Bing, ChatgptAi

form = Router()

engine = ChatgptAi


@form.message(Command(commands=['bing'], ignore_case=True))
async def switch_to_bing(message: Message):
    global engine
    engine = Bing

    await message.reply('<b>Engine was switch to Bing!</b>')


@form.message(Command(commands=['gpt'], ignore_case=True))
async def switch_to_gpt(message: Message):
    global engine
    engine = ChatgptAi

    await message.reply('<b>Engine was switch to ChatGPT</b>')


@form.message()
async def chat(message: Message):
    global engine

    kwargs = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': message.text}]
    }
    if isinstance(engine(), Bing):
        kwargs['tone'] = 'Balanced'

    response = await engine.create_async(**kwargs)

    await message.answer(response)
