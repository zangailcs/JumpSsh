# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ftpWin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ftpWin(object):
    def setupUi(self, ftpWin):
        if not ftpWin.objectName():
            ftpWin.setObjectName(u"ftpWin")
        ftpWin.resize(800, 600)
        self.nodeListView = QListView(ftpWin)
        self.nodeListView.setObjectName(u"nodeListView")
        self.nodeListView.setGeometry(QRect(20, 20, 350, 500))
        self.label_2 = QLabel(ftpWin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 30, 111, 16))
        self.label_3 = QLabel(ftpWin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 380, 111, 16))
        self.upBtn = QPushButton(ftpWin)
        self.upBtn.setObjectName(u"upBtn")
        self.upBtn.setGeometry(QRect(390, 310, 111, 23))
        self.layoutWidget = QWidget(ftpWin)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(390, 410, 391, 81))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.downLocalRootEdit = QLineEdit(self.layoutWidget)
        self.downLocalRootEdit.setObjectName(u"downLocalRootEdit")

        self.gridLayout_2.addWidget(self.downLocalRootEdit, 0, 1, 1, 1)

        self.downSaveRootChooseBtn = QPushButton(self.layoutWidget)
        self.downSaveRootChooseBtn.setObjectName(u"downSaveRootChooseBtn")

        self.gridLayout_2.addWidget(self.downSaveRootChooseBtn, 0, 2, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.downRemotePathEdit = QLineEdit(self.layoutWidget)
        self.downRemotePathEdit.setObjectName(u"downRemotePathEdit")

        self.gridLayout_2.addWidget(self.downRemotePathEdit, 1, 1, 1, 2)

        self.downloadBtn = QPushButton(ftpWin)
        self.downloadBtn.setObjectName(u"downloadBtn")
        self.downloadBtn.setGeometry(QRect(390, 500, 111, 23))
        self.layoutWidget1 = QWidget(ftpWin)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(390, 50, 391, 248))
        self.formLayout = QFormLayout(self.layoutWidget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.upFileChooseBtn = QPushButton(self.layoutWidget1)
        self.upFileChooseBtn.setObjectName(u"upFileChooseBtn")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.upFileChooseBtn)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.upRemotePathEdit = QLineEdit(self.layoutWidget1)
        self.upRemotePathEdit.setObjectName(u"upRemotePathEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.upRemotePathEdit)

        self.upLocalFileListWidget = QListWidget(self.layoutWidget1)
        self.upLocalFileListWidget.setObjectName(u"upLocalFileListWidget")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.upLocalFileListWidget)

        self.upClearBtn = QPushButton(ftpWin)
        self.upClearBtn.setObjectName(u"upClearBtn")
        self.upClearBtn.setGeometry(QRect(510, 310, 111, 23))

        self.retranslateUi(ftpWin)

        QMetaObject.connectSlotsByName(ftpWin)
    # setupUi

    def retranslateUi(self, ftpWin):
        ftpWin.setWindowTitle(QCoreApplication.translate("ftpWin", u"\u6587\u4ef6\u4f20\u8f93", None))
        self.label_2.setText(QCoreApplication.translate("ftpWin", u"--- \u4e0a\u4f20 ---", None))
        self.label_3.setText(QCoreApplication.translate("ftpWin", u"--- \u4e0b\u8f7d ---", None))
        self.upBtn.setText(QCoreApplication.translate("ftpWin", u"\u4e0a\u4f20\u5230\u9009\u5b9a\u670d\u52a1\u5668", None))
        self.label_5.setText(QCoreApplication.translate("ftpWin", u"\u672c\u5730\u76ee\u5f55:", None))
        self.downSaveRootChooseBtn.setText(QCoreApplication.translate("ftpWin", u"...", None))
        self.label_6.setText(QCoreApplication.translate("ftpWin", u"\u8fdc\u7aef\u8def\u5f84:", None))
        self.downloadBtn.setText(QCoreApplication.translate("ftpWin", u"\u4e0b\u8f7d\u5230\u672c\u5730", None))
        self.label.setText(QCoreApplication.translate("ftpWin", u"\u672c\u5730\u6587\u4ef6\u8def\u5f84:", None))
        self.upFileChooseBtn.setText(QCoreApplication.translate("ftpWin", u"...", None))
        self.label_4.setText(QCoreApplication.translate("ftpWin", u"\u8fdc\u7aef\u8def\u5f84:", None))
        self.upClearBtn.setText(QCoreApplication.translate("ftpWin", u"\u6e05\u7a7a\u6240\u9009\u6587\u4ef6", None))
    # retranslateUi

