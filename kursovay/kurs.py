# Form implementation generated from reading ui file 'kurs.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(423, 238)
        Form.setMinimumSize(QtCore.QSize(423, 238))
        Form.setMaximumSize(QtCore.QSize(423, 238))
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(160, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 80, 241, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 451, 241))
        self.label.setStyleSheet("border-image: url(./картинки/df26c3111893819.600a2261192bf.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.layoutWidget.raise_()


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Enter"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\">Autorization</p></body></html>"))
        self.pushButton.setText(_translate("Form", "Enter"))
        self.label_4.setText(_translate("Form", "Login"))
        self.label_5.setText(_translate("Form", "Password"))

