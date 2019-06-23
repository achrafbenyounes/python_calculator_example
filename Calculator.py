from PySide2 import QtWidgets

class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Principal Window")
        self.resize(500, 500)
        self.setup_ui()
        self.setup_connections()

    
    def setup_ui(self):
        self.layout = QtWidgets.QGridLayout(self)

        self.btn_0 = QtWidgets.QPushButton("0-0")

        self.btn_1 = QtWidgets.QPushButton('0.0')
        self.btn_2 = QtWidgets.QPushButton('0.1')
        self.btn_3 = QtWidgets.QPushButton('0.2')
        self.btn_4 = QtWidgets.QPushButton('1.0')
        self.btn_5 = QtWidgets.QPushButton('1.1')
        self.btn_6 = QtWidgets.QPushButton('1.2')
        self.btn_7 = QtWidgets.QPushButton('2.0')
        self.btn_8 = QtWidgets.QPushButton('2.1')
        self.btn_9 = QtWidgets.QPushButton('2.2')

        self.layout.addWidget(self.btn_0, 0, 0, 1, 3)
        self.layout.addWidget(self.btn_1, 1, 0, 1, 1)
        self.layout.addWidget(self.btn_2, 1, 1, 1, 1)
        self.layout.addWidget(self.btn_3, 1, 2, 1, 1)

    """
        self.layout.addWidget(self.btn_1, 0, 0)
        self.layout.addWidget(self.btn_2, 0, 1)
        self.layout.addWidget(self.btn_3, 0, 2)

        self.layout.addWidget(self.btn_4, 1, 0)
        self.layout.addWidget(self.btn_5, 1, 1)
        self.layout.addWidget(self.btn_6, 1, 2)

        self.layout.addWidget(self.btn_7, 2, 0)
        self.layout.addWidget(self.btn_8, 2, 1)
        self.layout.addWidget(self.btn_9, 2, 2)
    """

        


    
    def setup_connections(self):
        pass

app = QtWidgets.QApplication([])
fenetre = PrincipalWindow()
fenetre.show()

app.exec_()