""" Tsuki: your personal Twitter client application

    Interface   :   GUI (PyQt5)
    Language    :   Python 3.6.0
    Created     :   8 Mar 2017 2:02 AM
    Version     :   0.1
    Author      :   Jero Bado <tokidokitalkyou@gmail.com>
"""

import sys

from TwitterAPI import TwitterConnectionError, TwitterRequestError


def main():
    """ The working code of Tsuki """

    from PyQt5.QtWidgets import QApplication
    from src.gui.main_window import Tsuki
    
    APP = QApplication(sys.argv)
    tsuki = Tsuki()
    tsuki.authenticate()
    #suki.sendTweet()
    #tsuki.updateTimeline(20)
    tsuki.show()
    APP.exec()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except TwitterConnectionError:
        print('[Tsuki]: Connection failed. Try to reconnect.')
    except TwitterRequestError:
        print('[Tsuki]: Request failed. Check your tokens.')
