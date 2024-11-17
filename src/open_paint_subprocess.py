import subprocess
import os
import pyautogui
import time
import pyperclip


expand_user = os.path.expanduser("~")
print(expand_user)
original_image = r'..\resources\source_images\IMAGE_1.png'
paint_image = r'C:\Users\user\Code\image_comparison\resources\source_images\REF_Image.png'

pyperclip.copy(paint_image)

# get the path of paint:
paint_path = os.path.splitdrive(os.path.expanduser("~"))[0] + r"\WINDOWS\system32\mspaint.exe"
# open the file with paint
print(original_image)
subprocess.Popen([paint_path, original_image])

time.sleep(3)

pyautogui.hotkey('f12')
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.hotkey('enter')
