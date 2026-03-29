from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bot.target.project import finder

user = Router() 

class UserStates(StatesGroup):
    write = State()

@user.message(CommandStart()) 
async def start(message: Message): 
    await message.answer('Привет') 


@user.message(Command('get')) 
async def send_request(message: Message, state: FSMContext): 
    await state.set_state(UserStates.write)
    await message.answer("Жду запрос в гугел")


@user.message(UserStates.write) 
async def ne_callback(message: Message, state: FSMContext): 
    text = message.text
    if not text:
        return
    r = await finder(text)
    await message.answer(str(r))
    await state.clear()

