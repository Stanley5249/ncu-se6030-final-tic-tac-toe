from typing import override

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PySide6 import QtCore, QtGui, QtWidgets

from .d2Playground import D2Playground


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OOXX")
        self.resize(1000, 600)
        self.setStyleSheet("QWidget { font: 14px Microsoft JhengHei; }")
        self.setUpdatesEnabled(True)
        icon = QtGui.QIcon()
        self.setWindowIcon(icon)
        self.setWindowIconText("OOXX")
        self.ui()

        self.pg = D2Playground()

    def ui(self) -> None:
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.main_layout = QtWidgets.QHBoxLayout(self.central_widget)

        self.left_panel = QtWidgets.QWidget()
        self.left_layout = QtWidgets.QVBoxLayout(self.left_panel)

        self.game_board_widget = QtWidgets.QWidget()
        self.game_board_layout = QtWidgets.QGridLayout(self.game_board_widget)

        self.create_game_buttons()

        self.control_panel_widget = QtWidgets.QWidget()
        self.control_panel_layout = QtWidgets.QVBoxLayout(self.control_panel_widget)

        self.game_start_btn = QtWidgets.QPushButton()
        self.game_start_btn.setText("開始遊戲")
        self.game_start_btn.setAutoDefault(True)
        self.game_start_btn.setShortcut("Ctrl+S")
        self.game_start_btn.clicked.connect(self.on_game_start_btn_pressed)
        self.control_panel_layout.addWidget(self.game_start_btn)

        self.status_panel_widget = QtWidgets.QWidget()
        self.status_panel_layout = QtWidgets.QVBoxLayout(self.status_panel_widget)

        self.status_label = QtWidgets.QTextBrowser()
        self.status_label.setText("狀態：\n")
        self.status_panel_layout.addWidget(self.status_label)

        self.left_layout.addWidget(self.game_board_widget)
        self.left_layout.addWidget(self.control_panel_widget)
        self.left_layout.addWidget(self.status_panel_widget)

        self.main_layout.addWidget(self.left_panel)

        self.gv_size = 600
        gs_size = self.gv_size
        self.playground_gv = QtWidgets.QGraphicsView()
        self.playground_gs = QtWidgets.QGraphicsScene()
        self.playground_gs.setSceneRect(0, 0, gs_size, gs_size)
        self.playground_gv.setScene(self.playground_gs)

        self.main_layout.addWidget(self.playground_gv)

    def create_game_buttons(self) -> None:
        for y in range(3, 0, -1):
            for x in range(1, 4):
                btn = QtWidgets.QPushButton()
                btn.setText(f"{x}{y}")
                btn.clicked.connect(
                    lambda checked=False, x=x, y=y: self.on_place_btn_pressed(x, y)
                )

                setattr(self, f"btn{x}{y}", btn)

                self.game_board_layout.addWidget(btn, 3 - y, x - 1)

    def disable_place_btn(self) -> None:
        for i in range(1, 4):
            for j in range(1, 4):
                btn = getattr(self, f"btn{i}{j}")
                btn.setEnabled(False)

    def enable_place_btn(self) -> None:
        for i in range(1, 4):
            for j in range(1, 4):
                btn = getattr(self, f"btn{i}{j}")
                btn.setEnabled(True)

    def on_game_start_btn_pressed(self) -> None:
        self.pg.Reset()
        self.set_next_graph_view()
        self.status_label.setText(f"狀態\n下一位玩家是 {self.pg.next_player}")
        self.enable_place_btn()

    def on_place_btn_pressed(self, x: int, y: int) -> None:
        if not self.pg.CheckPlaceable(x, y):
            self.status_label.setText(
                f"狀態\n下一位玩家是 {self.pg.next_player}\n無法落子"
            )
            return

        self.pg.Place(x, y)
        self.status_label.setText(f"狀態\n下一位玩家是 {self.pg.next_player}")

        self.set_next_graph_view()

        winner = self.pg.CheckWinner()
        if winner != "none":
            if winner == "draw":
                self.status_label.setText("狀態\n平手")
            else:
                self.status_label.setText(f"狀態\n{winner} 獲勝")

            self.disable_place_btn()

    def set_next_graph_view(self) -> None:
        next_fig = self.pg.RenderPlayground(self.pg.circle, self.pg.cross)
        self.playground_canvas = FigureCanvasQTAgg(next_fig)
        self.playground_gs.clear()
        self.playground_gs.addWidget(self.playground_canvas)
        self.playground_gv.setScene(self.playground_gs)

    @override
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key.Key_Escape:
            instance = QtCore.QCoreApplication.instance()
            if instance is not None:
                instance.quit()
            self.close()
        elif event.key() == QtCore.Qt.Key.Key_F11:
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()
        elif event.key() == QtCore.Qt.Key.Key_F12:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()
