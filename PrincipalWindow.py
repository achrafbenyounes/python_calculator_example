from PySide2 import QtWidgets

class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Super Calculator")
        self.setup_ui()
        self.setup_connections()

    
    def setup_ui(self):
        self.le_operation = QtWidgets.QLineEdit()
        self.le_result = QtWidgets.QLineEdit('0')

        self.btn_0 = QtWidgets.QPushButton('0')
        self.btn_1 = QtWidgets.QPushButton('1')
        self.btn_2 = QtWidgets.QPushButton('2')
        self.btn_3 = QtWidgets.QPushButton('3')
        self.btn_4 = QtWidgets.QPushButton('4')
        self.btn_5 = QtWidgets.QPushButton('5')
        self.btn_6 = QtWidgets.QPushButton('6')
        self.btn_7 = QtWidgets.QPushButton('7')
        self.btn_8 = QtWidgets.QPushButton('8')
        self.btn_9 = QtWidgets.QPushButton('9')
        self.btn_point = QtWidgets.QPushButton('.')
        self.btn_plus = QtWidgets.QPushButton('+')
        self.btn_minus = QtWidgets.QPushButton('-')
        self.btn_mult = QtWidgets.QPushButton('x')
        self.btn_div = QtWidgets.QPushButton('/')
        self.btn_eq = QtWidgets.QPushButton('=')
        self.btn_del = QtWidgets.QPushButton('C')

        self.grid_layout = QtWidgets.QGridLayout(self)

        self.grid_layout.addWidget(self.le_operation, 0, 0, 1, 4)
        self.grid_layout.addWidget(self.le_result, 1, 0, 1, 4)
        self.grid_layout.addWidget(self.btn_del, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.btn_div, 2, 3, 1, 1)
        self.grid_layout.addWidget(self.btn_7, 3, 0, 1, 1)
        self.grid_layout.addWidget(self.btn_8, 3, 1, 1, 1)
        self.grid_layout.addWidget(self.btn_9, 3, 2, 1, 1)
        self.grid_layout.addWidget(self.btn_mult, 3, 3, 1, 1)
        self.grid_layout.addWidget(self.btn_4, 4, 0, 1, 1)
        self.grid_layout.addWidget(self.btn_5, 4, 1, 1, 1)
        self.grid_layout.addWidget(self.btn_6, 4, 2, 1, 1)
        self.grid_layout.addWidget(self.btn_minus, 4, 3, 1, 1)
        self.grid_layout.addWidget(self.btn_1, 5, 0, 1, 1)
        self.grid_layout.addWidget(self.btn_2, 5, 1, 1, 1)
        self.grid_layout.addWidget(self.btn_3, 5, 2, 1, 1)
        self.grid_layout.addWidget(self.btn_plus, 5, 3, 1, 1)
        self.grid_layout.addWidget(self.btn_0, 6, 1, 1, 1)
        self.grid_layout.addWidget(self.btn_point, 6, 2, 1, 1)
        self.grid_layout.addWidget(self.btn_eq, 6, 3, 1, 1)

        for i in range(self.grid_layout.count()):
            widget = self.grid_layout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QPushButton):
                widget.setFixedSize(64, 64)
    

    def setup_connections(self):
        pass

app = QtWidgets.QApplication([])
calculaor_window = Calculator()
calculaor_window.show()

app.exec_()