from twitter import *
import sys
import config


class TwitterSearch:

    @staticmethod
    def search(terms):
        sys.path.append('.')
        twitter = Twitter(auth=OAuth(config.ACCESS_KEY, config.SECRET_KEY, config.CONSUMER_KEY, config.CONSUMER_SECRET))
        results = twitter.users.search(q=terms)

        for user in results:
            print("@%s (%s): %s" % (user["screen_name"], user["name"]))