# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_JumpSsh(object):
    def setupUi(self, JumpSsh):
        if not JumpSsh.objectName():
            JumpSsh.setObjectName(u"JumpSsh")
        JumpSsh.setEnabled(True)
        JumpSsh.resize(1366, 800)
        JumpSsh.setDocumentMode(False)
        self.centralwidget = QWidget(JumpSsh)
        self.centralwidget.setObjectName(u"centralwidget")
        self.autoSudo = QCheckBox(self.centralwidget)
        self.autoSudo.setObjectName(u"autoSudo")
        self.autoSudo.setGeometry(QRect(830, 10, 71, 16))
        self.autoSudo.setChecked(True)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 30, 1341, 691))
        self.splitter.setOrientation(Qt.Horizontal)
        self.iMasterTable = QTreeWidget(self.splitter)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"\u73af\u5883\u5217\u8868");
        self.iMasterTable.setHeaderItem(__qtreewidgetitem)
        self.iMasterTable.setObjectName(u"iMasterTable")
        self.splitter.addWidget(self.iMasterTable)
        self.singleTermContainer = QTabWidget(self.splitter)
        self.singleTermContainer.setObjectName(u"singleTermContainer")
        self.singleTermContainer.setTabsClosable(True)
        self.term1 = QWidget()
        self.term1.setObjectName(u"term1")
        self.singleTermContainer.addTab(self.term1, "")
        self.term2 = QWidget()
        self.term2.setObjectName(u"term2")
        self.singleTermContainer.addTab(self.term2, "")
        self.splitter.addWidget(self.singleTermContainer)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(3, 0, 507, 25))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.addEnvBtn = QPushButton(self.widget)
        self.addEnvBtn.setObjectName(u"addEnvBtn")

        self.horizontalLayout.addWidget(self.addEnvBtn)

        self.updateEnvBtn = QPushButton(self.widget)
        self.updateEnvBtn.setObjectName(u"updateEnvBtn")

        self.horizontalLayout.addWidget(self.updateEnvBtn)

        self.updateBtn = QPushButton(self.widget)
        self.updateBtn.setObjectName(u"updateBtn")

        self.horizontalLayout.addWidget(self.updateBtn)

        self.openMultiTermBtn = QPushButton(self.widget)
        self.openMultiTermBtn.setObjectName(u"openMultiTermBtn")

        self.horizontalLayout.addWidget(self.openMultiTermBtn)

        self.deleteBtn = QPushButton(self.widget)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.horizontalLayout.addWidget(self.deleteBtn)

        self.enableTcpBtn = QPushButton(self.widget)
        self.enableTcpBtn.setObjectName(u"enableTcpBtn")
        self.enableTcpBtn.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.horizontalLayout.addWidget(self.enableTcpBtn)

        JumpSsh.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(JumpSsh)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1366, 22))
        JumpSsh.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(JumpSsh)
        self.statusbar.setObjectName(u"statusbar")
        JumpSsh.setStatusBar(self.statusbar)

        self.retranslateUi(JumpSsh)

        self.singleTermContainer.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(JumpSsh)
    # setupUi

    def retranslateUi(self, JumpSsh):
        JumpSsh.setWindowTitle(QCoreApplication.translate("JumpSsh", u"JumpSsh", None))
        self.autoSudo.setText(QCoreApplication.translate("JumpSsh", u"autoSudo", None))
        self.singleTermContainer.setTabText(self.singleTermContainer.indexOf(self.term1), QCoreApplication.translate("JumpSsh", u"term1", None))
        self.singleTermContainer.setTabText(self.singleTermContainer.indexOf(self.term2), QCoreApplication.translate("JumpSsh", u"term2", None))
        self.addEnvBtn.setText(QCoreApplication.translate("JumpSsh", u"\u6dfb\u52a0\u73af\u5883", None))
        self.updateEnvBtn.setText(QCoreApplication.translate("JumpSsh", u"\u66f4\u65b0\u73af\u5883\u4fe1\u606f", None))
        self.updateBtn.setText(QCoreApplication.translate("JumpSsh", u"\u66f4\u65b0\u8282\u70b9\u4fe1\u606f", None))
        self.openMultiTermBtn.setText(QCoreApplication.translate("JumpSsh", u"\u6253\u5f00\u5206\u5c4f\u7ec8\u7aef", None))
        self.deleteBtn.setText(QCoreApplication.translate("JumpSsh", u"\u5220\u9664\u6240\u9009\u73af\u5883", None))
        self.enableTcpBtn.setText(QCoreApplication.translate("JumpSsh", u"\u4f7f\u80fd\u7aef\u53e3\u8f6c\u53d1", None))
    # retranslateUi

