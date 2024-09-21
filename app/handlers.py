from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboard as kb
import app.database.requests as rq

router = Router()

"""class Register(StatesGroup):
    name = State()
    age = State()
    number = State()"""


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Қош келдіңіз QazaqRepablic онлайн дүкеніне',reply_markup=kb.main)


@router.message(F.text == 'Katalog')
async def catalog(message: Message):
    await message.answer('Товардың котегориясын таңдаңыз', reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Сіз категория таңдадыңыз')
    await callback.message.answer('Категория бойынша товарды таңдаңыз',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Сіз товар таңдадыңыз')
    await callback.message.answer(f'Атауы: {item_data.name}\nОписания: {item_data.description}\nБағасы: {item_data.price}тг',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))





































"""@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('You take command help')

@router.message(F.text == 'Katalog')
async def katalog(message: Message):
    await message.answer('Товар түрін таңдаңыз:', reply_markup=kb.Katalog)

@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Сіз категория таңдадыңыз', show_alert=True)
    await callback.message.answer('Сіз бүржейдені таңдадыңыз')

@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Есіміңізді енгізіңіз')

@router.message(Register.name)
async def register(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Жасыңызды жазыңыз')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Телефон нөміріңізді жіберіңіз', reply_markup=kb.get_number)

@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Сіздің атыңыз: {data["name"]}\nСіздің жасыңыз: {data["age"]}\n Сіздің нөміріңіз: {data["number"]}')
    await state.clear()"""