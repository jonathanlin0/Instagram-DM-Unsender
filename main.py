from tkinter import Y
from pyautogui import *
import pyautogui
import keyboard
import win32api, win32con
from time import sleep
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#while True:
#    print(pyautogui.position())
#    print(pyautogui.pixel(pyautogui.position()[0] + 20, pyautogui.position()[1]))
#    sleep(0.3)
#    if keyboard.is_pressed("ctrl") == True:
#        print("ctrl")
#    if keyboard.is_pressed("alt") == True:
#        print("alt")

while True:
    
    if keyboard.is_pressed("alt") == True:
        break

    # upper boundary of messages: y = 278
    # the x value for messages: x = 1374
    # the y value for bottom of sent messages: y = 920
    # rgb color of grey msg bubble: (239, 239, 239)
    # distance between unsend 3 dot button and msg boundary: 91
    # width of unsend 3 dot button: 10
    # color of 3 dot button when selected: (164, 164, 164)
    # color of 3 dot button when deselected: (142, 142, 142)
    # distance between 3 dot and unsend button: y = 36
    # location of unsend button (954, 609)
    
    

    y_value = 920
    while y_value > 278:
        
        print(pyautogui.position())

        if keyboard.is_pressed("alt") == True:
            break

        while pyautogui.pixel(1374, y_value) != (239, 239, 239) and y_value > 278:
            y_value -= 2
        
        left_x_boundary = 1374
        if pyautogui.pixel(left_x_boundary, y_value) != (255,255,255):
            print(time.time())
        
            while True:
                left_x_boundary -= 3
                if pyautogui.pixel(left_x_boundary, y_value) == (255, 255, 255) and pyautogui.pixel(left_x_boundary - 10, y_value) != (239, 239, 239):
                    break
            #while pyautogui.pixel(left_x_boundary, y_value) != (255, 255, 255) and pyautogui.pixel(left_x_boundary - 10, y_value) != (239, 239, 239):
            #    left_x_boundary -= 1
            
            pyautogui.moveTo(left_x_boundary, y_value)

            for i in range(left_x_boundary - 101, left_x_boundary - 91):
                #pyautogui.moveTo(i, y_value)
                should_click = False
                if pyautogui.pixel(i, y_value - 1) == (142, 142, 142) or pyautogui.pixel(i, y_value - 1) == (164, 164, 164):
                    should_click = True
                if pyautogui.pixel(i, y_value) == (142, 142, 142) or pyautogui.pixel(i, y_value) == (164, 164, 164):
                    should_click = True
                if pyautogui.pixel(i, y_value + 1) == (142, 142, 142) or pyautogui.pixel(i, y_value + 1) == (164, 164, 164):
                    should_click = True
                if should_click == True:
                    click(i,y_value)
                    sleep(0.3)
                    click(left_x_boundary - 101, y_value - 36)
                    sleep(0.3)
                    click(954, 609)
                    if y_value + 20 <= 920:
                        y_value += 20
                    pyautogui.scroll(-20)
                    break
        
        y_value -= 3

    pyautogui.scroll(400)

    #print(left_x_boundary, y_value)
    #print(pyautogui.pixel(pyautogui.position()[0] + 20, pyautogui.position()[1]))

    #print(pyautogui.position())
    
    pause_time = 0.3
    start_time = time.time()
    while time.time() - start_time < pause_time:
        sleep(0.05)
        if keyboard.is_pressed("alt") == True:
            break