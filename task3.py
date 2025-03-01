import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore

class CanvasWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []

    def add_circle(self):
        diameter = random.randint(10, 100)
        w = self.width()
        h = self.height()
        if w < diameter or h < diameter:
            return
        x = random.randint(0, w - diameter)
        y = random.randint(0, h - diameter)
        color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QPen(QtCore.Qt.black))
        for (x, y, diameter, color) in self.circles:
            painter.setBrush(QtGui.QBrush(color))
            painter.drawEllipse(x, y, diameter, diameter)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Случайные окружности")
        self.resize(400, 400)
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)
        self.pushButton = QtWidgets.QPushButton("Добавить окружность", self)
        layout.addWidget(self.pushButton)
        self.canvas = CanvasWidget(self)
        self.canvas.setMinimumSize(300, 300)
        layout.addWidget(self.canvas)
        self.pushButton.clicked.connect(self.canvas.add_circle)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()