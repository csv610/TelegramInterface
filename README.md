# Telegram Interface

A powerful and simple command-line interface for interacting with Telegram using the Telethon library. This tool allows you to send messages, files, and monitor incoming messages in real-time.

## 🚀 Features

- **Real-time Monitoring**: Listen for incoming messages across all your chats.
- **Media Support**: Automatically download incoming photos and media to a local directory.
- **Flexible Sending**: Send text messages or files (with optional captions) to yourself or any contact.
- **Secure Configuration**: Uses environment variables for sensitive credentials.
- **Session Management**: Handles Telegram's authorization flow and persists sessions locally.

## 🛠 Prerequisites

- Python 3.10+
- Telegram API Credentials (ID and Hash) from [my.telegram.org](https://my.telegram.org/apps)

## 📥 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/csv610/TelegramInterface.git
   cd TelegramInterface
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**:
   Create a `.env` file in the root directory:
   ```env
   TELEGRAM_ID=your_api_id
   TELEGRAM_HASH=your_api_hash
   PHONE_NUMBER=your_phone_number_with_country_code
   ```

## 📖 Usage

### Monitoring Messages
Run the receiver script to listen for incoming messages and view recent dialogs:
```bash
python telegram_receive.py --limit 10 --dir ./downloads
```
*   `--limit`: Number of recent chats to display on startup.
*   `--dir`: Directory where incoming media will be saved.

### Sending Messages & Files
Use the sender script to transmit data:

**Send a simple message to 'Saved Messages':**
```bash
python telegram_send.py "Hello from the CLI!"
```

**Send a file with a caption:**
```bash
python telegram_send.py -f report.pdf -m "Here is the daily report"
```

**Send to a specific recipient:**
```bash
python telegram_send.py "Secret message" --to "+1234567890"
```

## 📁 Project Structure

- `telegram_receive.py`: Real-time listener and media downloader.
- `telegram_send.py`: CLI tool for sending text and files.
- `telegram_utils.py`: Shared utilities for authentication and config loading.
- `requirements.txt`: Python dependencies.
- `.env`: (User-created) Configuration for API credentials.

## 🔒 Security Note
Never commit your `.env` file or `*.session` files to public repositories. These contain sensitive tokens that grant access to your Telegram account.
