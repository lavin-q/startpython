import time
import random
import pyautogui
import pyperclip

txt = "高端人士的感慨是吗？"
time.sleep(3)
for _ in range(50):
    pyperclip.copy(txt)
    #pyautogui.typewrite(pyperclip.paste(), interval="0.15")
    pyautogui.hotkey("Ctrl", "V")
    #pyautogui.press('Enter')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(0.15)
