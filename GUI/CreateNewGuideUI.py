# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/CreateNewGuide.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 308)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 270, 381, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.lblGuideTitle = QtWidgets.QLabel(Dialog)
        self.lblGuideTitle.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.lblGuideTitle.setObjectName("lblGuideTitle")
        self.txtBoxGuideTitle = QtWidgets.QLineEdit(Dialog)
        self.txtBoxGuideTitle.setGeometry(QtCore.QRect(52, 10, 151, 20))
        self.txtBoxGuideTitle.setObjectName("txtBoxGuideTitle")
        self.lblGuideText = QtWidgets.QLabel(Dialog)
        self.lblGuideText.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.lblGuideText.setObjectName("lblGuideText")
        self.txtAreaGuideText = QtWidgets.QTextEdit(Dialog)
        self.txtAreaGuideText.setGeometry(QtCore.QRect(10, 60, 381, 161))
        self.txtAreaGuideText.setObjectName("txtAreaGuideText")
        self.btnChooseAvatar = QtWidgets.QPushButton(Dialog)
        self.btnChooseAvatar.setGeometry(QtCore.QRect(10, 240, 381, 23))
        self.btnChooseAvatar.setObjectName("btnChooseAvatar")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "0"))
        self.lblGuideTitle.setText(_translate("Dialog", "Title"))
        self.lblGuideText.setText(_translate("Dialog", "Text"))
        self.btnChooseAvatar.setText(_translate("Dialog", "Choose avatar"))

