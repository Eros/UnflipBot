from twitter import *
import credentials

import twitter_search as ts


def main():
    twitter = Twitter(auth=OAuth(credentials.ACCESS_KEY, credentials.SECRET_KEY, credentials.CONSUMER_KEY,
                                 credentials.CONSUMER_SECRET))
    print("Attempted to auth bot")


if __name__ == '__main__':
    main()
