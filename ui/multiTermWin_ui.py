# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'multiTermWin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Ui_multiTermWin(object):
    def setupUi(self, multiTermWin):
        if not multiTermWin.objectName():
            multiTermWin.setObjectName(u"multiTermWin")
        multiTermWin.resize(1364, 843)
        self.termWidget4 = QWidget(multiTermWin)
        self.termWidget4.setObjectName(u"termWidget4")
        self.termWidget4.setGeometry(QRect(690, 400, 581, 401))
        self.termWidget2 = QWidget(multiTermWin)
        self.termWidget2.setObjectName(u"termWidget2")
        self.termWidget2.setGeometry(QRect(680, 50, 611, 321))
        self.termWidget1 = QWidget(multiTermWin)
        self.termWidget1.setObjectName(u"termWidget1")
        self.termWidget1.setGeometry(QRect(0, 60, 651, 331))
        self.termWidget3 = QWidget(multiTermWin)
        self.termWidget3.setObjectName(u"termWidget3")
        self.termWidget3.setGeometry(QRect(20, 410, 641, 391))
        self.send2allBox = QCheckBox(multiTermWin)
        self.send2allBox.setObjectName(u"send2allBox")
        self.send2allBox.setGeometry(QRect(1190, 10, 131, 21))

        self.retranslateUi(multiTermWin)

        QMetaObject.connectSlotsByName(multiTermWin)
    # setupUi

    def retranslateUi(self, multiTermWin):
        multiTermWin.setWindowTitle(QCoreApplication.translate("multiTermWin", u"\u5206\u5c4f\u7ec8\u7aef", None))
        self.send2allBox.setText(QCoreApplication.translate("multiTermWin", u"\u8f93\u5165\u5230\u6240\u6709\u4f1a\u8bdd", None))
    # retranslateUi

