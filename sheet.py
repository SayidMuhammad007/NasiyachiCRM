import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from loader import bot

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = "1YKuxPvffbFM6WwXW8fy3Qjk8HE0ZsrHeBKkpuBmirhw"
RANGE = '🧮 Kalkulyator!A:S'  # Update this to the desired range
WORKERS = "👥 Xodimlar"
ORDERS = "📒 Buyurtmalar"

def getCreds():
    credentials = None
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('secret.json', SCOPES)
            credentials = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())
    service = build('sheets', 'v4', credentials=credentials)
    return service

async def getData(value_to_find, cur, table):
    try:
        service = getCreds()
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{table}!A:CD').execute()
        values = result.get('values', [])
        data = []
        for row in values:
            if row and len(row) >= 77 and str(row[cur]) == str(value_to_find):
                data.append(row)
        print(data)
        return data
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None

async def getData1(value_to_find, cur, table):
    try:
        service = getCreds()  # Assuming getCreds() is defined correctly
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{table}!A:FF').execute()
        values = result.get('values', [])
        data = []
        for row in values:
            if len(row) > cur and str(row[cur]) == str(value_to_find):
                data.append(row)
        print(data)
        return data
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None

async def getDataNew(value_to_find, cur, table):
    try:
        service = getCreds()  # Assuming getCreds() is defined correctly
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{table}!A:FF').execute()
        values = result.get('values', [])
        data = []
        for row in values:
            if len(row) > cur and str(row[cur]) == str(value_to_find) and row[46] == "🆕 Yangi do'kon!":
                data.append(row)
        print(data)
        return data
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None

async def getData01(value_to_find, cur, table):
    try:
        service = getCreds()  # Assuming getCreds() is defined correctly
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{table}!A:FF').execute()
        values = result.get('values', [])
        data = []
        for row in values:
            if len(row) > cur and str(row[cur]) == str(value_to_find):
                data.append(row)
        print(data)
        return data
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None




async def getData2(value_to_find, cur, table):
    try:
        service = getCreds()
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{table}!A:CC').execute()
        values = result.get('values', [])
        data = []
        for row in values:
            if row and len(row) >= cur and str(row[cur]) == str(value_to_find):
                data.append(row)
        print(data)
        return data
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None


async def getPaymentData():
    try:
        service = getCreds()
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'📋 To\'lov hisoblari!A3:CC').execute()
        values = result.get('values', [])
        data = []
        for row in values:
            if row and len(row) > 14 and row[14]:
                data.append(row)
        return data
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None


async def getDataNew(value_to_find, cur, table):
    try:
        service = getCreds()  # Assuming getCreds() is defined correctly
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{table}!A:FF').execute()
        values = result.get('values', [])
        data = []
        for row in values:
            if len(row) > cur and str(row[cur]) == str(value_to_find) and row[46] == "🆕 Yangi do'kon!":
                data.append(row)
        print(data)
        return data
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None

async def checkUser(value_to_find, table, row_id):
    try:
        service = getCreds()
        sheets = service.spreadsheets()
        if sheets:
            result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"{table}!A:BC").execute()
            values = result.get('values', [])
            for row in values:
                try:
                    if row and str(row[row_id]) == str(value_to_find):
                        return row  # Row numbers start at 1, return the row data as well
                    elif ',' in row[row_id]:
                        if str(value_to_find) in row[row_id]:
                            return row  # Row numbers start at 1, return the row data as well

                except (ValueError, IndexError):
                    print(ValueError)  # Row numbers start at 1, return the row data as well
        return None
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None

async def getDataForDropdown(table):
    service = getCreds()
    sheets = service.spreadsheets()
    try:
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{table}').execute()
        values = result.get('values', [])
        data = []
        for row in values:
            if row:
                data.append(row)
        return data
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None

async def getAllHaveValueOne(table, col, cur, value_to_find):
    service = getCreds()
    sheets = service.spreadsheets()
    try:
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{table}!{col}').execute()
        values = result.get('values', [])
        data = []
        for row in values:
            if len(row) > cur and str(row[cur]) == str(value_to_find):
                data.append(row)
        return data
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None


async def getAll(table):
    try:
        service = getCreds()
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{table}!A3:FF').execute()
        values = result.get('values', [])
        data = []
        for row in values:
            if row:
                data.append(row)
        return data
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None

async def getAllMarkets(table):
    try:
        service = getCreds()
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{table}!A3:FF').execute()
        values = result.get('values', [])
        data = []
        for row in values:
            if row and len(row) > 58:
                data.append(row)
        return data
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None

async def find_orders(value_to_find, cur, table, user_id):
    try:
        service = getCreds()
        sheets = service.spreadsheets()
        status = None
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{table}!A3:CD').execute()
        values = result.get('values', [])
        data = []
        if user_id == None:
            for index, row in enumerate(values):
                if cur < len(row) and row and str(value_to_find) in str(row[cur]):
                    data.append(row)
        else:
            check = None
            for index, row in enumerate(values):
                if len(row) >= 75 and str(row[3]) == str(user_id):
                    check = row
                    status = True
            print(f"check{check}")
            if check == None or check[1] == "⚪️ rasmiylashtirildi" or check[1] == "⛔️ bekor qilindi" or check[1] == "🔴 sotilmadi":
                for index, row in enumerate(values):
                    if row and len(row) > 75 and str(row[cur]) == str(value_to_find):
                        data.append(row)
            else:
                data.append(check)
        print(data)
        return data, status
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None


