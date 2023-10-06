import os
import os.path as osp

from PySide2 import QtGui, QtCore
from PySide2.QtWidgets import QDialog, QFileDialog

from term_window import global_configs
from ui.ftpWin_ui import Ui_ftpWin
from utils import get_jump_ssn, show_message, get_target_ssn, split_str, get_checked_items


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
        self.downRemoteFileChooseBtn.clicked.connect(self.download_remote_file_choose_handler)

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
        if len(local_filepaths) == 0:
            show_message(self, "提示", "请选择需要上传的文件")
            return
        checked_node = get_checked_items(self.nodeListView)
        if len(checked_node) == 0:
            show_message(self, "提示", "请选择后台节点")
            return
        print('start to upload files:', local_filepaths)
        uname, pwd = self.account_info['username'], self.account_info['pwd']
        jump_ssn = get_jump_ssn(self.jump_ip, uname, pwd)
        if jump_ssn is None or not jump_ssn.is_active():
            show_message(self, "提示", "获取连接失败")
            return
        remote_root = self.upRemotePathEdit.text()
        for node in checked_node:
            curr_ssn = get_target_ssn(jump_ssn, node.split(split_str)[-1], uname, pwd)
            for local_path in local_filepaths:
                curr_ssn.put(local_path, '/'.join([remote_root, osp.basename(local_path)]))
            curr_ssn.close()
        jump_ssn.close()
        show_message(self, "提示", "文件传输完成")

    def download_remote_file_choose_handler(self):
        checked_node = get_checked_items(self.nodeListView)
        if len(checked_node) == 0:
            show_message(self, "提示", "请选择后台节点")
            return
        sample_node = checked_node[0]
        uname, pwd = self.account_info['username'], self.account_info['pwd']
        jump_ssn = get_jump_ssn(self.jump_ip, uname, pwd)
        if jump_ssn is None or not jump_ssn.is_active():
            show_message(self, "提示", "获取连接失败")
            return
        curr_ssn = get_target_ssn(jump_ssn, sample_node.split(split_str)[-1], uname, pwd)
        sftp_client = curr_ssn.get_sftp_client()
        file_lists = sftp_client.listdir(self.downRemotePathEdit.text())
        model = QtGui.QStandardItemModel(self)
        for file in file_lists:
            item = QtGui.QStandardItem(file)
            item.setCheckable(True)
            item.setCheckState(QtCore.Qt.Unchecked)
            model.appendRow(item)
        self.downloadRemoteFileListView.setModel(model)

    def download_files_handler(self):
        remote_filepaths = get_checked_items(self.downloadRemoteFileListView)
        remote_filepaths = ['/'.join([self.downRemotePathEdit.text(), name]) for name in remote_filepaths]
        if len(remote_filepaths) == 0:
            show_message(self, "提示", "请选择需要下载的文件")
            return
        checked_node = get_checked_items(self.nodeListView)
        if len(checked_node) == 0:
            show_message(self, "提示", "请选择后台节点")
            return
        print('start to download files:', remote_filepaths)
        uname, pwd = self.account_info['username'], self.account_info['pwd']
        jump_ssn = get_jump_ssn(self.jump_ip, uname, pwd)
        if jump_ssn is None or not jump_ssn.is_active():
            show_message(self, "提示", "获取连接失败")
            return
        local_root = self.downLocalRootEdit.text()
        for node in checked_node:
            local_dir = osp.join(local_root, node)
            os.makedirs(local_dir, exist_ok=True)
            curr_ssn = get_target_ssn(jump_ssn, node.split(split_str)[-1], uname, pwd)
            for remote_path in remote_filepaths:
                curr_ssn.get(remote_path, osp.join(local_dir, osp.basename(remote_path)))
            curr_ssn.close()
        jump_ssn.close()
        show_message(self, "提示", "文件传输完成")

