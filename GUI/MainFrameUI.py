# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/MainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(769, 261)
        self.lblGuideTitle = QtWidgets.QLabel(Dialog)
        self.lblGuideTitle.setGeometry(QtCore.QRect(110, 10, 31, 21))
        self.lblGuideTitle.setObjectName("lblGuideTitle")
        self.lblRating = QtWidgets.QLabel(Dialog)
        self.lblRating.setGeometry(QtCore.QRect(10, 5, 41, 31))
        self.lblRating.setObjectName("lblRating")
        self.txtEditGuideText = QtWidgets.QTextEdit(Dialog)
        self.txtEditGuideText.setEnabled(True)
        self.txtEditGuideText.setGeometry(QtCore.QRect(10, 40, 291, 211))
        self.txtEditGuideText.setReadOnly(True)
        self.txtEditGuideText.setObjectName("txtEditGuideText")
        self.cbxGuides = QtWidgets.QComboBox(Dialog)
        self.cbxGuides.setGeometry(QtCore.QRect(140, 10, 161, 22))
        self.cbxGuides.setObjectName("cbxGuides")
        self.cbxRating = QtWidgets.QComboBox(Dialog)
        self.cbxRating.setGeometry(QtCore.QRect(420, 180, 51, 21))
        self.cbxRating.setObjectName("cbxRating")
        self.btnRateGuide = QtWidgets.QPushButton(Dialog)
        self.btnRateGuide.setGeometry(QtCore.QRect(320, 182, 91, 21))
        self.btnRateGuide.setObjectName("btnRateGuide")
        self.txtEditComments = QtWidgets.QTextEdit(Dialog)
        self.txtEditComments.setGeometry(QtCore.QRect(490, 40, 261, 181))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.txtEditComments.setFont(font)
        self.txtEditComments.setReadOnly(True)
        self.txtEditComments.setObjectName("txtEditComments")
        self.lblComments = QtWidgets.QLabel(Dialog)
        self.lblComments.setGeometry(QtCore.QRect(490, 10, 81, 16))
        self.lblComments.setObjectName("lblComments")
        self.btnAddComment = QtWidgets.QPushButton(Dialog)
        self.btnAddComment.setGeometry(QtCore.QRect(710, 230, 41, 23))
        self.btnAddComment.setObjectName("btnAddComment")
        self.leComment = QtWidgets.QLineEdit(Dialog)
        self.leComment.setGeometry(QtCore.QRect(490, 231, 211, 20))
        self.leComment.setObjectName("leComment")
        self.lblGuideRating = QtWidgets.QLabel(Dialog)
        self.lblGuideRating.setGeometry(QtCore.QRect(50, 10, 47, 21))
        self.lblGuideRating.setObjectName("lblGuideRating")
        self.btnEditGuide = QtWidgets.QPushButton(Dialog)
        self.btnEditGuide.setGeometry(QtCore.QRect(400, 230, 71, 23))
        self.btnEditGuide.setObjectName("btnEditGuide")
        self.btnCreateNewGuide = QtWidgets.QPushButton(Dialog)
        self.btnCreateNewGuide.setGeometry(QtCore.QRect(320, 230, 71, 23))
        self.btnCreateNewGuide.setObjectName("btnCreateNewGuide")
        self.lblGuideAvatar = QtWidgets.QLabel(Dialog)
        self.lblGuideAvatar.setGeometry(QtCore.QRect(330, 50, 131, 111))
        self.lblGuideAvatar.setObjectName("lblGuideAvatar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Best Guider v1.0"))
        self.lblGuideTitle.setText(_translate("Dialog", "Title"))
        self.lblRating.setText(_translate("Dialog", "Rating"))
        self.btnRateGuide.setText(_translate("Dialog", "Rate"))
        self.lblComments.setText(_translate("Dialog", "Comments"))
        self.btnAddComment.setText(_translate("Dialog", "Add"))
        self.lblGuideRating.setText(_translate("Dialog", "0"))
        self.btnEditGuide.setText(_translate("Dialog", "Edit Guide"))
        self.btnCreateNewGuide.setText(_translate("Dialog", "Add Guide"))
        self.lblGuideAvatar.setText(_translate("Dialog", "TextLabel"))

