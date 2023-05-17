# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zzy\Desktop\界面设计\QCL-END\开始界面.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(487, 450)
        font = QtGui.QFont()
        font.setFamily("3DS Fonticon")
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("窗口图标.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(120, 340, 81, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 340, 81, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 20, 151, 121))
        self.label.setMaximumSize(QtCore.QSize(1677720, 1677))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap("窗口图标.png"))
        self.label.setScaledContents(True)
        self.label.setIndent(7)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 180, 401, 111))
        font = QtGui.QFont()
        font.setFamily("3DS Fonticon")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(100, 400, 271, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        self.radioButton_2.clicked.connect(Form.open_houchuli)
        self.radioButton.clicked.connect(Form.open_qianchuli)
        self.pushButton.clicked.connect(Form.chushi)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "海底管道多相流计算协同软件"))
        self.radioButton.setText(_translate("Form", "前处理"))
        self.radioButton_2.setText(_translate("Form", "后处理"))
        self.label_2.setText(_translate("Form", "<span style=\"color:#0000FF;\">海底管道多相流计算协同软件"))
#        self.label_2.setText(_translate("Form", "<html><head/><body><span style=\"font-size:10pt;font-weight:600;color:#ffffff;\">海底多相流计算协同软件V1.0</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "进入"))
        self.pushButton_2.setText(_translate("Form", "退出"))

