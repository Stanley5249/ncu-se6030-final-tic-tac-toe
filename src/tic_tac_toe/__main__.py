import sys

from PySide6 import QtGui, QtWidgets

from .gui import MyWidget


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setPalette(QtGui.QPalette(QtGui.QColor("#222")))
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
