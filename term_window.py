import os
import os.path as osp
import threading

from PySide2 import QtCore, QtWidgets, QtWebEngineWidgets, QtWebChannel
from PySide2.QtWidgets import QTreeWidgetItem, QWidget
from winpty import PtyProcess

from ui.mainWin_ui import Ui_JumpSsh
from utils import match_any_key, load_global_configs, split_str, all_accounts, get_term_id, all_opened_term, \
    match_logined_prefix

global_configs = load_global_configs()

CONNECTING = 0
AUTO_SUDO = 1
RUNNING = 2


def connect_curr_term(ui: Ui_JumpSsh, item: QTreeWidgetItem):
    if item.childCount() != 0:
        print('Not leaf node: ' + item.text(0))
        open_new_term('本地终端', None, None, None, None, ui, None)
        return
    if not item.parent():
        return
    root_item = item.parent()
    while root_item.parent():
        root_item = root_item.parent()
    target_ip = item.text(0).split(split_str)[-1]
    jump_ip = root_item.text(0).split(split_str)[-1]
    if target_ip == jump_ip:
        return
    account = all_accounts.get(root_item.text(0))
    username, pwd, su_pwd = account['username'], account['pwd'], account['suPwd']
    open_new_term(item.text(0), jump_ip, pwd, su_pwd, target_ip, ui, username, ui.autoSudo.isChecked())


def open_new_term(item_name, jump_ip, pwd, su_pwd, target_ip, ui, username, auto_sudo=False):
    tab_new = QWidget()
    tab_new.setObjectName(get_term_id())
    tab_id = ui.singleTermContainer.count()
    ui.singleTermContainer.addTab(tab_new, item_name)
    ui.singleTermContainer.setCurrentIndex(tab_id)
    term = EmbeddedTerminal(tab_new, jump_ip, target_ip, username, pwd, su_pwd, global_configs['pty_base'], auto_su=auto_sudo)
    term.show()
    all_opened_term[tab_new.objectName()] = term
    return term


class TerminalAPI(QtCore.QObject):
    def __init__(self, term=None):
        super().__init__(term)
        self.term = term
        self.write_all = False
        self.neighbors = []

    input = QtCore.Signal(str)

    @QtCore.Slot(str)
    def write(self, text: str):
        # print("write:", repr(text))
        self.term.proc.write(text)
        if len(self.neighbors) > 0 and self.write_all:
            for neighbor in self.neighbors:
                neighbor.api.pure_write(text)

    @QtCore.Slot(str)
    def pure_write(self, text: str):
        self.term.proc.write(text)

    @QtCore.Slot(int, int)
    def resize(self, cols: int, rows: int):
        self.term.proc.setwinsize(rows, cols)

    def add_neighbor(self, term):
        self.neighbors.append(term)

    def set_write_all(self, write_all):
        self.write_all = write_all


class EmbeddedTerminal(QtWidgets.QWidget):
    def __init__(self, parent, jump_host, target_host, username, pwd, su_pwd,
                 embed_term='powershell', width=1100, height=680, auto_su=True):
        super().__init__(parent=parent)

        self.jump_host = jump_host
        self.target_host = target_host
        self.username = username
        self.pwd = pwd
        self.su_pwd = su_pwd
        self.auto_su = auto_su

        self.setWindowTitle("Embedded Terminal")
        self.setMinimumWidth(width)
        self.setMinimumHeight(height)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(QtCore.QMargins())

        self.webview = QtWebEngineWidgets.QWebEngineView(self)

        layout.addWidget(self.webview)

        self.channel = QtWebChannel.QWebChannel(self)
        self.webview.page().setWebChannel(self.channel)

        self.api = TerminalAPI(self)
        self.channel.registerObject("term", self.api)

        self.webview.load(QtCore.QUrl.fromLocalFile(osp.join(os.getcwd(), "index.html")))

        self.proc = PtyProcess.spawn([embed_term])
        self.read_thread = threading.Thread(target=self.read_thread_main)
        self.read_thread.start()
        self.state = CONNECTING
        if self.target_host:
            self.api.pure_write("ssh -J {}@{} {}@{}".format(username, jump_host, username, target_host) + os.linesep)
        else:
            self.state = RUNNING

    def closeEvent(self, event):
        self.api.pure_write("exit" + os.linesep)
        self.proc.close(force=True)
        self.read_thread.join()

    def read_thread_main(self):
        # TODO Something more robust to wait for the API to connect?
        try:
            while True:
                data = self.proc.read()
                # print('read data:', data, 'at state=', self.state)
                if self.state == RUNNING:
                    self.api.input.emit(data)
                elif self.state == AUTO_SUDO and match_any_key(global_configs['su_prompt'], data):
                    self.api.pure_write(self.su_pwd + os.linesep + "clear" + os.linesep)
                    self.state = RUNNING
                elif self.state == CONNECTING:
                    if match_any_key(global_configs['passwd_prompt'], data):
                        self.api.pure_write(self.pwd + os.linesep)
                    elif match_any_key(global_configs['first_ssh_prompt'], data):
                        self.api.pure_write("yes" + os.linesep)
                    elif match_logined_prefix(data, self.username):
                        if self.auto_su:
                            self.state = AUTO_SUDO
                            self.api.pure_write('su - root' + os.linesep)
                        else:
                            self.state = RUNNING
                            self.api.input.emit(data)

        except (EOFError, ConnectionAbortedError):
            pass

    def add_neighbor(self, term):
        self.api.add_neighbor(term)

    def set_write_all(self, write_all):
        self.api.set_write_all(write_all)

