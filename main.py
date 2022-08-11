from pyautogui import *
import pyautogui
import keyboard
import win32api, win32con
from time import sleep
import time
import random

# package used for image recognition:
# https://brokencode.io/how-to-easily-image-search-with-python/
from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import imagesearcharea

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def margin_gen(val):
    change = random.randint(-25, 25)
    val = val * 0.01 * (100 + change)
    return int(val)


while True:
    
    if keyboard.is_pressed("alt") == True:
        quit()

    # top left of msg box: 872, 262
    # bottom right of msg box: 1356, 924

    y_value = 920
    while y_value > 278:

        if keyboard.is_pressed("alt") == True:
            quit()

        #while pyautogui.pixel(1374, y_value) != (239, 239, 239) and y_value > 278:
        while pyautogui.pixel(1374, y_value) == (255, 255, 255) and y_value > 278:
            print("Checking y = " + str(y_value))
            y_value -= 3

        right_x_boundary = 1374
        sleep(0.3)
        if pyautogui.pixel(right_x_boundary, y_value) != (255,255,255):

            print("Message bubble detected at y = " + str(y_value))
                    
            
            pyautogui.moveTo(right_x_boundary, y_value)

            sleep(0.3)
            dot_pos = imagesearcharea("dots.JPG", 872, 262, 1356, 924)

            if dot_pos[0] != -1 and dot_pos[1] != -1:

                print("Triple dot detected at (" + str(dot_pos[0] + 872) + ", " + str(dot_pos[1] + 262) + ")")
                dot_pos = list(dot_pos)
                dot_pos[0] = dot_pos[0] + 872
                dot_pos[1] = dot_pos[1] + 262


                click(dot_pos[0], dot_pos[1])
                print("Triple button clicked")
                sleep(0.3)
                click(dot_pos[0], dot_pos[1] - 36)
                sleep(0.3)

                unsend_pos = imagesearcharea("unsend_button.png", 872, 262, 1356, 924)
                if unsend_pos[0] != -1 and unsend_pos[1] != -1:
                    print("Unsend button detected at (" + str(unsend_pos[0] + 872) + ", " + str(unsend_pos[1] + 262) + ")")
                    click(unsend_pos[0] + 872, unsend_pos[1] + 262)
                    print("Unsend button clicked")

                print("Unsent a DM")

                person_name = "NAME"
                f = open("log.txt", "a")
                f.write("\nDELETE MESSAGE {" + person_name + "} "+ str(time.time()))
                f.close()

                if y_value + 20 <= 920:
                    y_value += 20
                try:
                    pyautogui.scroll(-20)
                except:
                    hi = 1
            else:
                y_value -= 2
    
    pyautogui.scroll(margin_gen(-200))
    pyautogui.scroll(margin_gen(600))
    print("Scrolled up")
    pause_time = 0.3
    start_time = time.time()
    while time.time() - start_time < pause_time:
        sleep(0.05)
        if keyboard.is_pressed("alt") == True:
            quit()
            