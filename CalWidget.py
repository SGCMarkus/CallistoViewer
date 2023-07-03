from PyQt6 import QtCore, QtGui, QtWidgets

class CalWidget(QtWidgets.QLabel):
    selectedDate = QtCore.QDate.currentDate()

    def __init__(self, parent=None):
        super(CalWidget, self).__init__(parent)
        self.calButton = QtWidgets.QToolButton(self)
        self.calButton.setIcon(QtGui.QIcon('images/calendarIcon.png'))
        self.calButton.setStyleSheet('border: 0px; padding: 0px;')
        self.calButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.calButton.clicked.connect(self.showCalWid)
        self.setText(self.selectedDate.toString("dd/MM/yyyy"))

    def resizeEvent(self, event):
        buttonSize = self.calButton.sizeHint()
        frameWidth = self.style().pixelMetric(QtWidgets.QStyle.PixelMetric.PM_DefaultFrameWidth)
        self.calButton.move(int(self.rect().right() - frameWidth - buttonSize.width()),
                         int((self.rect().bottom() - buttonSize.height() + 1)/2))
        super(CalWidget, self).resizeEvent(event)

    def showCalWid(self):
        self.calendar = QtWidgets.QCalendarWidget()
        self.calendar.setMinimumDate(QtCore.QDate(1970, 1, 1))
        self.calendar.setMaximumDate(QtCore.QDate.currentDate())
        self.calendar.setSelectedDate(self.selectedDate)
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.updateDate)
        self.calendar.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.calendar.setStyleSheet('background: white; color: black')
        self.calendar.setGridVisible(True)
        pos = QtGui.QCursor.pos()
        self.calendar.setGeometry(pos.x(), pos.y(),300, 200)
        self.calendar.show()

    def updateDate(self,*args):
        self.selectedDate = self.calendar.selectedDate()
        getDate = self.selectedDate.toString("dd/MM/yyyy")
        self.setText(getDate)
        self.calendar.deleteLater()
