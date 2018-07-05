from twitter import *
import sys
import credentials


class TwitterSearch:

    @staticmethod
    def search(terms):
        sys.path.append('.')
        twitter = Twitter(auth=OAuth(credentials.ACCESS_KEY, credentials.SECRET_KEY, credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET))
        results = twitter.users.search(q=terms)

        for user in results:
            print("@%s (%s): %s" % [user['screen_name'], user["name"]])