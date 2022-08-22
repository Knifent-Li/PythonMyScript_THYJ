import win32gui
import win32con
import win32api
from win32clipboard import *
import cv2
import time
import os

# 需要用到pywin32的库
wds_name = '桃花源记2'  # 窗口名
handle = win32gui.FindWindow('TL_THYJ2_WINDOW_CLS', wds_name)
print(handle)


# 窗口句柄

win_1 = win32gui.GetWindowRect(handle)
print(win_1)
# # 启动客户端

# 点击'进入游戏'
# print('进入游戏')
# win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, 0, (692 << 16 | 986))
# win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, (692 << 16 | 986))
# win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, 0, ((692) << 16 | (986)))
# win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, ((692) << 16 | (986)))

