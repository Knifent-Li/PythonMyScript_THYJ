#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/19 13:13
# @Author  : Lynn
# @Site    : 
# @File    : per_hour_XX.py
# @Software: PyCharm
# 注意：需要将飞行术放到快捷栏F7处方可正常使用


import schedule
import time
import win32gui
import win32api
import pyautogui
import numpy as np

Window_class = "TL_THYJ2_WINDOW_CLS"
RED_COR = 248
GREEN_COR = 252
BLUE_COR = 248

ini_arr = np.array([1176, 443, 1176, 461, 1176, 479, 1176, 497])
xx_area = ini_arr.reshape(4, 2)  # 读取最多四行npc名
lanling_point = [[755, 533], [877, 594], [865, 478], [988, 401], [1121, 437], [1151, 547], [1200, 643]]


def get_forge(wincls):
    # 获取句柄
    game_hwnd = win32gui.FindWindow(wincls, None)
    win32gui.SetForegroundWindow(game_hwnd)


def doclick(cx, cy, st):
    # 模拟点击
    pyautogui.click(cx, cy, 1)
    time.sleep(st)


def goto(cx, cy):
    open_map_wild()
    pyautogui.click(cx, cy, 1)
    open_map_wild()     # 开了地图要记得关
    time.sleep(4.5)


def open_map_city():
    # 打开地图
    win32api.keybd_event(118, 41, 0, 0)
    time.sleep(1.5)


def open_map_wild():
    win32api.keybd_event(9, 15, 0, 0)       # 使用键码0f对应tab键，0f转换成十进制15
    time.sleep(1.5)


def open_friend():
    doclick(1284, 809, 1)
    time.sleep(1)


def init():
    # 初始化到兰陵
    time.sleep(1)
    open_map_city()
    doclick(1263, 689, 3)     # 到洛阳
    doclick(1076, 728, 2)      # 到兰陵


def check_xx(cor_list, red_color, green_color, blue_color):
    # 通过这个方法来检测是否有可杀的xx
    # red,green,blue为列表，存储星星名和战斗图标关键rgb值
    stack = [bool, 0, 0]      # 一个列表，存储了判定值和符合条件的xx的坐标
    open_friend()
    for i in range(4):
        a = int(cor_list[i][0])
        b = int(cor_list[i][1])
        temp_xx = pyautogui.pixelMatchesColor(a, b, (red_color, green_color, blue_color))
        if temp_xx:
            battle_x = 1285
            battle_y = int(cor_list[i][1])
            battle_y += 1
            temp_battle = pyautogui.pixelMatchesColor(battle_x, battle_y, (56, 60, 64))
            if not temp_battle:
                stack[0] = True
                stack[1] = 1190
                stack[2] = battle_y
                return stack

    stack[0] = False
    stack[1] = None
    stack[2] = None
    open_friend()
    return stack


def check_battle():
    # 检查是否进入作战界面以及判断何时作战结束
    global xx_area
    global RED_COR, GREEN_COR, BLUE_COR
    time.sleep(1)
    while True:
        is_battle = pyautogui.pixelMatchesColor(653, 259, (248, 228, 96))
        if is_battle:
            continue
        else:
            break

    re_flag = check_xx(xx_area, RED_COR, GREEN_COR, BLUE_COR)
    if re_flag[0]:
        doclick(re_flag[1], re_flag[2], 1)  # 移动到xx位置
        print(re_flag[1], re_flag[2])
        while True:
            wait_section = pyautogui.pixelMatchesColor(889, 612, (0, 252, 248))  # 坐标为对话框进入战斗选项的坐标
            if wait_section:
                break
            time.sleep(0.5)
        doclick(889, 612, 1)  # 进入战斗
        open_friend()
    time.sleep(0.5)


def chose_route(list_point, check_area, r, g, b):
    goto(list_point[0], list_point[1])
    flag = check_xx(check_area, r, g, b)
    if flag[0]:
        doclick(flag[1], flag[2], 1)        # 移动到xx位置
        print(flag[1], flag[2])
        while True:
            start_time = time.perf_counter()
            wait_section = pyautogui.pixelMatchesColor(889, 612, (0, 252, 248))     # 坐标为对话框进入战斗选项的坐标
            if wait_section:
                break
            else:
                # 这是一个计时器，如果10s内没进入战斗界面，强制进入下一个xx的检查
                timer = time.perf_counter() - start_time
                limit = timer - 5
                if limit > 0:
                    break
            time.sleep(0.5)
        doclick(889, 612, 1)        # 进入战斗
        open_friend()
        check_battle()
    time.sleep(0.5)


def start():
    # 开始杀星
    global xx_area
    global lanling_point
    global RED_COR, GREEN_COR, BLUE_COR
    init()
    time.sleep(0.5)

    # 兰陵杀星
    for i in range(7):
        chose_route(lanling_point[i], xx_area, RED_COR, GREEN_COR, BLUE_COR)


def main():
    get_forge(Window_class)
    # schedule.every().hour.do(start)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

    schedule.every().hour.do(start())
    # while True:
        # time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新时间
        # print(time_now)
        # if time_now == '08:07:15':
        #     schedule.every().hour.do(start())
        #     schedule.run_pending()
        #     time.sleep(1)
        # print("not this  time")
        # schedule.run_pending()
        # time.sleep(1)

    start()               # 用于调试


if __name__ == '__main__':
    main()
