
from PySide2 import QtGui, QtCore
from PySide2.QtWidgets import QDialog, QFileDialog

from term_window import global_configs
from ui.ftpWin_ui import Ui_ftpWin
from utils import get_jump_ssn


class FtpDialog(QDialog, Ui_ftpWin):
    def __init__(self, jump_ip, node_list, account_info):
        super(FtpDialog, self).__init__()
        self.setupUi(self)
        self.jump_ip = jump_ip
        self.node_list = node_list
        self.account_info = account_info
        self.upFileChooseBtn.clicked.connect(self.choose_local_files)
        self.upClearBtn.clicked.connect(self.clear_local_files)

        self.downSaveRootChooseBtn.clicked.connect(self.choose_local_save_root)

        self.upBtn.clicked.connect(self.up_files_handler)
        self.downloadBtn.clicked.connect(self.download_files_handler)

        self.upRemotePathEdit.setText(global_configs['ftp']['default_remote_path'])
        self.downRemotePathEdit.setText(global_configs['ftp']['default_remote_path'])

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

    def choose_local_files(self):
        file_dia = QFileDialog()
        file_dia.setFileMode(QFileDialog.ExistingFiles)
        if file_dia.exec_():
            self.upLocalFileListWidget.addItems(file_dia.selectedFiles())
        # remote_ssn = get_jump_ssn(self.jump_ip, self.account_info['username'], self.account_info['pwd'])
        # ftp_client = remote_ssn.get_sftp_client()
        # ftp_client.put()

    def choose_local_save_root(self):
        save_root = QFileDialog().getExistingDirectory(self, "选择文件夹路径")
        self.downLocalRootEdit.setText(str(save_root))

    def clear_local_files(self):
        self.upLocalFileListWidget.clear()

    def up_files_handler(self):
        item_cnt = self.upLocalFileListWidget.count()
        local_filepaths = []
        for i in range(item_cnt):
            local_filepaths.append(self.upLocalFileListWidget.item(i).text())
        pass

    def download_files_handler(self):
        pass

