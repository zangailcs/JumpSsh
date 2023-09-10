import json
import os.path as osp

from PySide2.QtWidgets import QDialog

from ui.changeEnvDia_ui import Ui_changeEnvDia
from utils import show_message, cache_dir


class ChangeEnvDialog(QDialog, Ui_changeEnvDia):
    """
    dia_type 1--创建 2--修改
    """

    def __init__(self, dia_type):
        super(ChangeEnvDialog, self).__init__()
        self.dia_type = dia_type
        self.setupUi(self)
        self.cancelBtn.clicked.connect(self.close)
        if self.dia_type == 1:
            self.setWindowTitle("添加环境")
        else:
            self.setWindowTitle("修改环境信息")
        self.acceptBtn.clicked.connect(self.accept_handle)

    def open_dialog(self, curr_host=""):
        if self.dia_type == 1:
            self.jumpHostLineEdit.setReadOnly(False)
        else:
            self.jumpHostLineEdit.setText(curr_host)
            self.jumpHostLineEdit.setReadOnly(True)
        self.show()

    def accept_handle(self):
        ip = self.jumpHostLineEdit.text()
        if not ip:
            show_message(self, "提示", "ip地址不能为空")
            return
        sopuser_pwd = self.sopuserPwdLineEdit.text()
        if not sopuser_pwd:
            show_message(self, "提示", "sopuser密码不能为空")
            return
        root_pwd = self.rootPwdLineEdit.text()
        if not root_pwd:
            show_message(self, "提示", "root密码不能为空")
            return
        alias = self.aliasLineEdit.text()
        env_info = {
          "ip": ip,
          "alias": alias,
          "account": {
            "username": "sopuser",
            "pwd": sopuser_pwd,
            "suPwd": root_pwd
          }
        }
        fout = open(osp.join(cache_dir, ip + '.json'), 'w', encoding='utf-8')
        json.dump(env_info, fout, indent=4)
        fout.close()
        self.close()
