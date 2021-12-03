import asyncio
from pyrogram import Client


async def main():
    api_id = int(input("API ID daxil edin: "))
    api_hash = input("API HASH daxil edin: ")
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        await app.send_message(
            "me",
            "**@TheCyberUserBot Pyrogram Session String**:\n\n"
            f"`{await app.export_session_string()}`"
        )
        print(f"Pyrogram stringi kayıtlı mesajlara qeyd edildi!")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
