""" Tsuki > src > gui > main_window.py

    Main GUI design of the application.
"""

from TwitterAPI import TwitterAPI
from PyQt5.QtWidgets import QMainWindow, QListView

from src.resources.models import TimelineListModel


class Tsuki(QMainWindow):
    """ Main window for Tsuki """

    def __init__(self, parent=None):

        super(Tsuki, self).__init__(parent)
        self._widgets()
        self._layout()
        self._properties()
        self.show()

    def _widgets(self):

        self.timelineListView = QListView()

    def _layout(self):

        self.setCentralWidget(self.timelineListView)

    def _properties(self):

        self.resize(325, 500)   # width, height
        self.setWindowTitle('Tsuki つき 0.1')

    # TSUKI METHODS DEFINITION STARTS HERE
    def authenticate(self):
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

    def updateTimeline(self, count):

        TIMELINE_LIST = []
        print("[Tsuki]: Updating timeline...")
        r = api.request('statuses/home_timeline', {'count': count})
        for item in r.get_iterator():
            if 'text' in item:
                twitter_time = item['created_at']
                twitter_name = item['user']['name']
                twitter_handle = item['user']['screen_name']
                twitter_tweet = item['text']

                # Output format: [time] name (@screen_name): text
                # print("[{0}] {1} (@{2}): {3}".format(twitter_time,
                #                                    twitter_name,
                #                                    twitter_handle,
                #                                    twitter_tweet))
                TIMELINE_LIST.append(twitter_tweet)

        model = TimelineListModel(TIMELINE_LIST)
        self.timelineListView.setModel(model)