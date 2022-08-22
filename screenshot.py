import win32gui
import time
import pyautogui

handle = win32gui.FindWindow("TL_THYJ2_WINDOW_CLS", None)
win32gui.SetForegroundWindow(handle)
time.sleep(2)

im = pyautogui.screenshot()
im.save('./material.png')
