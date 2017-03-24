""" Tsuki > src > gui > main_window.py

    Main GUI design of the application.
"""

from TwitterAPI import TwitterAPI
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow,
                             QListView,
                             QAction)

from src.resources import resources
from src.resources.models import TimelineListModel


class Tsuki(QMainWindow):
    """ Main window for Tsuki """

    def __init__(self, parent=None):

        super(Tsuki, self).__init__(parent)
        self._widgets()
        self._layout()
        self._properties()
        self._createActions()
        self._createToolbar()
        #self.show()

    def _widgets(self):

        self.timelineListView = QListView()
        self.timelineListView.setWrapping(True)

    def _layout(self):

        self.setCentralWidget(self.timelineListView)

    def _properties(self):

        self.resize(325, 500)   # width, height
        self.setWindowTitle('Tsuki つき 0.1')

    def _createActions(self):

        self.updateAction = QAction(QIcon(':/update-1.png'), 'Update timeline', self,
                                    triggered=self.updateTimeline)
        self.tweetAction = QAction(QIcon(':/tweet-2.png'), 'Send tweet', self,
                                    triggered=self.sendTweet)
        self.retweetAction = QAction(QIcon(':/retweet-2.png'), 'Retweet', self,
                                    triggered=self.reTweet)
        self.sendAction = QAction(QIcon(':/send-1.png'), 'Send message', self,
                                    triggered=self.sendMessage)

    def _createToolbar(self):

        self.tsukiToolBar = self.addToolBar('Tsuki')
        self.tsukiToolBar.addAction(self.updateAction)
        self.tsukiToolBar.addAction(self.tweetAction)
        self.tsukiToolBar.addAction(self.retweetAction)
        self.tsukiToolBar.addAction(self.sendAction)

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

    def updateTimeline(self, count=10):

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
        print("[Tsuki]: Timeline updated")

        model = TimelineListModel(TIMELINE_LIST)
        self.timelineListView.setModel(model)

    def sendTweet(self, message=""):

        while True:
            message = input("[Tsuki]: What's happening? ")
            if len(message) > 0:
                print("[Tsuki]: Sending tweet...")
                r = api.request('statuses/update', {'status': message})
                if r.status_code == 200:
                    print("[Tsuki]: Tweet sent!")
                    break
                else:
                    print("[Tsuki]: Tweet not sent.")
                    break
            else:
                print("[Tsuki]: You should write something inspiring! :)")

    def reTweet(self, message):

        print('[Tsuki]: Retweeted!')


    def sendMessage(self, message):

        print('[Tsuki]: Message sent!')