from PySide2 import QtWidgets

app = QtWidgets.QApplication([])
fenetre = QtWidgets.QWidget()
fenetre.setWindowTitle('PySide Application')
widh = high = 500
fenetre.resize(widh, high)


fenetre.show()
app.exec_()
