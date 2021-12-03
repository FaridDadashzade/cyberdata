import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyrogram import Client

cyberlogo = """

░█████╗░██╗░░░██╗██████╗░███████╗██████╗░
██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗
██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝
██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗
╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║
░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝

C Y B Ξ R String Session Generator
"""

template = """
C Y B Ξ R String Generator: @TheCyberUserBot
            
<code>String:</code>: <code>{}</code>
⚠️ <b>Xahiş edirik bu kodu güvənmədiyiniz insanlarla paylaşmayın.</b>"""

select = " "

print(cyberlogo)

while select != ("1", "2"):
    select = input("1. Telethon\n2. Pyrogram\n\nXahiş edirəm bir seçim edin: ").lower()
    if select == "1":
        print("""\nTelethon seçildi.\nScript işə salınır...""")
        time.sleep(1)
        API_KEY = int(input("API_KEY daxil edin: "))
        API_HASH = input("API_HASH daxil edin: ")

        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            session_string = client.session.save()
            saved_messages_template = "Telethon String" + template.format(session_string)
            print("\nString Session yaradılır...\n")
            client.send_message("me", saved_messages_template, parse_mode="html")
            time.sleep(1)
            print("String Session kayıtlı mesajlarınıza qeyd edildi.")
        break

    elif select == "2":
        print("""\nPyrogram seçildi.\nScript işə salınır...""")
        time.sleep(1)
        with Client(
        "CyberUserBot", 
        api_id=int(input("API_ID daxil edin: ")),
        api_hash=input("API_HASH daxil edin: ")) as pyrogram:
            saved_messages_template = "Pyrogram String" + template.format(pyrogram.export_session_string())
            print("\nString Session yaradılır...\n")           
            pyrogram.send_message("me", saved_messages_template, parse_mode="html")
            time.sleep(1) 
            print("String Session kayıtlı mesajlarınıza qeyd edildi.")
        break
    
    else:
        print("\nXahiş edirəm sadəcə 1 və ya 2 yazın.\n")
        time.sleep(1.5)
