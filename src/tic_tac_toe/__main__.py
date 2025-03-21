import sys

from PySide6 import QtWidgets
from qt_material import apply_stylesheet

from .core import TicTacToe

__all__ = ["main"]


def apply_custom_stylesheet(app: QtWidgets.QApplication) -> None:
    extra = {
        "font_family": "Consolas",
        "font_size": "20px",
    }
    apply_stylesheet(app, "dark_teal.xml", extra=extra)


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    apply_custom_stylesheet(app)
    game = TicTacToe()
    game.gui.window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
