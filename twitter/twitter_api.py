
import requests

from decouple import config
import tweepy


class Twitter:

    def __init__(self, version=2):
        self.API_KEY = config("TWITTER_API_KEY")
        self.API_SECRET = config("TWITTER_API_SECRET")
        self.BEARER = config("TWITTER_BEARER_TOKEN")
        self.ACCESS_TOKEN = config("TWITTER_ACCESS_TOKEN")
        self.ACCESS_SECRET = config("TWITTER_ACCESS_SECRET")

    def client(self):
        api = tweepy.OAuth1UserHandler(
            consumer_key=self.API_KEY,
            consumer_secret=self.API_SECRET,
            access_token=self.ACCESS_TOKEN,
            access_token_secret=self.ACCESS_SECRET
        )
        return tweepy.API(api, wait_on_rate_limit=True)


if __name__ == "__main__":

    pass




