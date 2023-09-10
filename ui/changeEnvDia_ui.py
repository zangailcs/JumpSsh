# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changeEnvDia.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_changeEnvDia(object):
    def setupUi(self, changeEnvDia):
        if not changeEnvDia.objectName():
            changeEnvDia.setObjectName(u"changeEnvDia")
        changeEnvDia.resize(360, 186)
        self.acceptBtn = QPushButton(changeEnvDia)
        self.acceptBtn.setObjectName(u"acceptBtn")
        self.acceptBtn.setGeometry(QRect(100, 130, 75, 23))
        self.cancelBtn = QPushButton(changeEnvDia)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(200, 130, 75, 23))
        self.layoutWidget = QWidget(changeEnvDia)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 21, 215, 96))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label1)

        self.jumpHostLineEdit = QLineEdit(self.layoutWidget)
        self.jumpHostLineEdit.setObjectName(u"jumpHostLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.jumpHostLineEdit)

        self.label1_2 = QLabel(self.layoutWidget)
        self.label1_2.setObjectName(u"label1_2")
        self.label1_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label1_2)

        self.sopuserPwdLineEdit = QLineEdit(self.layoutWidget)
        self.sopuserPwdLineEdit.setObjectName(u"sopuserPwdLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sopuserPwdLineEdit)

        self.label1_3 = QLabel(self.layoutWidget)
        self.label1_3.setObjectName(u"label1_3")
        self.label1_3.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label1_3)

        self.rootPwdLineEdit = QLineEdit(self.layoutWidget)
        self.rootPwdLineEdit.setObjectName(u"rootPwdLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.rootPwdLineEdit)

        self.label1_4 = QLabel(self.layoutWidget)
        self.label1_4.setObjectName(u"label1_4")
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setPointSize(12)
        self.label1_4.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label1_4)

        self.aliasLineEdit = QLineEdit(self.layoutWidget)
        self.aliasLineEdit.setObjectName(u"aliasLineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.aliasLineEdit)


        self.retranslateUi(changeEnvDia)

        QMetaObject.connectSlotsByName(changeEnvDia)
    # setupUi

    def retranslateUi(self, changeEnvDia):
        changeEnvDia.setWindowTitle(QCoreApplication.translate("changeEnvDia", u"\u6dfb\u52a0\u73af\u5883", None))
        self.acceptBtn.setText(QCoreApplication.translate("changeEnvDia", u"\u786e\u5b9a", None))
        self.cancelBtn.setText(QCoreApplication.translate("changeEnvDia", u"\u53d6\u6d88", None))
        self.label1.setText(QCoreApplication.translate("changeEnvDia", u"\u7ba1\u7406\u9762ip*:", None))
        self.label1_2.setText(QCoreApplication.translate("changeEnvDia", u"sopuser\u5bc6\u7801*:", None))
        self.sopuserPwdLineEdit.setPlaceholderText(QCoreApplication.translate("changeEnvDia", u"Changeme_123", None))
        self.label1_3.setText(QCoreApplication.translate("changeEnvDia", u"root\u5bc6\u7801*:", None))
        self.rootPwdLineEdit.setPlaceholderText(QCoreApplication.translate("changeEnvDia", u"Changeme_123", None))
        self.label1_4.setText(QCoreApplication.translate("changeEnvDia", u"\u73af\u5883\u540d\u79f0:", None))
        self.aliasLineEdit.setText("")
    # retranslateUi

