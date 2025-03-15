from pyrogram import Client, filters, enums
import asyncio
import os

api_id = int(os.getenv("API_ID")) 
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")

app = Client("my_account", api_id=api_id, api_hash=api_hash, session_string=session_string)

async def send_typing_indicators(chat_id):
    while True:
        await app.send_chat_action(chat_id, enums.ChatAction.TYPING)
        await asyncio.sleep(1)

@app.on_message(filters.group)
async def handle_message(client, message):
    asyncio.create_task(send_typing_indicators(message.chat.id))

app.run()
