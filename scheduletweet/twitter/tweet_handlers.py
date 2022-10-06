import logging
import arrow
import os
import tweepy

from twitter.models import TwitterSchedulerModel

logger = logging.getLogger(__name__)


def send_tweets(consumer_key, consumer_secret, access_token,access_token_secret):
    expired_tweets = TwitterSchedulerModel.objects.filter(
        sent=False, tweet_at__lte=arrow.utcnow().datetime)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    if expired_tweets.count() == 0:
        logging.info("No tweet to send as of now")
    for db_tweet in expired_tweets:
        logging.info('sending tweet')
        api.update_status(db_tweet.tweet)
        logging.info('tweet sent')
        db_tweet.sent = True
        db_tweet.save()


def tweet_scheduler():
    consumer_key = "JeWxj1otXrhTHuZf3hqkc7mC6"
    consumer_secret = "zcCzzVl837T0mYx0CrsXHiHLR0wwX4zl0RpMFXrIUbzvs6kQRV"
    access_token = "1576480519822327810-gA2CExhfaiAMCBaunOZfeAc6lk2e4a"
    access_token_secret = "wZyTIxkg93ZCJRHClTgmLcUjWRo6rRI7vD6q8StJnkDFa"
    send_tweets(consumer_key, consumer_secret, access_token, access_token_secret)
    


#client Id = SENnNWxjUGVodkx2X0ZzdjBsNWM6MTpjaQ
#client secret = GpIWrV9E6-7eSAUlsUnFzbTc7bqWMMLaY6pKa4yloUElkjzrf2
#client secret (auth) = GpIWrV9E6-7eSAUlsUnFzbTc7bqWMMLaY6pKa4yloUElkjzrf2
