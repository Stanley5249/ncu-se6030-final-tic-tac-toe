import sys

from PySide6 import QtWidgets
import PySide6.QtGui as QtGui

from .gui import MyWidget


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setPalette(QtGui.QPalette(QtGui.QColor('#222')))
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
