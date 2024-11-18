import subprocess
import os
import pyautogui
import time
import pyperclip


original_image_path = r'..\resources\source_images\IMAGE_1.png'
ref_image_path = rf'~\Code\image_comparison\resources\source_images\REF_Image.png'
expanded_ref_image_path = os.path.expanduser(ref_image_path)
print(expanded_ref_image_path)
# Copy the
pyperclip.copy(expanded_ref_image_path)

# get the path of MS Paint desktop app:
paint_path = os.path.splitdrive(os.path.expanduser("~"))[0] + r"\WINDOWS\system32\mspaint.exe"
# open the file with paint
ms_paint = subprocess.Popen([paint_path, original_image_path])
time.sleep(2)
pyautogui.hotkey('f12')
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.hotkey('enter')
time.sleep(2)
pyautogui.hotkey('enter')
time.sleep(2)
ms_paint.kill()
time.sleep(5)
os.remove(expanded_ref_image_path)
