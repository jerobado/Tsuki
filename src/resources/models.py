# Models to be created here

from PyQt5.QtCore import (Qt,
                          QModelIndex,
                          QAbstractListModel)


class TimelineListModel(QAbstractListModel):
    """ Model class for holding a list of tweets in the timeline """

    def __init__(self, timelinelist, parent=None):
        super(TimelineListModel, self).__init__(parent)
        self.__timelinelist = timelinelist

    def data(self, index, role):
        if role == Qt.DisplayRole:
            row = index.row()
            value = self.__timelinelist[row]
            return value

    def rowCount(self, parent):
        return len(self.__timelinelist)

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

