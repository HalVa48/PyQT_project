import sys
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow
from maindesign import Ui_MainWindow
from design_dop import Ui_DopWindow
from monotonicity_intervals import monotonicity_intervals
from domain import linear_domain
from OxOy import ox, oy


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.result)

    def result(self):
        self.res = Res()
        self.res.show()

    def run(self):
        self.graphicsView.clear()

        def get_function_points(expression, x_min, x_max, num_points):
            x = np.linspace(x_min, x_max, num_points)
            y = eval(expression)
            return x, y

        x_min = float(self.lineEdit.text().split(";")[0])
        x_max = float(self.lineEdit.text().split(";")[1])

        num_points = 1000

        x_points, y_points = get_function_points(str(self.lineEdit_2.text()), x_min, x_max, num_points)

        # Устанавливаем y_min и y_max так, чтобы соответствовать требованиям
        y_min = min(x_points)
        y_max = max(x_points)

        # Разбиваем гиперболу на две части
        y_points[y_points > y_max] = np.nan
        y_points[y_points < y_min] = np.nan

        self.graphicsView.plot(x_points, y_points, pen='r')

class Res(QMainWindow, Ui_DopWindow):
    def __init__(self):
        super().__init__()
        self.move(400, 200)
        self.setupUi(self)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())