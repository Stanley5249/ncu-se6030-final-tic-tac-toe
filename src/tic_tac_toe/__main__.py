import sys

from PySide6 import QtWidgets
from qt_material import apply_stylesheet

from .gui import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_teal.xml")

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
