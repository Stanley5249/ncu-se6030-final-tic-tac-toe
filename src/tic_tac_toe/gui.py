import PySide6.QtCore as QtCore
import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from .d2Playground import D2Playground


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OOXX")
        self.resize(1000, 600)
        self.setStyleSheet(
            "QWidget { font: 14px Microsoft JhengHei; color: #fff; background: #222; background-color: #222; }"
        )
        self.setUpdatesEnabled(True)
        Icon = QtGui.QIcon()
        self.setWindowIcon(Icon)
        self.setWindowIconText("OOXX")
        self.ui()

        self.pg = D2Playground()

    def ui(self):
        self.box = QtWidgets.QWidget(self)
        self.box.setGeometry(0, 0, 300, 600)
        self.grid = QtWidgets.QGridLayout(self.box)

        self.GameStartBtn = QtWidgets.QPushButton(self)
        self.GameStartBtn.setText("開始遊戲")
        self.GameStartBtn.setAutoDefault(True)
        self.GameStartBtn.setShortcut("Ctrl+S")
        self.GameStartBtn.clicked.connect(self.onGameStartBtnPressed)
        self.grid.addWidget(self.GameStartBtn, 3, 0)

        self.btn11 = QtWidgets.QPushButton(self)
        self.btn11.setText("11")
        self.btn11.clicked.connect(lambda: self.onPlaceBtnPressed(1, 1))
        self.grid.addWidget(self.btn11, 2, 0)
        self.btn12 = QtWidgets.QPushButton(self)
        self.btn12.setText("12")
        self.btn12.clicked.connect(lambda: self.onPlaceBtnPressed(1, 2))
        self.grid.addWidget(self.btn12, 1, 0)
        self.btn13 = QtWidgets.QPushButton(self)
        self.btn13.setText("13")
        self.btn13.clicked.connect(lambda: self.onPlaceBtnPressed(1, 3))
        self.grid.addWidget(self.btn13, 0, 0)
        self.btn21 = QtWidgets.QPushButton(self)
        self.btn21.setText("21")
        self.btn21.clicked.connect(lambda: self.onPlaceBtnPressed(2, 1))
        self.grid.addWidget(self.btn21, 2, 1)
        self.btn22 = QtWidgets.QPushButton(self)
        self.btn22.setText("22")
        self.btn22.clicked.connect(lambda: self.onPlaceBtnPressed(2, 2))
        self.grid.addWidget(self.btn22, 1, 1)
        self.btn23 = QtWidgets.QPushButton(self)
        self.btn23.setText("23")
        self.btn23.clicked.connect(lambda: self.onPlaceBtnPressed(2, 3))
        self.grid.addWidget(self.btn23, 0, 1)
        self.btn31 = QtWidgets.QPushButton(self)
        self.btn31.setText("31")
        self.btn31.clicked.connect(lambda: self.onPlaceBtnPressed(3, 1))
        self.grid.addWidget(self.btn31, 2, 2)
        self.btn32 = QtWidgets.QPushButton(self)
        self.btn32.setText("32")
        self.btn32.clicked.connect(lambda: self.onPlaceBtnPressed(3, 2))
        self.grid.addWidget(self.btn32, 1, 2)
        self.btn33 = QtWidgets.QPushButton(self)
        self.btn33.setText("33")
        self.btn33.clicked.connect(lambda: self.onPlaceBtnPressed(3, 3))
        self.grid.addWidget(self.btn33, 0, 2)

        self.StatusLabel = QtWidgets.QLabel(self)
        self.StatusLabel.setText("狀態：\n")
        self.grid.addWidget(self.StatusLabel, 7, 0)

        self.GVsize = 600
        GSsize = self.GVsize
        self.PlaygroundGV = QtWidgets.QGraphicsView(self)
        self.PlaygroundGV.setGeometry(320, 0, self.GVsize, self.GVsize)
        self.PlaygroundGS = QtWidgets.QGraphicsScene()
        self.PlaygroundGS.setSceneRect(0, 0, GSsize, GSsize)
        self.PlaygroundGV.setScene(self.PlaygroundGS)

    def keyPressEvent(self, event):
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
        else:
            pass

    def disablePlaceBtn(self):
        for i in range(1, 4):
            for j in range(1, 4):
                btn = getattr(self, f"btn{i}{j}")
                btn.setEnabled(False)

    def enablePlaceBtn(self):
        for i in range(1, 4):
            for j in range(1, 4):
                btn = getattr(self, f"btn{i}{j}")
                btn.setEnabled(True)

    def onGameStartBtnPressed(self):
        print("onGameStartBtnPressed")

        self.pg.Reset()
        self.setNextGraphView()
        self.StatusLabel.setText(f"狀態\n下一位玩家是 {self.pg.next_player}")
        self.enablePlaceBtn()

    def onPlaceBtnPressed(self, x, y):
        print("onPlaceBtnPressed")

        print(f"{self.pg.next_player} place at ({x}, {y})\n")
        if self.pg.CheckPlaceable(x, y) is False:
            print(f"({x}, {y}) is not placeable\n")
            self.StatusLabel.setText(
                f"狀態\n下一位玩家是 {self.pg.next_player}\n無法落子"
            )
            return
        self.pg.Place(x, y)
        self.StatusLabel.setText(f"狀態\n下一位玩家是 {self.pg.next_player}")

        self.setNextGraphView()

        winner = self.pg.CheckWinner()
        if winner != "none":
            if winner == "draw":
                self.StatusLabel.setText("狀態\n平手")
            else:
                self.StatusLabel.setText(f"狀態\n{winner} 獲勝")
            self.disablePlaceBtn()
            return

    def setNextGraphView(self):
        next_fig = self.pg.RenderPlayground(self.pg.circle, self.pg.cross)
        self.PlaygroundCanvas = FigureCanvasQTAgg(next_fig)
        self.PlaygroundGS.clear()
        self.PlaygroundGS.addWidget(self.PlaygroundCanvas)
        self.PlaygroundGV.setGeometry(320, 0, self.GVsize, self.GVsize)
        self.PlaygroundGV.setScene(self.PlaygroundGS)
