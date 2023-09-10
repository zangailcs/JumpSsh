
from PySide2 import QtGui, QtCore
from PySide2.QtWidgets import QDialog

from multi_term_dialog import MultiTermDialog
from ui.chooseNodeDia_ui import Ui_chooseNodeDialog


class ChooseNodeDialog(QDialog, Ui_chooseNodeDialog):
    """
    dia_type 1--创建 2--修改
    """

    def __init__(self, jump_ip, node_list, account_info):
        super(ChooseNodeDialog, self).__init__()
        self.setupUi(self)
        self.cancelBtn.clicked.connect(self.close)
        self.jump_ip = jump_ip
        self.node_list = node_list
        self.account_info = account_info
        self.acceptBtn.clicked.connect(self.accept_handle)
        self.init_node_list()
        self.multi_term_dia = None

    def open_dialog(self):
        self.show()

    def init_node_list(self):
        model = QtGui.QStandardItemModel(self)
        for node in self.node_list:
            item = QtGui.QStandardItem(node)
            item.setCheckable(True)
            item.setCheckState(QtCore.Qt.Unchecked)
            model.appendRow(item)
        self.nodeListView.setModel(model)

    def accept_handle(self):
        model = self.nodeListView.model()
        checked_node = []
        for row in range(model.rowCount()):
            if model.item(row).checkState() == QtCore.Qt.Checked:
                checked_node.append(model.item(row).text())
        self.multi_term_dia = MultiTermDialog(self.jump_ip, checked_node, self.account_info)
        self.multi_term_dia.show()

