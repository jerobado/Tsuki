# Objective: attempting to write my first tests

import sys
import unittest

sys.path.append('../')

from PyQt5.QtWidgets import QApplication
from src.gui.main_window import Tsuki

APP = QApplication(sys.argv)


class TestTsukiGUI(unittest.TestCase):

    def test_tsuki_windowTitle(self):
        tsuki = Tsuki()
        self.assertEqual(tsuki.windowTitle(), 'Tsuki つき 0.1', 'tsuki.windowTitle is the same')

    def test_timeline_is_updated_by_tweets(self):
        tsuki = Tsuki()
        self.assertEqual(tsuki.updateTimeline(), True, 'tsuki.updateTimeline is updated by 10 tweets')


if __name__ == '__main__':
    unittest.main()
