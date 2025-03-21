from collections.abc import Iterator
from typing import Literal

from PySide6 import QtCore, QtWidgets

type Marker = Literal["X", "O", ""]

MARKER_TO_COLOR: dict[Marker, str] = {"X": "cyan", "O": "red"}


class TicTacToe:
    def __init__(self):
        self.marker_it = marker_cycle()
        self.board: dict[tuple[int, int], Marker] = {
            (i, j): "" for i in range(3) for j in range(3)
        }
        self.gui = GUI(self)

    def reset_board(self):
        self.marker_it = marker_cycle()

        for key in self.board:
            self.board[key] = ""

        self.gui.reset_board()

    def check_winner(self, marker: Marker) -> bool:
        board = self.board

        for row in range(3):
            if all(board[row, col] == marker for col in range(3)):
                return True

        for col in range(3):
            if all(board[row, col] == marker for row in range(3)):
                return True

        if all(board[i, i] == marker for i in range(3)):
            return True

        if all(board[i, 2 - i] == marker for i in range(3)):
            return True

        return False

    def place_marker(self, x: int, y: int) -> None:
        if self.board[x, y] != "":
            return

        marker = next(self.marker_it)
        self.board[x, y] = marker
        self.gui.on_click(x, y, marker)

        if self.check_winner(marker):
            self.gui.game_over(marker)
            self.reset_board()

        elif all(cell != "" for cell in self.board.values()):
            self.gui.draw()
            self.reset_board()


class GUI:
    def __init__(self, game: TicTacToe):
        # ======================================================================
        # init widgets
        # ======================================================================

        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Tic-Tac-Toe")
        self.window.setGeometry(100, 100, 300, 300)

        self.main_widget = QtWidgets.QWidget(self.window)
        self.main_widget.setStyleSheet("font-size: 32px;")

        self.board_panel = QtWidgets.QWidget(self.main_widget)

        self.status_label = QtWidgets.QLabel("", self.main_widget)
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status_label.setFixedHeight(50)

        self.buttons = {
            (i, j): QtWidgets.QPushButton("", self.board_panel)
            for i in range(3)
            for j in range(3)
        }
        for (i, j), button in self.buttons.items():
            button.setFixedSize(100, 100)
            button.clicked.connect(lambda _, x=i, y=j: game.place_marker(x, y))

        # ======================================================================
        # init layouts
        # ======================================================================

        window_layout = QtWidgets.QVBoxLayout(self.window)
        window_layout.addWidget(self.main_widget)

        main_widget_layout = QtWidgets.QVBoxLayout(self.main_widget)
        main_widget_layout.addStretch(1)
        main_widget_layout.addWidget(self.status_label)
        main_widget_layout.addStretch(1)
        main_widget_layout.addWidget(self.board_panel)

        board_panel_layout = QtWidgets.QGridLayout(self.board_panel)
        for (i, j), button in self.buttons.items():
            board_panel_layout.addWidget(button, i, j)

        # ======================================================================
        # set layouts
        # ======================================================================

        self.window.setLayout(main_widget_layout)
        self.main_widget.setLayout(main_widget_layout)
        self.board_panel.setLayout(board_panel_layout)

    def on_click(self, x: int, y: int, marker: Marker) -> None:
        self.status_label.setText(f"It's {marker}'s turn")

        button = self.buttons[x, y]
        button.setText(marker)
        color = MARKER_TO_COLOR[marker]
        button.setStyleSheet(f"color: {color!r};")

    def reset_board(self) -> None:
        for button in self.buttons.values():
            button.setText("")

        self.status_label.setText("")

    def game_over(self, marker: Marker) -> None:
        QtWidgets.QMessageBox.information(
            self.window,
            "Game Over",
            f"{marker} wins!",
            QtWidgets.QMessageBox.StandardButton.Ok,
        )

    def draw(self) -> None:
        QtWidgets.QMessageBox.information(
            self.window,
            "Game Over",
            "Draw!",
            QtWidgets.QMessageBox.StandardButton.Ok,
        )


def marker_cycle() -> Iterator[Marker]:
    while True:
        yield "X"
        yield "O"
