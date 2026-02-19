import os
import sys
import asyncio
import logging
import argparse
from telegram_utils import get_authorized_client

logger = logging.getLogger(__name__)

async def send_content(message=None, file_path=None, recipient='me'):
    """
    Sends a message or a file to the specified recipient.
    """
    client = await get_authorized_client('telegram')
    
    try:
        if file_path:
            if not os.path.isfile(file_path):
                logger.error(f"File not found: {file_path}")
                return
            
            logger.info(f"Sending file '{file_path}' to {recipient}...")
            # Use message as caption if both are provided
            await client.send_file(recipient, file_path, caption=message)
        elif message:
            logger.info(f"Sending message to {recipient}...")
            await client.send_message(recipient, message)
        else:
            logger.warning("Nothing to send. Provide a message or a file.")
            return
            
        logger.info("Successfully sent!")
    except Exception as e:
        logger.exception("An unexpected error occurred during sending:")
    finally:
        await client.disconnect()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Send messages and files via Telegram.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python telegram_send.py "Hello world"
  python telegram_send.py -f image.jpg -m "Look at this!"
  python telegram_send.py "Secret message" -t "+1234567890"
        """
    )
    
    parser.add_argument("message", nargs="?", help="The message text to send.")
    parser.add_argument("-f", "--file", help="Path to a file to send.")
    parser.add_argument("-m", "--msg", dest="message_alt", help="Alternative way to provide message text.")
    parser.add_argument("-t", "--to", default="me", help="Recipient (username, phone, or 'me'). Default: 'me'.")
    
    args = parser.parse_args()
    
    # Resolve message from either positional argument or -m flag
    final_message = args.message or args.message_alt
    
    if not final_message and not args.file:
        parser.print_help()
        sys.exit(1)
        
    asyncio.run(send_content(message=final_message, file_path=args.file, recipient=args.to))
