import pyautogui
import time

words = open("word.txt" , 'r',encoding='utf-8')
time.sleep(1)

for word in words:
    pyautogui.typewrite(words)
    pyautogui.press('enter')
    time.sleep(1)
