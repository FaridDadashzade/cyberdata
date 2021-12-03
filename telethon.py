from telethon.sync import TelegramClient
from telethon.sessions import StringSession

APP_ID = int(input("Xahiş edirəm APP_ID daxil edin: "))
API_HASH = input("Xahiş edirəm API_HASH daxil edin: ")

with TelegramClient(
    StringSession(),
    APP_ID,
    API_HASH
) as cyber:
    this_string = cyber.session.save()
    mesaj = cyber.send_message("me", this_string)
    print(f"Telethon Stringi kayıtlı mesajlara göndərildi!\n\n{this_string}")
