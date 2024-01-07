# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'portMapWin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PortMapWin(object):
    def setupUi(self, PortMapWin):
        if not PortMapWin.objectName():
            PortMapWin.setObjectName(u"PortMapWin")
        PortMapWin.resize(630, 613)
        self.nodeListView = QListView(PortMapWin)
        self.nodeListView.setObjectName(u"nodeListView")
        self.nodeListView.setGeometry(QRect(20, 20, 311, 500))
        self.pushButton = QPushButton(PortMapWin)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 500, 75, 23))

        self.retranslateUi(PortMapWin)

        QMetaObject.connectSlotsByName(PortMapWin)
    # setupUi

    def retranslateUi(self, PortMapWin):
        PortMapWin.setWindowTitle(QCoreApplication.translate("PortMapWin", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("PortMapWin", u"\u786e\u5b9a", None))
    # retranslateUi

