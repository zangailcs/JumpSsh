import json
import os.path as osp
from functools import partial

from PySide2.QtCore import QRect
from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QMainWindow, QPushButton

from change_env_dialog import ChangeEnvDialog
from choose_node_dialog import ChooseNodeDialog
from term_window import connect_curr_term
from ui.mainWin_ui import Ui_JumpSsh
from utils import init_tree_data, close_term_tab, split_str, show_message, all_opened_term, cache_dir, all_accounts


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_JumpSsh()
        self.ui.setupUi(self)
        self.ui.singleTermContainer.clear()
        self.ui.iMasterTable.clear()
        self.ui.iMasterTable.itemDoubleClicked.connect(lambda item: connect_curr_term(self.ui, item))
        init_tree_data(self.ui.iMasterTable)
        self.ui.singleTermContainer.tabCloseRequested.connect(lambda index:
                                                              close_term_tab(self.ui.singleTermContainer, index))
        self.ui.splitter.setStretchFactor(1, 1)
        self.add_dia = ChangeEnvDialog(1)
        self.ui.addEnvBtn.clicked.connect(self.add_env_handler)
        self.update_dia = ChangeEnvDialog(2)
        self.ui.updateEnvBtn.clicked.connect(self.update_env_handler)
        self.ui.deleteBtn.clicked.connect(self.delete_env_handler)
        self.ui.openMultiTermBtn.clicked.connect(self.open_choose_node_dia)
        self.choose_node_dia = None
        self.quick_input_map = {}
        self.all_quick_buttons = []
        self.init_buttons()

    def open_choose_node_dia(self):
        item = self.check_selected_env(self.ui.iMasterTable.selectedItems())
        if item is None:
            return
        all_node_list = []
        for index in range(item.childCount()):
            nodes_item = item.child(index)
            for node_idx in range(nodes_item.childCount()):
                all_node_list.append(nodes_item.child(node_idx).text(0))
        account = all_accounts.get(item.text(0))
        self.choose_node_dia = ChooseNodeDialog(item.text(0).split(split_str)[-1], all_node_list, account)
        self.choose_node_dia.open_dialog()

    def add_env_handler(self):
        self.add_dia.open_dialog()
        init_tree_data(self.ui.iMasterTable)

    def update_env_handler(self):
        item = self.check_selected_env(self.ui.iMasterTable.selectedItems())
        if item is None:
            return
        self.update_dia.open_dialog(item.text(0).split(split_str)[-1])

    def delete_env_handler(self):
        item = self.check_selected_env(self.ui.iMasterTable.selectedItems())
        if item is None:
            return
        self.ui.iMasterTable.takeTopLevelItem(self.ui.iMasterTable.indexOfTopLevelItem(item))
        #
        cache_path = osp.join(cache_dir, item.text(0).split(split_str)[-1] + '.json')
        print(cache_path)
        # os.remove(cache_path)

    def check_selected_env(self, items):
        if len(items) != 1:
            show_message(self, "提示", "请选择单个环境信息！")
            return None
        item = items[0]
        if item.parent():
            show_message(self, "提示", "请选择环境根节点")
            return None
        return item

    def closeEvent(self, event):
        for key in all_opened_term:
            all_opened_term[key].closeEvent(event=QCloseEvent())

    def init_buttons(self):
        quick_inputs = json.load(open('quickInputs.json', encoding='utf-8'))
        left, top = 10, 720
        width, height = 90, 30
        for quick_input in quick_inputs:
            btn = QPushButton(self.ui.centralwidget)
            btn.setText(quick_input['name'])
            btn.setGeometry(QRect(left, top, width, height))
            left += 100
            if left > self.width():
                left = 0
                top += 35
            self.quick_input_map[quick_input['name']] = quick_input['content']
            btn.clicked.connect(partial(self.quick_input_btn_handler, btn.text()))

    def quick_input_btn_handler(self, input_name):
        if self.ui.singleTermContainer.count() == 0:
            show_message(self, "提示", "当前未打开任何终端")
            return
        obj_name = self.ui.singleTermContainer.currentWidget().objectName()
        all_opened_term[obj_name].api.pure_write(self.quick_input_map[input_name])

