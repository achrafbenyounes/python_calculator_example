from PySide2 import QtWidgets, QtCore, QtGui
from functools import partial

class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Super Calculator")
        self.setup_ui()
        self.setup_connections()
        self.setup_shortcuts_keyboard()

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
        self.btn_numbers = []

        for i in range(self.grid_layout.count()):
            widget = self.grid_layout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QPushButton):
                widget.setFixedSize(64, 64)
                if widget.text().isdigit():
                    self.btn_numbers.append(widget)

    # This function make a connection between the signal applied in a widget and its relative python function called
    def setup_connections(self):
        for btn_number in self.btn_numbers:
            # We use the function partial from functools module to pass parameter to a function
            btn_number.clicked.connect(partial(self.btnNumberPressed, btn_number.text()))
        self.btn_del.clicked.connect(self.cleanResult)
        self.btn_minus.clicked.connect(partial(self.btnOperationPressed, str(self.btn_minus.text())))
        self.btn_plus.clicked.connect(partial(self.btnOperationPressed, str(self.btn_plus.text())))
        self.btn_mult.clicked.connect(partial(self.btnOperationPressed, str(self.btn_mult.text())))
        self.btn_div.clicked.connect(partial(self.btnOperationPressed, str(self.btn_div.text())))
        self.btn_eq.clicked.connect(self.calculOperation)

    def btnNumberPressed(self, button):
        """function called when the user clicks in number (0-9) """

        """Get the default value text of the result line edit widget"""
        result = str(self.le_result.text())

        if result == '0':
            self.le_result.setText(button)
        else:
            self.le_result.setText(result + button)
    
    def cleanResult(self):
	    """Reset the text in result editline and operation editline widget"""

	    self.le_result.setText('0')
	    self.le_operation.setText('')
    
    def btnOperationPressed(self, operation):
        """	Function called when the user clicks on some operation key (+, -, /, *)"""
		# Get the line edit operation
        operationText = str(self.le_operation.text())
		# Get the text value of result edit line widget
        result = str(self.le_result.text())
		# Sum the current operation with the result text and add in the end the chosen operation 
        self.le_operation.setText(operationText + result + operation)
		# Rest lineEdit result
        self.le_result.setText('0')
    
    def calculOperation(self):
        """Calculate the final result when we click in the = sign"""
        # Get the text in the line edit result
        result = str(self.le_result.text())
        # Add the current value of line edit result to the value of line edit operation
        self.le_operation.setText(self.le_operation.text() + result)

        # Evaluate the result of the operation
        result_operation = eval(str(self.le_operation.text()))

        # Affect the final result to result line edit widget
        self.le_result.setText(str(result_operation))
    
    # Function to handle number shortcuts keyboard
    def setup_shortcuts_keyboard(self):
        for btn in range(10):
            # We call the function partial to pass argument to the function btnNumberPressed()
            QtWidgets.QShortcut(QtGui.QKeySequence(str(btn)), self, partial(self.btnNumberPressed, str(btn)))

        QtWidgets.QShortcut(QtGui.QKeySequence(self.btn_plus.text()), self, partial(self.btnOperationPressed, (self.btn_plus.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(self.btn_minus.text()), self, partial(self.btnOperationPressed, (self.btn_minus.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(self.btn_mult.text()), self, partial(self.btnOperationPressed, (self.btn_mult.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence('Enter'), self, self.calculOperation)
        # Add shortcut for closing the application by clicking in 'Esc' button
        QtWidgets.QShortcut(QtGui.QKeySequence('Esc'), self, self.close)

app = QtWidgets.QApplication([])
calculaor_window = Calculator()
calculaor_window.show()

app.exec_()