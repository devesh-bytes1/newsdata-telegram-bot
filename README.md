# 📰 NewsData.io Telegram Bot

A Telegram bot that delivers **Latest News** and **Cryptocurrency News** directly to your Telegram chats using the [NewsData.io API](https://newsdata.io). Get instant access to breaking news and crypto updates with interactive inline keyboards.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- **📰 Latest News**: Get the most recent news from around the world
- **₿ Crypto News**: Browse news for 200+ cryptocurrencies
- **🖼️ Rich Media**: News articles with images and captions
- **🔘 Interactive Buttons**: Easy navigation with inline keyboards
- **⚙️ Configurable**: Customize language and number of articles
- **🚀 Fast & Reliable**: Built with async python-telegram-bot library

## 🎯 What It Does

The bot provides two main functionalities:

1. **Latest News**: Fetches general news articles from NewsData.io
2. **Crypto News**: Browse news for specific cryptocurrencies (Bitcoin, Ethereum, Solana, etc.)

Users interact with the bot through:
- `/start` command to launch the bot
- Inline keyboard buttons to navigate menus
- Photo messages with article captions and "Read More" links

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.8 or higher** installed
- **Telegram account** to create a bot
- **NewsData.io API key** ([Get one here](https://newsdata.io/register))

## 🚀 Installation

### Step 1: Clone or Download the Repository

```bash
# If using git
git clone https://github.com/your-username/newsdata-telegram-bot.git
cd newsdata-telegram-bot

# Or extract the zip file and navigate to the folder
cd newsdata_telegram_bot
```

### Step 2: Install Dependencies

```bash
pip install -r req.txt
```

**Dependencies installed:**
- `python-telegram-bot==21.0` - Telegram Bot API wrapper
- `python-dotenv==1.0.0` - Environment variable management
- `requests==2.31.0` - HTTP requests for API calls

### Step 3: Create a Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` command
3. Follow the prompts:
   - Choose a name for your bot (e.g., "My News Bot")
   - Choose a username (must end in 'bot', e.g., "mynews_bot")
4. **Copy the API token** (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Step 4: Get NewsData.io API Key

1. Visit [https://newsdata.io/register](https://newsdata.io/register)
2. Sign up for a free account
3. Go to your dashboard
4. **Copy your API key** (looks like: `pub_xxxxxxxxxxxxxxxxxxxxx`)

### Step 5: Configure Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit the `.env` file with your credentials:

```env
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
NEWSDATA_API_KEY=pub_xxxxxxxxxxxxxxxxxxxxx
DEFAULT_LANGUAGE=en
DEFAULT_NEWS_COUNT=5
```

**Configuration Options:**

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `TELEGRAM_BOT_TOKEN` | Your Telegram Bot API token from BotFather | - | ✅ Yes |
| `NEWSDATA_API_KEY` | Your NewsData.io API key | - | ✅ Yes |
| `DEFAULT_LANGUAGE` | News language (en, es, fr, de, etc.) | `en` | ❌ No |
| `DEFAULT_NEWS_COUNT` | Number of articles per request (1-10) | `5` | ❌ No |

### Step 6: Run the Bot

```bash
python main.py
```

**Expected output:**
```
2026-02-10 12:00:00 - __main__ - INFO - Starting bot...
2026-02-10 12:00:01 - httpx - INFO - HTTP Request: POST https://api.telegram.org/bot...
```

✅ **Your bot is now running!**

## 📱 How to Use

### 1. Start the Bot

Open Telegram and search for your bot by username (e.g., `@mynews_bot`)

Send: `/start`

You'll see the **Main Menu** with two buttons:
- 📰 **Latest News**
- ₿ **Crypto News**

### 2. Get Latest News

Click **"📰 Latest News"**

The bot will:
1. Fetch the latest news articles
2. Send 5 articles (default) with:
   - Article image (if available)
   - Article title
   - Source name
   - "Read full article" link

### 3. Browse Crypto News

Click **"₿ Crypto News"**

You'll see a list of cryptocurrencies (200+ coins):
- Bitcoin
- Ethereum  
- Solana
- Cardano
- And many more...

**Select a cryptocurrency** to see related news articles.

### 4. Navigation

Each message includes navigation buttons:
- **« Back to Main Menu** - Return to main menu
- **« Back to Coins** - Return to crypto list

## 📂 Project Structure

```
newsdata_telegram_bot/
├── main.py                 # Entry point - starts the bot
├── req.txt                 # Python dependencies
├── .env.example            # Environment variables template
├── .env                    # Your actual config (create this)
├── .gitignore             # Git ignore rules
└── src/
    ├── __init__.py        # Package initialization
    ├── config.py          # Configuration and settings
    ├── handlers.py        # Message and callback handlers
    ├── keyboards.py       # Inline keyboard definitions
    └── news_fetcher.py    # NewsData.io API integration
```

### File Descriptions

**main.py**
- Initializes the Telegram bot application
- Registers command and callback handlers
- Starts polling for updates

**src/config.py**
- Loads environment variables from `.env`
- Validates required settings
- Provides configuration to other modules

**src/handlers.py**
- `start()` - Handles `/start` command
- `callback_handler()` - Processes button clicks
- Sends news articles with formatting

**src/keyboards.py**
- `main_menu_keyboard()` - Main menu buttons
- `crypto_coins_keyboard()` - List of 200+ crypto coins
- `back_to_main_keyboard()` - Navigation button
- `COINS` - Dictionary of coin symbols to names

**src/news_fetcher.py**
- `get_latest_news()` - Fetches general news
- `get_crypto_news(coin)` - Fetches crypto-specific news
- `fetch_news()` - Generic API request handler

## 🔧 Customization

### Change Number of Articles

Edit `.env`:
```env
DEFAULT_NEWS_COUNT=10
```

Restart the bot to apply changes.

### Change Language

Edit `.env` to set your preferred language:
```env
DEFAULT_LANGUAGE=es  # Spanish
DEFAULT_LANGUAGE=fr  # French
DEFAULT_LANGUAGE=de  # German
DEFAULT_LANGUAGE=pt  # Portuguese
```

**Supported languages**: en, ar, zh, nl, fr, de, he, hi, it, ja, ml, mr, no, pt, ro, ru, es, sv, ta, te, uk

### Add More Cryptocurrencies

Edit `src/keyboards.py` and add entries to the `COINS` dictionary:

```python
COINS = {
    # ... existing coins ...
    "custom": "Your Custom Coin",
}
```

### Change API Endpoint

If you're using a different NewsData.io endpoint or testing locally:

Edit `src/news_fetcher.py`:
```python
LATEST_URL = "https://newsdata.io/api/1/latest"  # Production
CRYPTO_URL = "https://newsdata.io/api/1/crypto"  # Production
```

## 🐛 Troubleshooting

### Bot doesn't respond

**Check:**
1. Bot is running (`python main.py` shows no errors)
2. `.env` file exists and has correct tokens
3. Telegram bot token is valid (check with @BotFather)

### "No news available" message

**Possible causes:**
1. **Invalid NewsData.io API key** - Check your dashboard
2. **API rate limit reached** - Free tier has limits
3. **Network issues** - Check internet connection
4. **Invalid endpoint URL** - Verify URLs in `news_fetcher.py`

**Solution:**
```bash
# Check logs for detailed error messages
python main.py
```

### Photo sending fails

**Cause:** Invalid image URL from API

**Solution:** The bot automatically falls back to text-only messages when images fail. No action needed.

### Import errors

**Cause:** Missing dependencies

**Solution:**
```bash
pip install -r req.txt
```

### "TELEGRAM_BOT_TOKEN is required" error

**Cause:** Missing `.env` file or empty token

**Solution:**
1. Create `.env` file: `cp .env.example .env`
2. Add your bot token to `.env`
3. Restart the bot

## 📊 API Rate Limits

**NewsData.io Free Tier:**
- 200 API calls per day
- Access to latest news and crypto endpoints

**Telegram API:**
- 30 messages per second to the same group
- No limit for private chats

**Tip:** Consider implementing caching for frequently requested news to reduce API calls.

## 🔒 Security Best Practices

1. **Never commit `.env` file** - It's already in `.gitignore`
2. **Keep your tokens secret** - Don't share bot token or API key
3. **Use environment variables** - Don't hardcode credentials
4. **Regenerate tokens** if accidentally exposed

## 🚀 Deployment

### Option 1: Run on VPS (Recommended)

```bash
# Install dependencies
sudo apt update
sudo apt install python3 python3-pip

# Clone repository
git clone https://github.com/your-username/newsdata-telegram-bot.git
cd newsdata-telegram-bot

# Install requirements
pip3 install -r req.txt

# Configure .env
nano .env
# (Add your tokens)

# Run with screen (keeps running after disconnect)
screen -S newsbot
python3 main.py
# Press Ctrl+A, then D to detach

# To reattach: screen -r newsbot
```

### Option 2: Run with systemd (Auto-restart)

Create `/etc/systemd/system/newsbot.service`:

```ini
[Unit]
Description=NewsData Telegram Bot
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/newsdata_telegram_bot
ExecStart=/usr/bin/python3 /path/to/newsdata_telegram_bot/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable newsbot
sudo systemctl start newsbot
sudo systemctl status newsbot
```

### Option 3: Docker (Coming Soon)

## 🔄 Updates & Maintenance

### Update Dependencies

```bash
pip install --upgrade -r req.txt
```

### Check Bot Status

```bash
# If using systemd
sudo systemctl status newsbot

# If using screen
screen -r newsbot
```

### View Logs

Logs are printed to console. For persistent logging:

```bash
python main.py >> bot.log 2>&1
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- [NewsData.io API Documentation](https://newsdata.io/documentation)
- [python-telegram-bot Documentation](https://docs.python-telegram-bot.org/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Report Issues](https://github.com/your-username/newsdata-telegram-bot/issues)

## 💡 Feature Ideas

Want to enhance the bot? Here are some ideas:

- ✅ Add market news endpoint
- ✅ Implement inline search
- ✅ Add bookmarking functionality
- ✅ Schedule daily news digest
- ✅ Support multiple languages per user
- ✅ Add sentiment analysis display
- ✅ Create admin dashboard

---

## 🔔 How to Add Automatic Hourly News Feature

Want to send news automatically to users every hour? Follow these steps:

### Step 1: Create Subscription Manager

Create a new file `src/scheduler.py`:

```python
import logging
import json
from pathlib import Path
from typing import Set

logger = logging.getLogger(__name__)

SUBSCRIPTIONS_FILE = Path(__file__).resolve().parent.parent / "subscriptions.json"


def load_subscriptions() -> Set[int]:
    """Load subscribed user IDs from file."""
    if not SUBSCRIPTIONS_FILE.exists():
        return set()
    
    try:
        with open(SUBSCRIPTIONS_FILE, 'r') as f:
            data = json.load(f)
            return set(data.get('subscribers', []))
    except Exception as e:
        logger.error(f"Error loading subscriptions: {e}")
        return set()


def save_subscriptions(subscribers: Set[int]) -> None:
    """Save subscribed user IDs to file."""
    try:
        with open(SUBSCRIPTIONS_FILE, 'w') as f:
            json.dump({'subscribers': list(subscribers)}, f)
    except Exception as e:
        logger.error(f"Error saving subscriptions: {e}")


def add_subscriber(user_id: int) -> bool:
    """Add a user to the subscription list."""
    subscribers = load_subscriptions()
    if user_id not in subscribers:
        subscribers.add(user_id)
        save_subscriptions(subscribers)
        return True
    return False


def remove_subscriber(user_id: int) -> bool:
    """Remove a user from the subscription list."""
    subscribers = load_subscriptions()
    if user_id in subscribers:
        subscribers.remove(user_id)
        save_subscriptions(subscribers)
        return True
    return False


def is_subscribed(user_id: int) -> bool:
    """Check if a user is subscribed."""
    subscribers = load_subscriptions()
    return user_id in subscribers


def get_all_subscribers() -> Set[int]:
    """Get all subscribed user IDs."""
    return load_subscriptions()
```

### Step 2: Update Keyboards

In `src/keyboards.py`, add the auto-news toggle button to the main menu:

```python
def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📰 Latest News", callback_data="latest"),
            InlineKeyboardButton("₿ Crypto News", callback_data="crypto_menu"),
        ],
        [
            InlineKeyboardButton("⏰ Auto-News (Toggle)", callback_data="toggle_auto_news"),
        ]
    ])
```

### Step 3: Update Handlers

In `src/handlers.py`:

**3a. Add imports at the top:**
```python
from .scheduler import add_subscriber, remove_subscriber, is_subscribed, get_all_subscribers
```

**3b. Update the start function to show subscription status:**
```python
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    subscribed = is_subscribed(user.id)
    subscription_status = "🔔 Auto-news: ON" if subscribed else "🔕 Auto-news: OFF"
    
    text = (
        f"Hello <b>{user.first_name}</b> 👋\n\n"
        "Welcome to the News & Crypto Bot!\n"
        f"{subscription_status}\n\n"
        "Choose an option below:"
    )
    await update.message.reply_html(text, reply_markup=main_menu_keyboard())
```

**3c. Add toggle handler in `callback_handler` function (after the back_main handler):**
```python
    if data == "toggle_auto_news":
        user_id = query.from_user.id
        if is_subscribed(user_id):
            remove_subscriber(user_id)
            message = "🔕 Auto-news disabled\n\nYou will no longer receive hourly news updates."
        else:
            add_subscriber(user_id)
            message = "🔔 Auto-news enabled!\n\nYou will receive latest news every hour automatically."
        
        try:
            await query.edit_message_text(
                message,
                reply_markup=back_to_main_keyboard()
            )
        except Exception:
            await context.bot.send_message(
                chat_id=chat_id,
                text=message,
                reply_markup=back_to_main_keyboard()
            )
        return
```

**3d. Add scheduled news function at the end of `handlers.py`:**
```python
async def send_scheduled_news(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send latest news to all subscribed users."""
    logger.info("Running scheduled news delivery...")
    subscribers = get_all_subscribers()
    
    if not subscribers:
        logger.info("No subscribers for auto-news")
        return
    
    articles = get_latest_news()
    
    if not articles:
        logger.warning("No news available for scheduled delivery")
        return
    
    for user_id in subscribers:
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text="<b>🔔 Hourly News Update</b>",
                parse_mode=ParseMode.HTML
            )
            
            for art in articles[:settings.default_news_count]:
                photo_url = art.get("image_url")
                title = art.get("title", "No title").strip()
                source = art.get("source_name", "—")
                link = art.get("link", "#")
                
                caption = (
                    f"<b>{title}</b>\n"
                    f"<i>{source}</i>\n\n"
                    f"<a href=\"{link}\">Read full article →</a>"
                )
                
                try:
                    if photo_url and photo_url.startswith(("http://", "https://")):
                        await context.bot.send_photo(
                            chat_id=user_id,
                            photo=photo_url,
                            caption=caption,
                            parse_mode=ParseMode.HTML,
                            disable_notification=True
                        )
                    else:
                        await context.bot.send_message(
                            chat_id=user_id,
                            text=caption,
                            parse_mode=ParseMode.HTML,
                            disable_web_page_preview=False
                        )
                except Exception as e:
                    logger.warning(f"Failed to send article to {user_id}: {e}")
                    
        except Exception as e:
            logger.error(f"Failed to send news to user {user_id}: {e}")
            # If user blocked the bot, remove from subscribers
            if "bot was blocked by the user" in str(e).lower():
                remove_subscriber(user_id)
                logger.info(f"Removed blocked user {user_id} from subscribers")
    
    logger.info(f"Scheduled news sent to {len(subscribers)} subscribers")
```

### Step 4: Update main.py

Replace `main.py` with:

```python
#!/usr/bin/env python3

import logging

from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from src.config import settings
from src.handlers import start, callback_handler, send_scheduled_news

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    logger.info("Starting bot...")

    app = Application.builder().token(settings.telegram_bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(callback_handler))

    # Schedule hourly news delivery
    job_queue = app.job_queue
    job_queue.run_repeating(
        send_scheduled_news,
        interval=3600,  # 3600 seconds = 1 hour
        first=60,  # Start after 60 seconds of bot running
        name="hourly_news"
    )
    logger.info("Scheduled hourly news delivery enabled")

    app.run_polling(
        drop_pending_updates=True,
        allowed_updates=["message", "callback_query"]
    )


if __name__ == "__main__":
    main()
```

### Step 5: Customize (Optional)

**Change delivery interval:**
Edit the `interval` parameter in `main.py`:
- Every 30 minutes: `interval=1800`
- Every 2 hours: `interval=7200`
- Every 6 hours: `interval=21600`
- Daily: `interval=86400`

**Change number of articles:**
Edit `.env` file:
```env
DEFAULT_NEWS_COUNT=5
```

### Step 6: Run the Bot

```bash
python main.py
```

You should see:
```
2026-02-11 12:00:00 - __main__ - INFO - Starting bot...
2026-02-11 12:00:01 - __main__ - INFO - Scheduled hourly news delivery enabled
```

### How Users Enable Auto-News:

1. Start the bot: `/start`
2. Click "⏰ Auto-News (Toggle)" button
3. Receive confirmation: "🔔 Auto-news enabled!"
4. Every hour, they'll receive the latest news automatically
5. Click toggle again to disable

### Files Created:
- `src/scheduler.py` - Subscription management
- `subscriptions.json` - Auto-generated file storing subscriber IDs (don't manually create)

---

## 📧 Support

Need help?

- 📖 [Check the documentation](https://newsdata.io/documentation)
- 💬 [Open an issue](https://github.com/your-username/newsdata-telegram-bot/issues)
- 📧 Email: support@newsdata.io

## 🙏 Acknowledgments

- [NewsData.io](https://newsdata.io) - For providing the news API
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - For the excellent Telegram Bot library
- Contributors and users of this project

---

**Made with ❤️ for the Telegram community**

⭐ **Star this repo if you find it helpful!**