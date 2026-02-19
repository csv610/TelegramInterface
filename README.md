# Telegram Interface

A set of Python scripts for interacting with the Telegram API using the Telethon library.

## Workflow

The following diagram illustrates the interaction between a mobile device and a local machine using these scripts:

```mermaid
sequenceDiagram
    participant User as iPhone (User)
    participant Cloud as Telegram Cloud
    participant Home as Local Machine (Home)

    User->>Cloud: Sends Text/Image
    Cloud->>Home: New Message Event (telegram_receive.py)
    Note over Home: Processes Text/Image
    Home->>Cloud: Sends Results (telegram_send.py)
    Cloud->>User: Receives Results
```

## Functionality

- **Message Monitoring**: Logs incoming messages from all active chats in real-time.
- **Media Acquisition**: Downloads received photos to a local directory.
- **Message Dispatch**: Sends text messages and files to specified recipients.
- **Authentication**: Manages Telegram session authorization and configuration via environment variables.

## Requirements

- Python 3.10+
- Telegram API credentials (ID and Hash)

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Define credentials in a `.env` file:
   ```env
   TELEGRAM_ID=your_api_id
   TELEGRAM_HASH=your_api_hash
   PHONE_NUMBER=your_phone_number
   ```

## Usage

### Receiving Messages
The script displays recent chats and listens for new messages.
```bash
python telegram_receive.py --limit 10 --dir ./downloads
```

### Sending Content
The script transmits text or files.

**Send text to "Saved Messages":**
```bash
python telegram_send.py "Message text"
```

**Send a file with a caption:**
```bash
python telegram_send.py -f path/to/file -m "Caption text"
```

**Send to a specific contact:**
```bash
python telegram_send.py "Message text" --to "+1234567890"
```

## Components

- `telegram_receive.py`: Message listener and media downloader.
- `telegram_send.py`: Command-line interface for sending content.
- `telegram_utils.py`: Shared authentication and configuration logic.
- `requirements.txt`: Project dependencies.
