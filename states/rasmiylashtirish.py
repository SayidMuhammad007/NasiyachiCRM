from aiogram.dispatcher.filters.state import State, StatesGroup

class Save(StatesGroup):
    id = State()
    time = State()
    product = State()
    price = State()
    image = State()
    market = State()
    customer_pic = State()
    screen = State()
    confirm = State()
    orderId = State()

class Customer(StatesGroup):
    name = State()
    id = State()
    phone = State()
    birth_date = State()
    limit = State()
    agg = State()
    hamkor = State()
    product = State()
    time = State()
    price = State()
    confirm = State()
    currency = State()

class Order(StatesGroup):
    name = State()
    product = State()
    phone = State()
    price = State()
    uzum = State()
    uzum_phone = State()
    pic = State()
    check = State()
    confirm = State()
    time = State()
    finishConfirm = State()
    market = State()