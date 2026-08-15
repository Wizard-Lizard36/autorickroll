import sys
import os
import webbrowser
sys.path.insert(0, r"C:\Users\max\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages")
import keyboard
import time

#webbrowser.open("https://ha.mr/")
webbrowser.open("http:")

time.sleep(1)

keyboard.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ", delay=0.02)

keyboard.press_and_release("enter")

time.sleep(3)

keyboard.press_and_release("f")
