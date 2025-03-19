import sys

from PySide6 import QtWidgets

from .gui import MyWidget


def main():
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
