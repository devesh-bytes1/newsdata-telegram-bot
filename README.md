![NewsData.io Telegram Bot](https://github.com/user-attachments/assets/b2f3cc3f-183f-4ef0-b68b-80bd0a47764d)

# 📰 NewsData.io Telegram Bot

Turn any Telegram chat into your own personal newsroom. This bot delivers the **latest world news** and **cryptocurrency news** straight to your conversations, powered by the [NewsData.io API](https://newsdata.io). No website to open and no extra app to install — just tap a button and the headlines come to you, complete with images and source links.

Whether you want a quick pulse on global events or you're tracking 200+ crypto coins, everything happens right inside Telegram through clean, tappable inline keyboards.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-26A5E4.svg)
![Powered by NewsData.io](https://img.shields.io/badge/Powered%20by-NewsData.io-orange.svg)

## ✨ Why You'll Like It

- **📰 Latest News** — fresh headlines from around the world, updated in real time
- **₿ Crypto News** — dedicated coverage for 200+ cryptocurrencies, from Bitcoin to the long tail
- **🖼️ Rich Media** — every article arrives with its image, headline, and a link to read more
- **🔘 Tap-to-Browse** — interactive inline keyboards mean zero typing
- **⚙️ Configurable** — set your preferred language and how many articles you want per request
- **🚀 Fast & Async** — built on the modern, asynchronous `python-telegram-bot` library
- **🆓 Free-Tier Friendly** — works out of the box with a free NewsData.io API key

## 🎯 What It Does

The bot keeps things simple with two core features:

1. **Latest News** — pulls general, up-to-the-minute headlines from across the globe so you never miss what's happening.
2. **Crypto News** — lets you pick a coin from a list of 200+ cryptocurrencies and instantly see the news that's moving the market.

Each story is delivered as a photo card with a caption and a direct link, so you can skim quickly and dive deeper only when something catches your eye.

## 🚀 Getting Started

### 1. Prerequisites

- Python **3.8+**
- A **Telegram bot token** from [@BotFather](https://t.me/botfather)
- A free **NewsData.io API key** from [newsdata.io/register](https://newsdata.io/register) (it looks like `pub_xxxxxxxx`)

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/newsdata-telegram-bot.git
cd newsdata-telegram-bot/newsdata_telegram_bot
```

### 3. Install the Dependencies

```bash
pip install -r req.txt
```

### 4. Add Your Credentials

Copy the example environment file and fill in your keys:

```bash
cp .env.example .env
```

Then open `.env` and set:

```ini
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
NEWSDATA_API_KEY=pub_xxxxxxxxxxxxxxxx

# Optional tweaks
DEFAULT_LANGUAGE=en      # en, es, fr, de, hi, ...
DEFAULT_NEWS_COUNT=5     # 1-10 articles per request
```

### 5. Run the Bot

```bash
python main.py
```

Open Telegram, send `/start` to your bot, and start browsing the news. That's it! 🎉

## ⚙️ Configuration Options

| Variable | Description | Default |
|---|---|---|
| `TELEGRAM_BOT_TOKEN` | Your bot token from @BotFather | *(required)* |
| `NEWSDATA_API_KEY` | Your NewsData.io API key | *(required)* |
| `DEFAULT_LANGUAGE` | Language code for news results | `en` |
| `DEFAULT_NEWS_COUNT` | Number of articles per request (1–10) | `5` |

## 🛠️ How It's Built

```
newsdata_telegram_bot/
├── main.py              # Entry point — wires up handlers and starts polling
├── req.txt              # Python dependencies
├── .env.example         # Template for your credentials
└── src/
    ├── config.py        # Loads and validates settings from .env
    ├── handlers.py      # Telegram command and button callbacks
    ├── keyboards.py     # Inline keyboard layouts + the coin list
    └── news_fetcher.py  # Talks to the NewsData.io API
```

The bot uses the asynchronous `python-telegram-bot` library for responsive, non-blocking interactions, and a small `requests`-based fetcher to call the NewsData.io endpoints.

## 🌍 About NewsData.io

[NewsData.io](https://newsdata.io) is a powerful news API that gives developers access to breaking news, historical archives, and crypto news from thousands of sources worldwide. The generous **free tier** makes it perfect for side projects like this one — sign up, grab your key, and you're ready to build.

## 🤝 Contributing

Contributions, ideas, and bug reports are welcome! Feel free to open an issue or submit a pull request. If you build something cool on top of this, we'd love to hear about it.

## 📄 License

This project is released under the **MIT License** — free to use, modify, and share.

---

Built with ❤️ and the [NewsData.io API](https://newsdata.io).
