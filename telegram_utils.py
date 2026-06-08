import os
import logging
from dotenv import load_dotenv
from telethon import TelegramClient

logger = logging.getLogger(__name__)


def load_config():
    """Load and return Telegram configuration from environment variables."""
    load_dotenv(override=True)

    api_id = os.getenv('TELEGRAM_ID')
    api_hash = os.getenv('TELEGRAM_HASH')
    phone = os.getenv('PHONE_NUMBER')

    if not api_id or not api_hash:
        raise ValueError("TELEGRAM_ID and TELEGRAM_HASH must be set in .env file.")

    try:
        api_id = int(api_id)
    except ValueError:
        raise ValueError("TELEGRAM_ID must be an integer.")

    return api_id, api_hash, phone


async def get_authorized_client(session_name='telegram'):
    """Initialize, connect, and ensure the client is authorized."""
    api_id, api_hash, phone = load_config()
    client = TelegramClient(session_name, api_id, api_hash)

    await client.connect()

    if not await client.is_user_authorized():
        if not phone:
            raise ValueError("Session not authorized and PHONE_NUMBER not found in .env")

        logger.info("Session not authorized. Starting interactive login...")
        await client.start(phone=phone)

    return client
