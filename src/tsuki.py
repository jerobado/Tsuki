""" Tsuki: your personal Twitter client application

    Interface   :   GUI (PyQt5)
    Language    :   Python 3.6.0
    Created     :   8 Mar 2017 2:02 AM
    Version     :   0.1
    Author      :   Jero Bado <tokidokitalkyou@gmail.com>
"""

import sys

from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterConnectionError, TwitterRequestError


def authenticate():
    """ This will will established an authentication using the keys given. """

    # NOTE: Provide your own keys!
    from src.resources.constants import (CONSUMER_KEY,
                                         CONSUMER_SECRET,
                                         ACCESS_KEY,
                                         ACCESS_SECRET)

    print("[Tsuki]: Authenticating, please do wait...")
    global api
    api = TwitterAPI(consumer_key=CONSUMER_KEY,
                     consumer_secret=CONSUMER_SECRET,
                     access_token_key=ACCESS_KEY,
                     access_token_secret=ACCESS_SECRET)
    print("[Tsuki]: Authentication successful!")


def update_timeline(count):

    print("[Tsuki]: Updating timeline...")
    r = api.request('statuses/home_timeline', {'count': count})
    for item in r.get_iterator():
        if 'text' in item:
            twitter_time = item['created_at']
            twitter_name = item['user']['name']
            twitter_handle = item['user']['screen_name']
            twitter_tweet = item['text']

            # Output format: [time] name (@screen_name): text
            print("[{0}] {1} (@{2}): {3}".format(twitter_time,
                                                twitter_name,
                                                twitter_handle,
                                                twitter_tweet))


def main():
    """ The working code of Tsuki """

    from PyQt5.QtWidgets import QApplication
    from src.gui.main_window import Tsuki
    
    APP = QApplication(sys.argv)
    window = Tsuki()
    APP.exec()


if __name__ == '__main__':
    try:
        authenticate()
        update_timeline(10)
        sys.exit(main())
    except TwitterConnectionError:
        print('[Tsuki]: Connection failed. Try to reconnect.')
    except TwitterRequestError:
        print('[Tsuki]: Request failed. Check your tokens.')
