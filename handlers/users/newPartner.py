from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.mainBtn import adminBtn
from keyboards.inline.inlineBnt import RequestBtn, category, RequestBtn0
from loader import dp
from secret import ADMIN_ID, CHANNEL_ID
from sheet import addData, getAll, getDataForDropdown, addDataa
from states.state import Partner
import re

phone_pattern = r'^\d{9}$|^\d{2}\s?\d{3}\s?\d{2}\s?\d{2}$'
@dp.message_handler(lambda message: message.text == "/start", state="*")
async def start_command(message: types.Message, state: FSMContext):
    await message.answer(text="Tanlang!", reply_markup=adminBtn)
    await state.finish()

@dp.message_handler(text="➕ Yangi hamkor")
async def bot_echo(message: types.Message):
    status = 0
    for i in ADMIN_ID:
        if message.from_user.id == i:
            status = 1
            await message.answer(text="Rahbar ismi", reply_markup=ReplyKeyboardRemove())
            await Partner.name.set()
    if status == 0:
        await message.answer(text=message.text)


# @dp.message_handler(state=Partner.name, text="/start")
# async def bot_echo(message: types.Message, state:FSMContext):
#     await message.answer(text="Tanlang!", reply_markup=btnAdmin())
#     await state.finish()

@dp.message_handler(state=Partner.name)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'name':message.text})
    await message.answer(text="Rahbar familiyasi")
    await Partner.lastname.set()

# @dp.message_handler(state=Partner.lastname, text="/start")
# async def bot_echo(message: types.Message, state:FSMContext):
#     await message.answer(text="Tanlang!", reply_markup=btnAdmin())
#     await state.finish()

@dp.message_handler(state=Partner.lastname)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'lastname':message.text})
    await message.answer(text="Rahbar telefon raqami (950707849)")
    await Partner.phone.set()


@dp.message_handler(lambda message: not re.match(phone_pattern, message.text), state=Partner.phone)
async def invalid_phone_format(message: types.Message):
    await message.answer(
        "Noto`g`ri formatda yozdingiz! (950707849)")


@dp.message_handler(lambda message: re.match(phone_pattern, message.text), state=Partner.phone)
async def valid_phone_format(message: types.Message, state: FSMContext):
    await state.update_data({'phone':message.text})
    await message.answer(text="Rahbar Telegram raqami")
    await Partner.tg.set()


@dp.message_handler(lambda message: not re.match(phone_pattern, message.text), state=Partner.tg)
async def invalid_phone_format(message: types.Message):
    await message.answer(
        "Noto`g`ri formatda yozdingiz! (950707849)")

@dp.message_handler(lambda message: re.match(phone_pattern, message.text), state=Partner.tg)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'tg':message.text})
    await message.answer(text="Rahbarning e-gmail pochtasi")
    await Partner.email.set()

@dp.message_handler(state=Partner.email)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'email':message.text})
    await message.answer(text="Rahbar telegram ID’si")
    await Partner.id.set()

@dp.message_handler(state=Partner.id)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'id':message.text})
    await message.answer(text="Do’kon nomi")
    await Partner.marketName.set()

@dp.message_handler(state=Partner.marketName)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'marketName':message.text})
    await message.answer(text="Do’kon raqami")
    await Partner.marketId.set()


@dp.message_handler(state=Partner.marketId)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'marketId':message.text})
    await message.answer(text="Do’kon call-center")
    await Partner.marketCall.set()

@dp.message_handler(state=Partner.marketCall)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'marketCall':message.text})
    await message.answer(text="Guvohnoma raqami")
    await Partner.licenceID.set()

@dp.message_handler(state=Partner.licenceID)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'licenceID':message.text})
    data = await getDataForDropdown("⚙️ Sozlamalar!CW3:CW")
    btn = category(data)
    await message.answer(text="Do’kon kategoriyasi", reply_markup=btn)
    await Partner.category.set()

@dp.callback_query_handler(state=Partner.category)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    await state.update_data({'category':callback.data})
    await callback.message.edit_text(text="Do`konning ichki rasmi")
    await Partner.marketpic1.set()


@dp.message_handler(state=Partner.marketpic1, content_types=types.ContentType.PHOTO)
async def bot_start(message: types.Message, state:FSMContext):
    sent_message = await message.copy_to(chat_id="@"+CHANNEL_ID)
    post_link = f"https://t.me/{CHANNEL_ID}/{sent_message.message_id}"
    await state.update_data({"marketpic1":post_link})
    await message.answer(text="Do’konning tashqi rasmi")
    await Partner.marketpic2.set()

@dp.message_handler(state=Partner.marketpic1, content_types=types.ContentType.ANY)
async def id(message: types.Message, state:FSMContext):
    await message.answer(text="Rasm yuboring!", reply_markup=ReplyKeyboardRemove())
    await Partner.marketpic1.set()


@dp.message_handler(state=Partner.marketpic2, content_types=types.ContentType.PHOTO)
async def bot_start(message: types.Message, state:FSMContext):
    sent_message = await message.copy_to(chat_id="@"+CHANNEL_ID)
    post_link = f"https://t.me/{CHANNEL_ID}/{sent_message.message_id}"
    await state.update_data({"marketpic2":post_link})
    await message.answer(text="Humo plastik kartasi", reply_markup=RequestBtn())
    await Partner.humo.set()

@dp.message_handler(state=Partner.marketpic2, content_types=types.ContentType.ANY)
async def id(message: types.Message, state:FSMContext):
    await message.answer(text="Rasm yuboring!", reply_markup=ReplyKeyboardRemove())
    await Partner.marketpic2.set()

