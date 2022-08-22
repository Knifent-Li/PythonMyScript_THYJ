#! D:\FileRepository\PyScript\Thyj2_Startup\venv\Scripts\python.exe
# coding=UTF-8
import os
import time

import win32api
import win32con
import win32gui

USER1 = 'ptl222'
PASSWD1 = 'shenma123'
USER2 = 'ptl333'
PASSWD2 = 'shenma123'
USER3 = 'ptl008'
PASSWD3 = 'shenma123'
EXE_DIR = 'D:\\GamePlatform\\桃花源记2\\launch.exe'
Game = '桃花源记2'


# 模拟键盘输入字符串
def send_str(text, hwnd=None):
    fstr = [ord(c) for c in text]
    for item in fstr:
        win32api.PostMessage(hwnd, win32con.WM_CHAR, item, 0)


def doclick(cx, cy, hwnd=None):
    long_position = win32api.MAKELONG(cx, cy)  # 模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起


# 运行桃花源记2
def login(user, passwd, game):
    os.system(EXE_DIR)

    time.sleep(1.75)
    handle1 = win32gui.FindWindow('#32770', game)
    # print(handle1)
    # 点击'进入游戏'
    print('进入游戏')
    win32api.SendMessage(handle1, win32con.WM_LBUTTONDOWN, 0, (692 << 16 | 986))
    win32api.SendMessage(handle1, win32con.WM_LBUTTONUP, 0, (692 << 16 | 986))

    time.sleep(5.5)
    handle1 = win32gui.FindWindow('TL_THYJ2_WINDOW_CLS', game)
    # print(handle1)
    # 点击'选择服务器'
    print('选择服务器')
    win32api.PostMessage(handle1, win32con.WM_KEYDOWN, 0x0D, 0)
    # doclick(399, 555, handle1)
    # win32api.SendMessage(handle1, win32con.WM_LBUTTONDOWN, 0, (555 << 16 | 399))
    # win32api.SendMessage(handle1, win32con.WM_LBUTTONUP, 0, (555 << 16 | 399))

    time.sleep(1)
    # 点击'进入游戏'
    print('进入登录界面')
    win32api.PostMessage(handle1, win32con.WM_KEYDOWN, 0x0D, 0)
    # doclick(623, 557, handle1)
    # win32api.SendMessage(handle1, win32con.WM_LBUTTONDOWN, 0, (557 << 16 | 623))
    # win32api.SendMessage(handle1, win32con.WM_LBUTTONUP, 0, (557 << 16 | 623))

    time.sleep(1)
    # 输入用户名和密码
    print('正在输入用户名和密码')
    win32api.PostMessage(handle1, win32con.WM_KEYDOWN, 0x09, 0)
    win32api.PostMessage(handle1, win32con.WM_KEYUP, 0x09, 0)
    time.sleep(0.5)
    for _ in range(0, 13):
        win32api.SendMessage(handle1, win32con.WM_KEYDOWN, 0x25, 0)
        win32api.SendMessage(handle1, win32con.WM_KEYDOWN, 0x2E, 0)

    time.sleep(0.5)
    send_str(user, handle1)

    win32api.PostMessage(handle1, win32con.WM_KEYDOWN, 0x09, 0)
    win32api.PostMessage(handle1, win32con.WM_KEYUP, 0x09, 0)
    send_str(passwd, handle1)

    # 点击登录
    time.sleep(0.5)
    print('登录')
    win32api.PostMessage(handle1, win32con.WM_KEYDOWN, 0x0D, 0)

    time.sleep(2)
    win32api.PostMessage(handle1, win32con.WM_KEYDOWN, 0x0D, 0)


def main():
    login(USER1, PASSWD1, Game)
    time.sleep(2)
    login(USER2, PASSWD2, Game)
    time.sleep(2)
    login(USER3, PASSWD3, Game)


if __name__ == '__main__':
    main()
