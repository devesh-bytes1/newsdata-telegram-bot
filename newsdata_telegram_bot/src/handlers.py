import logging

from telegram import Update, InputMediaPhoto
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from .news_fetcher import get_latest_news, get_crypto_news
from .keyboards import (
    main_menu_keyboard,
    crypto_coins_keyboard,
    back_to_main_keyboard,
    back_to_crypto_keyboard,
    COINS,
)
from .config import settings
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    text = (
        f"Hello <b>{user.first_name}</b> 👋\n\n"
        "Welcome to the News & Crypto Bot!\n"
        "Choose an option below:"
    )
    await update.message.reply_html(text, reply_markup=main_menu_keyboard())


async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    data = query.data
    chat_id = query.message.chat_id

    if data in ("back_main", "main"):
        try:
            await query.edit_message_text(
                "Main Menu:", reply_markup=main_menu_keyboard()
            )
        except Exception:
            # If editing fails, send a new message
            await context.bot.send_message(
                chat_id=chat_id,
                text="Main Menu:",
                reply_markup=main_menu_keyboard()
            )
        return

    if data == "latest":
        await query.edit_message_text("Fetching latest news...")
        articles = get_latest_news()

        if not articles:
            await query.edit_message_text(
                "No news available right now or API issue.",
                reply_markup=back_to_main_keyboard()
            )
            return

        await context.bot.send_message(
            chat_id=chat_id,
            text="<b>📰 Latest News</b>",
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
                        chat_id=chat_id,
                        photo=photo_url,
                        caption=caption,
                        parse_mode=ParseMode.HTML,
                        disable_notification=True,
                        reply_markup=back_to_main_keyboard()
                    )
                else:
                    await context.bot.send_message(
                        chat_id=chat_id,
                        text=caption,
                        parse_mode=ParseMode.HTML,
                        disable_web_page_preview=False,
                        reply_markup=back_to_main_keyboard()
                    )
            except Exception as e:
                logger.warning(f"Failed to send photo: {e}")
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=caption,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=False,
                    reply_markup=back_to_main_keyboard()
                )

    elif data == "crypto_menu":
        try:
            await query.edit_message_text(
                "Select a cryptocurrency:", reply_markup=crypto_coins_keyboard()
            )
        except Exception:
            await context.bot.send_message(
                chat_id=chat_id,
                text="Select a cryptocurrency:",
                reply_markup=crypto_coins_keyboard()
            )

    elif data.startswith("crypto:"):
        coin_symbol = data.split(":", 1)[1]
        coin_name = COINS.get(coin_symbol, coin_symbol.upper())

        await query.edit_message_text(f"Fetching {coin_name} news...")

        articles = get_crypto_news(coin=coin_symbol)

        if not articles:
            await query.edit_message_text(
                f"No recent news found for {coin_name}.",
                reply_markup=back_to_crypto_keyboard()
            )
            return

        await context.bot.send_message(
            chat_id=chat_id,
            text=f"<b>₿ {coin_name} News</b>",
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
                        chat_id=chat_id,
                        photo=photo_url,
                        caption=caption,
                        parse_mode=ParseMode.HTML,
                        disable_notification=True,
                        reply_markup=back_to_crypto_keyboard()
                    )
                else:
                    await context.bot.send_message(
                        chat_id=chat_id,
                        text=caption,
                        parse_mode=ParseMode.HTML,
                        disable_web_page_preview=False,
                        reply_markup=back_to_crypto_keyboard()
                    )
            except Exception as e:
                logger.warning(f"Failed to send photo: {e}")
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=caption,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=False,
                    reply_markup=back_to_crypto_keyboard()
                )