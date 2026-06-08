import os
import asyncio
import logging
import argparse
from telethon import events
from telegram_utils import get_authorized_client

logger = logging.getLogger(__name__)


async def main(limit=5, download_dir='downloads'):
    client = await get_authorized_client('telegram')
    try:
        logger.info("Successfully connected to Telegram!")

        os.makedirs(download_dir, exist_ok=True)

        logger.info(" --- Recent %d Chats ---", limit)
        async for dialog in client.iter_dialogs(limit=limit):
            logger.info("Chat: %s (ID: %s)", dialog.name, dialog.id)

        logger.info("Listening for new messages (Press Ctrl+C to stop)...")

        @client.on(events.NewMessage)
        async def handler(event):
            try:
                chat = await event.get_chat()
                sender = await event.get_sender()
                name = getattr(sender, 'first_name', 'Unknown')

                if event.text:
                    chat_title = getattr(chat, 'title', 'Private')
                    logger.info("[%s] %s: %s", chat_title, name, event.text)

                if event.photo:
                    path = await event.download_media(file=download_dir)
                    logger.info("Downloaded photo from %s to %s", name, path)
            except Exception:
                logger.exception("Error handling message:")

        await client.run_until_disconnected()
    finally:
        await client.disconnect()
        logger.info("Disconnected.")


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    parser = argparse.ArgumentParser(description="Listen for incoming Telegram messages.")
    parser.add_argument("-l", "--limit", type=int, default=5, help="Number of recent chats to show. Default: 5.")
    parser.add_argument("-d", "--dir", default="downloads", help="Directory to save media. Default: 'downloads'.")

    args = parser.parse_args()

    try:
        asyncio.run(main(limit=args.limit, download_dir=args.dir))
    except KeyboardInterrupt:
        logger.info("Stopped.")
