# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chooseNodeDia.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Ui_chooseNodeDialog(object):
    def setupUi(self, chooseNodeDialog):
        if not chooseNodeDialog.objectName():
            chooseNodeDialog.setObjectName(u"chooseNodeDialog")
        chooseNodeDialog.resize(400, 550)
        chooseNodeDialog.setStyleSheet(u"")
        self.nodeListView = QListView(chooseNodeDialog)
        self.nodeListView.setObjectName(u"nodeListView")
        self.nodeListView.setGeometry(QRect(20, 20, 360, 450))
        self.label = QLabel(chooseNodeDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 480, 111, 16))
        self.label.setStyleSheet(u"color: rgb(255, 0, 0)")
        self.widget = QWidget(chooseNodeDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 500, 158, 25))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.acceptBtn = QPushButton(self.widget)
        self.acceptBtn.setObjectName(u"acceptBtn")

        self.horizontalLayout.addWidget(self.acceptBtn)

        self.cancelBtn = QPushButton(self.widget)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.retranslateUi(chooseNodeDialog)

        QMetaObject.connectSlotsByName(chooseNodeDialog)
    # setupUi

    def retranslateUi(self, chooseNodeDialog):
        chooseNodeDialog.setWindowTitle(QCoreApplication.translate("chooseNodeDialog", u"\u9009\u62e9\u8282\u70b9", None))
        self.label.setText(QCoreApplication.translate("chooseNodeDialog", u"\u6700\u591a\u53ef\u9009\u56db\u4e2a\u8282\u70b9", None))
        self.acceptBtn.setText(QCoreApplication.translate("chooseNodeDialog", u"\u786e\u5b9a", None))
        self.cancelBtn.setText(QCoreApplication.translate("chooseNodeDialog", u"\u53d6\u6d88", None))
    # retranslateUi

