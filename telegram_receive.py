import os
import asyncio
import logging
import argparse
from telethon import events
from telegram_utils import get_authorized_client

logger = logging.getLogger(__name__)

async def main(limit=5, download_dir='downloads'):
    # Use the utility to get an authorized client
    client = await get_authorized_client('telegram')
    logger.info("Successfully connected to Telegram!")

    # Ensure downloads directory exists
    os.makedirs(download_dir, exist_ok=True)

    # 1. Read recent dialogs (chats)
    logger.info(f" --- Recent {limit} Chats ---")
    async for dialog in client.iter_dialogs(limit=limit):
        logger.info(f"Chat: {dialog.name} (ID: {dialog.id})")

    # 2. Monitor for new messages in real-time
    logger.info("\nListening for new messages (Press Ctrl+C to stop)...")
    
    @client.on(events.NewMessage)
    async def handler(event):
        chat = await event.get_chat()
        sender = await event.get_sender()
        name = getattr(sender, 'first_name', 'Unknown')
        
        # Print text message
        if event.text:
            chat_title = getattr(chat, 'title', 'Private')
            logger.info(f"[{chat_title}] {name}: {event.text}")

        # Download images/media
        if event.photo:
            path = await event.download_media(file=download_dir + '/')
            logger.info(f"Downloaded photo from {name} to {path}")

    await client.run_until_disconnected()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Listen for incoming Telegram messages.")
    parser.add_argument("-l", "--limit", type=int, default=5, help="Number of recent chats to show. Default: 5.")
    parser.add_argument("-d", "--dir", default="downloads", help="Directory to save media. Default: 'downloads'.")
    
    args = parser.parse_args()
    
    try:
        asyncio.run(main(limit=args.limit, download_dir=args.dir))
    except KeyboardInterrupt:
        logger.info("\nStopped.")
