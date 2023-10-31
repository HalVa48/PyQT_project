import sys
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.graphicsView.clear()

        def get_function_points(expression, x_min, x_max, num_points):
            x = np.linspace(x_min, x_max, num_points)
            y = eval(expression)
            return x, y

        x_min = float(self.lineEdit_2.text().split(";")[0])
        x_max = float(self.lineEdit_2.text().split(";")[1])

        num_points = 1000

        x_points, y_points = get_function_points(str(self.lineEdit.text()), x_min, x_max, num_points)

        # Устанавливаем y_min и y_max так, чтобы соответствовать требованиям
        y_min = min(x_points)
        y_max = max(x_points)

        # Разбиваем гиперболу на две части
        y_points[y_points > y_max] = np.nan
        y_points[y_points < y_min] = np.nan

        self.graphicsView.plot(x_points, y_points, pen='r')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())