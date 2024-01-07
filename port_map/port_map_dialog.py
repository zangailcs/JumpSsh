from PySide2 import QtGui, QtCore
from PySide2.QtWidgets import QDialog

from ui.portMapWin_ui import Ui_PortMapWin
from utils import get_checked_items, show_message, get_jump_ssn, split_str


class PortMapDialog(QDialog, Ui_PortMapWin):
    def __init__(self, jump_ip, node_list, account_info):
        super(PortMapDialog, self).__init__()
        self.setupUi(self)
        self.jump_ip = jump_ip
        self.node_list = node_list
        self.account_info = account_info

        self.pushButton.clicked.connect(self.submit_handler)

        self.init_node_list()

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

    def submit_handler(self):
        checked_node = get_checked_items(self.nodeListView)
        if len(checked_node) == 0:
            show_message(self, "提示", "请选择后台节点")
            return
        print('开始端口映射:', checked_node)
        uname, pwd = self.account_info['username'], self.account_info['pwd']
        jump_ssn = get_jump_ssn(self.jump_ip, uname, pwd)
        if jump_ssn is None or not jump_ssn.is_active():
            show_message(self, "提示", "获取连接失败")
            return

        failed_nodes = []
        for node in checked_node:
            target_node = node.split(split_str)[-1]
            result = jump_ssn.run_cmd('echo "%s" >> /root/port_map.txt' % target_node, username='root', raise_if_error=False)
            if result.exit_code != 0:
                failed_nodes.append(node)
        jump_ssn.close()
        if len(failed_nodes) == 0:
            show_message(self, "提示", "端口映射完成!")
        else:
            show_message(self, "警告", "失败节点列表：" + str(failed_nodes))