async def checkStatus():
    try:
        service = getCreds()
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'📒 Buyurtmalar!A3:CD').execute()
        values = result.get('values', [])
        data = []
        for i in values:
            if len(i) > 1 and i[1] == "🔵 yangi buyurtma":
                data.append(i)
        return data
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None

def find_empty_row(sheets, table):
    try:
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"{table}!B:B").execute()
        values = result.get('values', [])

        # Find the first empty cell in column B
        next_empty_row = 1
        for row in values:
            if row is None:
                break
            next_empty_row += 1
        print(f"next empty row:{next_empty_row}")
        return next_empty_row
    except HttpError as error:
        print(f"Error finding empty row: {error}")
        return None


async def add_row(rows, table):
    try:
        service = getCreds()
        sheets = service.spreadsheets()
        free = find_empty_row(sheets=sheets, table=table)
        for row in rows:
            if row[1] == None:
                row[1] = free
            print(f"id{row[0]}{row[1]}")
            sheets.values().update(
                spreadsheetId=SPREADSHEET_ID,
                range=f"'{table}'!{row[0]}{row[1]}",
                valueInputOption="RAW",
                body={"values": [[row[2]]]}
            ).execute()
        return rows[0][1]
    except HttpError as error:
        print(f"Error adding row: {error}")


async def getNotifMsg(id, tg_id, username):

    data1 = await getData(int(id)-2, 0, "📒 Buyurtmalar")
    seller1 = await getData1(tg_id, 4, "👥 Xodimlar")
    print(f"{id}-{tg_id}-{username}")
    data = data1[0]
    seller = seller1[0]
    msg = f"""
№{data[0]} raqamli buyurtma holati <b>{data[1]}</b> ga o'zgartirildi!

👤 Mijoz:
Ism: {data[7]}
Telefon raqam: {data[10]}
UzumNasiyadan ro'yhatdan o'tgan telefon raqami: {data[12]}

🛒 Buyurtma:
Mahsulot nomi:{data[22]}
Mahsulot narxi: {data[28]}
Nasiya narx:{data[34]}
Oylik to'lov:{data[35]}
Buyurtma holati:{data[1]}
Sana va vaqt: {data[4]}, {data[77]}

🏢 Do'kon:
Nomlanishi:{data[21]}
Call-center: {data[20]}

🤝 Menejer:
Ismi: {seller[1]}
Telefon raqam: {seller[2]}
Telegram: @{username}
    """
    admin = f"""
№{data[0]} raqamli buyurtma holati <b>{data[1]}</b> ga o'zgartirildi!

👤 Mijoz:
Ism: {data[7]}
Telefon raqam: {data[10]}
UzumNasiyadan ro'yhatdan o'tgan telefon raqami:

🛒 Buyurtma:
Mahsulot nomi:{data[22]}
Mahsulot narxi: {data[28]}
Nasiya narx:{data[34]}
Oylik to'lov:{data[35]}
Buyurtma holati:{data[1]}
Sana va vaqt: {data[4]}, {data[77]}

🏢 Do'kon:
Nomlanishi:{data[21]}
Call-center: {data[20]}

📎 Fayllar:
Mijozni mahsulot bilan tushgan rasmi: 
Shartnoma skrinshoti: 

🤝 Menejer:
Ismi: {seller[1]}
Telefon raqam: {seller[2]}
Telegram: @{username}
        """
    # print(len(data[21]))
    # if len(data[21]) > 5 :
    #     partner = await getData2(data[21], 28, "🏢 Hamkor-do'konlar")
    #     await bot.send_message(chat_id=partner[0][5], text=msg)
    return admin

async def addDData(column, values, table):
    try:
        service = getCreds()
        sheets = service.spreadsheets()
        next_empty_row = find_empty_row(sheets, table)
        print(column)
        if next_empty_row:
            for value in values:
                range_ = f"{table}!{value[1]}{next_empty_row}"
                data = [[value[0]]]  # Wrap the value in a list for proper formatting
                print(data)
                sheets.values().update(
                    spreadsheetId=SPREADSHEET_ID,
                    range=range_,
                    valueInputOption="RAW",
                    body={"values": data}
                ).execute()
            return True
        else:
            print('error: No empty rows found')
    except HttpError as error:
        print(f"Error adding row: {error}")


async def addDataa(values, table):
    try:
        service = getCreds()
        sheets = service.spreadsheets()
        next_empty_row = find_empty_row(sheets, table)
        print("testetset", next_empty_row)
        if next_empty_row:
            for value in values:
                range_ = f"{table}!{value[1]}{next_empty_row}"
                data = [[value[0]]]
                sheets.values().update(
                    spreadsheetId=SPREADSHEET_ID,
                    range=range_,
                    valueInputOption="RAW",
                    body={"values": data}
                ).execute()
            return True
        else:
            print('error: No empty rows found')
    except HttpError as error:
        print(f"Error adding row: {error}")

async def addData(values, table):
    try:
        service = getCreds()
        sheets = service.spreadsheets()
        next_empty_row = find_empty_row(sheets=sheets, table="📒 Buyurtmalar")
        if next_empty_row:
            for value in values:
                print(value[0])
                range_ = f"{table}!{value[1]}{next_empty_row}"
                data = [[value[0]]]  # Wrap the value in a list for proper formatting
                print(data)
                sheets.values().update(
                    spreadsheetId=SPREADSHEET_ID,
                    range=range_,
                    valueInputOption="RAW",
                    body={"values": data}
                ).execute()
            return True, next_empty_row-2
        else:
            print('error: No empty rows found')
    except HttpError as error:
        print(f"Error adding row: {error}")
