# JumpSsh
A GUI ssh tool to quickly connect private ip address through jump server, based on python, pyside2(pyqt5), xterm.js.
一个基于python, pyside2(pyqt5), xterm.js的图形界面的ssh工具，可以通过跳板机快速ssh连接内网ip。

## 特性:
- 快速ssh连接内网ip，基于以下命令行:（此命令并不需要本机与目标机互通，而是基于tcp端口转发）
```bash
ssh -J user1@jump_host user2@target_host
# user1、jump_host：跳板机用户名、ip地址
# user2、target_host：目标终端用户名、私网ip地址
```
- 自动输入连接密码
- 支持同时打开多个终端
- 撰写栏（快速输入按钮）
- 简单的分屏操作（同时输入命令到多终端）

## 示例图：
主页：
![image text](https://github.com/zangailcs/JumpSsh/blob/main/example_images/homePage.jpg "Home page")

分屏终端：
![image text](https://github.com/zangailcs/JumpSsh/blob/main/example_images/multiTermPage.jpg "Multi Term page")

## 如何使用：
方式一：运行源码
1. clone此仓库：
```commandline
git clone https://github.com/zangailcs/JumpSsh.git
```

2. pip安装必要的依赖
```commandline
pip install -r requirements.txt
```

3. 运行run.py
```commandline
python run.py
```

4. 创建示例虚拟机：可以参考本仓中附带的Vagrantfile，创建三个centos/7虚拟机，以尝试ssh功能

方式二：暂无