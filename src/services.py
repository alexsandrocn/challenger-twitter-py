from typing import List, Dict, Any

import tweepy

from src.connection import trends_collection
from src.constants import WOEID
from src.secrets import consumer_key, access_token, access_token_secret, consumer_secret


def _get_trends(woe_id: int) -> List[Dict[str, Any]]:
    """Get treending topics from Twitter API.
    Args:
        woe_id (int): Identifier of location.
    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    trends = api.trends_place(woe_id)

    return trends[0]["trends"]


def get_trends_from_mongo() -> List[Dict[str, Any]]:
    """Get trends topics and save on MongoDB."""
    trends = trends_collection.find({})
    return list(trends)


def save_trends() -> None:
    trends = _get_trends(woe_id=WOEID)
    trends_collection.insert_many(trends)


