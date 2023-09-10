import json
import os
import os.path as osp
import time

import yaml
from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QMessageBox, QTreeWidgetItem, QTabWidget

all_accounts = {}
all_opened_term = {}
split_str = '@#'
cache_dir = 'envs'


def show_message(parent_widget, title, message):
    QMessageBox.information(parent_widget, title, message, QMessageBox.Yes)


def get_term_id():
    return str(int(time.time_ns()))


def get_alias(nce_info):
    if 'alias' in nce_info:
        return nce_info['alias']
    return nce_info['ip']


def init_tree_data(table_widget):
    table_widget.clear()
    for file_name in os.listdir(cache_dir):
        nce_info = json.load(open(osp.join(cache_dir, file_name), encoding='utf-8'))
        top = QTreeWidgetItem(table_widget, nce_info)
        top.setText(0, get_alias(nce_info) + split_str + nce_info['ip'])
        table_widget.addTopLevelItem(top)
        all_accounts[top.text(0)] = nce_info['account']
        if 'nodes' not in nce_info:
            continue
        for node_type in nce_info['nodes']:
            node_ips = nce_info['nodes'][node_type]
            child = QTreeWidgetItem(top, node_ips)
            child.setText(0, node_type)
            for node_name in node_ips:
                ip = node_ips[node_name]
                child1 = QTreeWidgetItem(child, ip)
                child1.setText(0, node_name + split_str + ip)


def close_term_tab(tab_widget: QTabWidget, index):
    term_key = tab_widget.widget(index).objectName()
    tab_widget.removeTab(index)
    all_opened_term[term_key].closeEvent(event=QCloseEvent())
    del all_opened_term[term_key]


def match_any_key(keys, line):
    for key in keys:
        if key in line:
            return True
    return False


def match_logined_prefix(data: str, uname):
    lines = data.split(os.linesep)
    for line in lines:
        if '[' + uname + '@' in line and '~]$' in line:
            return True
    return False


def load_global_configs():
    with open('configs.yaml', 'r', encoding='utf-8') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        print(config)
        return config

