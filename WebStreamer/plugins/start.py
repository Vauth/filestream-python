# This file is a part of TG-FileStreamBot
# pylint: disable=relative-beyond-top-level

from telethon.extensions import html
from telethon.events import NewMessage
from WebStreamer import __version__
from WebStreamer.clients import StreamBot
from WebStreamer.vars import Var
from telethon import Button 

@StreamBot.on(NewMessage(incoming=True,pattern=r"^\/start*", func=lambda e: e.is_private))
async def start(event: NewMessage.Event):
    user = await event.get_sender()
    if (Var.ALLOWED_USERS and user.id not in Var.ALLOWED_USERS) or (
        Var.BLOCKED_USERS and user.id in Var.BLOCKED_USERS):
        return await event.message.reply(
            message="You are not in the allowed list of users who can use me.",
            link_preview=False,
            parse_mode=html
        )
    await event.message.reply(
        message=f'Hi <a href="tg://user?id={user.id}">{user.first_name}</a>, Send me a file to get an instant stream link.',
        buttons=[[Button.url("Dev", "https://t.me/feelded")], [Button.url("Updates", "https://t.me/execal")]],
        link_preview=False,
        parse_mode=html
    )
    try:
        if user.id == Var.OWNER_ID: return
        await event.client.send_message(Var.OWNER_ID, f"#START\n**Name:** {user.mention}\n**Username:** @{user.username or 'None'}\n**ID:** `{user.id}`")
    except:
        print(f"{user.first_name} - {user.id} - started me")
