from PySide2.QtCore import QRect
from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QDialog

from term_window import EmbeddedTerminal, global_configs
from ui.multiTermWin_ui import Ui_multiTermWin
from utils import split_str


class MultiTermDialog(QDialog, Ui_multiTermWin):
    """
    dia_type 1--创建 2--修改
    """

    def __init__(self, jump_ip, node_list, account_info):
        super(MultiTermDialog, self).__init__()
        self.setupUi(self)
        self.jump_ip = jump_ip
        self.node_list = node_list
        self.account_info = account_info
        self.pos_list = [
            QRect(0, 40, 650, 350),
            QRect(650, 40, 650, 350),
            QRect(0, 400, 650, 350),
            QRect(650, 400, 650, 350)
        ]
        self.term_refs = [self.termWidget1, self.termWidget2, self.termWidget3, self.termWidget4]
        for i in range(4):
            self.term_refs[i].setGeometry(self.pos_list[i])
        self.term_list = []
        self.init_terms()
        self.send2allBox.stateChanged.connect(self.send2all_change_handler)

    def open_dialog(self):
        self.show()

    def init_terms(self):
        self.term_list = []
        username, pwd, su_pwd = self.account_info['username'], self.account_info['pwd'], self.account_info['suPwd']
        write_all = self.send2allBox.isChecked()
        for i in range(len(self.node_list)):
            node = self.node_list[i]
            term = EmbeddedTerminal(self.term_refs[i], self.jump_ip, node.split(split_str)[-1], username, pwd, su_pwd,
                                    global_configs['pty_base'], width=640, height=340)
            term.set_write_all(write_all)
            self.term_list.append(term)
        for i in range(len(self.term_list)):
            for j in range(len(self.term_list)):
                if i != j:
                    self.term_list[i].add_neighbor(self.term_list[j])

    def closeEvent(self, close_event):
        for term in self.term_list:
            term.closeEvent(event=QCloseEvent())

    def send2all_change_handler(self):
        write_all = self.send2allBox.isChecked()
        for term in self.term_list:
            term.set_write_all(write_all)
