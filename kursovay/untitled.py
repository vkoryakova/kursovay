# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Registerclien(object):
    def setupUi(self, Registerclien):
        Registerclien.setObjectName("Registerclien")
        Registerclien.resize(421, 488)
        Registerclien.setMinimumSize(QtCore.QSize(421, 488))
        Registerclien.setMaximumSize(QtCore.QSize(421, 488))
        font = QtGui.QFont()
        font.setPointSize(12)
        Registerclien.setFont(font)
        Registerclien.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.label = QtWidgets.QLabel(parent=Registerclien)
        self.label.setGeometry(QtCore.QRect(30, 90, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Registerclien)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Registerclien)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(parent=Registerclien)
        self.label_6.setGeometry(QtCore.QRect(100, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(parent=Registerclien)
        self.pushButton.setGeometry(QtCore.QRect(170, 370, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Registerclien)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 420, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(parent=Registerclien)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 431, 491))
        self.label_7.setStyleSheet("border-image: url(./картинки/df26c3111893819.600a2261192bf.png);")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("df26c3111893819.600a2261192bf.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Registerclien)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 90, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Registerclien)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 130, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Registerclien)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 170, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=Registerclien)
        self.lineEdit_6.setGeometry(QtCore.QRect(110, 210, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_4 = QtWidgets.QLabel(parent=Registerclien)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(parent=Registerclien)
        self.dateEdit.setGeometry(QtCore.QRect(110, 260, 131, 31))
        self.dateEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox = QtWidgets.QComboBox(parent=Registerclien)
        self.comboBox.setGeometry(QtCore.QRect(110, 310, 131, 31))
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(parent=Registerclien)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(parent=Registerclien)
        self.label_8.setGeometry(QtCore.QRect(30, 310, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.label_4.raise_()
        self.dateEdit.raise_()
        self.comboBox.raise_()
        self.label_5.raise_()
        self.label_8.raise_()

        self.retranslateUi(Registerclien)
        QtCore.QMetaObject.connectSlotsByName(Registerclien)

    def retranslateUi(self, Registerclien):
        _translate = QtCore.QCoreApplication.translate
        Registerclien.setWindowTitle(_translate("Registerclien", "Registerclient"))
        self.label.setText(_translate("Registerclien", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">FIO</span></p></body></html>"))
        self.label_2.setText(_translate("Registerclien", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Phone</span></p></body></html>"))
        self.label_3.setText(_translate("Registerclien", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Email</span></p></body></html>"))
        self.label_6.setText(_translate("Registerclien", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Client Registration</span></p></body></html>"))
        self.pushButton.setText(_translate("Registerclien", "Save"))
        self.pushButton_2.setText(_translate("Registerclien", "Cancel"))
        self.label_4.setText(_translate("Registerclien", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">ID_PC</span></p></body></html>"))
        self.label_5.setText(_translate("Registerclien", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Date</span></p></body></html>"))
        self.label_8.setText(_translate("Registerclien", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Time</span></p></body></html>"))
