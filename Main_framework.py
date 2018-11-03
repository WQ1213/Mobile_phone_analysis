# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_framework.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(456, 329)
        self.dataBtn = QtWidgets.QPushButton(Form)
        self.dataBtn.setGeometry(QtCore.QRect(40, 260, 80, 30))
        self.dataBtn.setObjectName("dataBtn")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(240, 260, 80, 30))
        self.clearBtn.setObjectName("clearBtn")
        self.analysisBtn = QtWidgets.QPushButton(Form)
        self.analysisBtn.setGeometry(QtCore.QRect(140, 260, 80, 30))
        self.analysisBtn.setObjectName("analysisBtn")
        self.resultText = QtWidgets.QTextEdit(Form)
        self.resultText.setGeometry(QtCore.QRect(40, 90, 381, 151))
        self.resultText.setObjectName("resultText")
        self.mobileComboBox = QtWidgets.QComboBox(Form)
        self.mobileComboBox.setGeometry(QtCore.QRect(100, 30, 131, 31))
        self.mobileComboBox.setObjectName("mobileComboBox")
        self.mobileComboBox.addItem("")
        self.mobileComboBox.addItem("")
        self.mobileComboBox.addItem("")
        self.mobileComboBox.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 51, 31))
        self.label.setObjectName("label")
        self.clear2Btn = QtWidgets.QPushButton(Form)
        self.clear2Btn.setGeometry(QtCore.QRect(340, 260, 80, 30))
        self.clear2Btn.setObjectName("clear2Btn")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 391, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.clearBtn.clicked.connect(Form.clearResult)
        self.dataBtn.clicked.connect(Form.data)
        self.analysisBtn.clicked.connect(Form.data_analysis)
        self.clear2Btn.clicked.connect(Form.clearFile)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "手机评论分析by.Duanraudon"))
        self.dataBtn.setText(_translate("Form", "数据采集"))
        self.clearBtn.setText(_translate("Form", "清空文本"))
        self.analysisBtn.setText(_translate("Form", "数据分析"))
        self.mobileComboBox.setItemText(0, _translate("Form", "Vivo_x23"))
        self.mobileComboBox.setItemText(1, _translate("Form", "Huawei_p20"))
        self.mobileComboBox.setItemText(2, _translate("Form", "Oppo_r17"))
        self.mobileComboBox.setItemText(3, _translate("Form", "Iphone_xs_max"))
        self.label.setText(_translate("Form", "手机型号"))
        self.clear2Btn.setText(_translate("Form", "清空文件"))
        self.label_2.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">若需重新采集该手机型号的数据，请先清空文件。</p></body></html>"))

