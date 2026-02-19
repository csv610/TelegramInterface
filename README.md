# Telegram Bot (Telethon-based)

This project uses the `Telethon` library to interact with Telegram as a user account. It includes scripts for receiving and sending messages, as well as handling images.

## Features

- **Message Monitoring:** Listen for new messages in real-time, log them, and download photos.
- **Message/File Sending:** Send text or files (with captions) to your "Saved Messages".
- **Utility Support:** Centralized client authorization logic.

## Prerequisites

1.  Python 3.10 or higher.
2.  A Telegram account.
3.  An API ID and API Hash from [Telegram Apps](https://my.telegram.org/apps).

## Setup

1.  **Configure Environment Variables:**
    -   Create or update the `.env` file in the project root.
    -   Fill in your credentials:
        ```env
        TELEGRAM_ID=your_api_id
        TELEGRAM_HASH=your_api_hash
        PHONE_NUMBER=your_phone_number_with_country_code
        ```

2.  **Install Dependencies:**
    -   Run: `pip install -r requirements.txt`

## Usage

### Receiving Messages
To listen for new messages and download any incoming photos:
```bash
python3 telegram_receive.py --limit 10 --dir my_downloads
```
This script will:
-   List your recent chats (default is 5).
-   Log all incoming text messages.
-   Download any photos to the specified directory (default is `downloads/`).

### Sending Content
To send text or files to your "Saved Messages" or other recipients:
```bash
# Send text to 'me'
python3 telegram_send.py "Hello from the script!"

# Send a file with a caption
python3 telegram_send.py -f image.jpg "Check this out!"

# Send a message to a specific user (phone or username)
python3 telegram_send.py "Hi there!" -t "+1234567890"
```

## Project Structure

- `telegram_receive.py`: Script for monitoring and receiving messages/media.
- `telegram_send.py`: Script for sending messages or files.
- `telegram_utils.py`: Contains common utility functions for client authorization.
- `downloads/`: Directory where received photos are saved.
