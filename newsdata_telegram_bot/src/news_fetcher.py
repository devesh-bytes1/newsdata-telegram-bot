import logging
from typing import List, Dict

import requests

from .config import settings

logger = logging.getLogger(__name__)

LATEST_URL = "https://local.newsdata.io/api/1/latest"
CRYPTO_URL = "https://local.newsdata.io/api/1/crypto"


def fetch_news(endpoint: str, params: dict) -> List[Dict]:
    
    try:
        resp = requests.get(endpoint, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        if data.get("status") != "success":
            logger.warning(f"API error: {data.get('message', 'Unknown')}")
            return []

        return data.get("results", [])

    except Exception as e:
        logger.error(f"Request failed: {e}")
        return []


def get_latest_news() -> List[Dict]:
    params = {
        "apikey": settings.newsdata_api_key,
        "language": settings.default_language,
        "size": min(settings.default_news_count, 10),
    }
    return fetch_news(LATEST_URL, params)


def get_crypto_news(coin: str) -> List[Dict]:
    params = {
        "apikey": settings.newsdata_api_key,
        "coin": coin,
        "language": settings.default_language,
        "size": min(settings.default_news_count, 10),
    }
    return fetch_news(CRYPTO_URL, params)