@dp.callback_query_handler(state=Partner.humo)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    if callback.data == 'confirmNo':
        dataa = "Yo`q ❌"
    else:
        dataa = "Ha ✅"
    await state.update_data({'humo':dataa})
    if callback.data == 'confirmNo':
        await callback.message.edit_text(text="UzCard plastik kartasi", reply_markup=RequestBtn0())
    else:
        await callback.message.edit_text(text="UzCard plastik kartasi", reply_markup=RequestBtn())
    await Partner.uzcard.set()

@dp.callback_query_handler(state=Partner.uzcard)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    if callback.data == 'confirmNo':
        dataa = "Yo`q ❌"
    else:
        dataa = "Ha ✅"
    await state.update_data({'uzcard':dataa})
    data = await getDataForDropdown("⚙️ Sozlamalar!AW3:AW")
    btn = category(data)
    await callback.message.edit_text(text="Do'kon joylashgan manzil(Viloyat)", reply_markup=btn)
    await Partner.region.set()


@dp.callback_query_handler(state=Partner.region)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    await state.update_data({'region':callback.data})
    data_to_row = {
        'Andijon viloyati': 'AX',
        'Buxoro viloyati': 'AY',
        'Fargʻona viloyati': 'AZ',
        'Jizzax viloyati': 'BA',
        'Xorazm viloyati': 'BB',
        'Namangan viloyati': 'BC',
        'Navoiy viloyati': 'BD',
        'Qashqadaryo viloyati': 'BE',
        'Qoraqalpogʻiston Respublikasi': 'BF',
        'Samarqand viloyati': 'BG',
        'Sirdaryo viloyati': 'BH',
        'Surxondaryo viloyati': 'BI',
        'Toshkent viloyati': 'BJ',
    }

    row = data_to_row.get(callback.data, '')
    data = await getDataForDropdown(f"⚙️ Sozlamalar!{row}3:{row}")
    btn = category(data)
    await callback.message.edit_text(text="Do'kon joylashgan manzil(shahar/tuman)", reply_markup=btn)
    await Partner.city.set()

@dp.callback_query_handler(state=Partner.city)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    print(callback.data)
    await state.update_data({'city':callback.data})
    await callback.message.edit_text(text="Muddatli to’lovga do’kondagi kunlik talab")
    await Partner.demand.set()

@dp.message_handler(state=Partner.demand)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'demand':message.text})
    data = await state.get_data()
    name = data.get('name')
    lastname = data.get('lastname')
    phone = data.get('phone')
    tg = data.get('tg')
    email = data.get('email')
    id = data.get('id')
    marketId = data.get('marketId')
    marketname = data.get('marketName')
    marketCall = data.get('marketCall')
    licenceId = data.get('licenceId')
    region = data.get('region')
    city = data.get('city')
    category = data.get('category')
    marketpic1 = data.get('marketpic1')
    marketpic2 = data.get('marketpic2')
    humo = data.get('humo')
    uzcard = data.get('uzcard')
    demand = data.get('demand')
    msg = f"""
🤝 Rahbar:
• Ism: <b>{name}</b>
• Familiya: <b>{lastname}</b>
• Telefon raqam: <b>{phone}</b>
• Telegram raqam: <b>{tg}</b>
• E-mail: <b>{email}</b>
• Telegram ID: <b>{id}</b>

🏢 Do'kon ma'lumotlari:
• Nomlanishi: <b>{marketname}</b>
• ID raqami: <b>{marketId}</b>
• Call-center raqami: <b>{marketCall}</b>
• Kategoriya: <b>{category}</b>
• Guvohnoma raqami: <b>{licenceId}</b>
• Manzil: <b>{region},{city}</b>
• Kunlik-talab: <b>{demand}</b>

💰 Moliya:
• Humo: <b>{humo}</b>
• UzCard: <b>{uzcard}</b>

🔗 Fayllar:
• Do`konning ichki rasmi: <b>{marketpic1}</b>
• Do’konning tashqi rasmi: <b>{marketpic2}</b>
    """
    await message.answer(text=msg, reply_markup=RequestBtn())
    await Partner.confirm.set()

@dp.callback_query_handler(state=Partner.confirm)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    await callback.message.delete()
    if callback.data == "confirmYes":
        data = await state.get_data()
        name = data.get('name')
        lastname = data.get('lastname')
        phone = data.get('phone')
        tg = data.get('tg')
        email = data.get('email')
        id = data.get('id')
        marketId = data.get('marketId')
        marketname = data.get('marketName')
        marketCall = data.get('marketCall')
        licenceId = data.get('licenceId')
        region = data.get('region')
        city = data.get('city')
        category = data.get('category')
        marketpic1 = data.get('marketpic1')
        marketpic2 = data.get('marketpic2')
        humo = data.get('humo')
        uzcard = data.get('uzcard')
        demand = data.get('demand')
        address = f"{region} | {city}"
        data = [
            [name, "B"],
            [lastname, "C"],
            [phone, "D"],
            [tg, "AG"],
            [email, "E"],
            [id, "F"],
            [marketId, "H"],
            [marketname, "G"],
            [marketCall, "I"],
            [licenceId, "J"],
            [demand, "M"],
            [category, "AO"],
            [marketpic1, "AP"],
            [marketpic2, "AQ"],
            [humo, "AR"],
            [uzcard, "AS"],
            [address, "K"],
        ]

        loading_message = await callback.message.answer_animation(
            animation='https://t.me/myprojectphotobase90775803200000/67')
        await addDataa(data, "🏢 Hamkor-do'konlar")

        await loading_message.delete()


        await callback.message.answer(text="Tasdiqlandi", reply_markup=adminBtn)
        await Partner.confirm.set()
    else:
        await callback.message.answer(text="Bekor qilindi!", reply_markup=adminBtn)
    await state.finish()