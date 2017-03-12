""" Tsuki > src > gui > main_window.py

    Main GUI design of the application.
"""

from PyQt5. QtWidgets import QMainWindow, QListView


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

