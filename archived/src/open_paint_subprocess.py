import subprocess
import os
import pyautogui
import time
import pyperclip

# Set the path of original IMAGE_1.png
original_image_path = r'../../task/IMAGE_1.png'

# Set the path of script generated REF_Image.jpg
ref_image_path = rf'~\Code\image_comparison\resources\source_images\REF_Image.jpeg'
expanded_ref_image_path = os.path.expanduser(ref_image_path)

# Copy the image path to the clipboard
pyperclip.copy(expanded_ref_image_path)

# Get the path of MS Paint desktop app
paint_path = os.path.splitdrive(os.path.expanduser("~"))[0] + r"\WINDOWS\system32\mspaint.exe"

# Open the IMAGE_1.png with MS Paint desktop app
ms_paint = subprocess.Popen([paint_path, original_image_path])
time.sleep(2)

# Enter full screen in MS Paint desktop app
pyautogui.hotkey('f11')
time.sleep(2)

# Take a screenshot of the full screen app view
screenshot = pyautogui.screenshot()
screenshot.save(r'..\resources\source_images\REF_Image_screenshot.jpeg')

# Close the full screen view of the app
pyautogui.hotkey('esc')

# Engage 'Save As' in the app
pyautogui.hotkey('f12')
time.sleep(2)

# Paste the path from the clipboard
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# Press 'Save'
pyautogui.hotkey('enter')
time.sleep(2)

# Press 'Yes' to .png warning from MS Paint
pyautogui.hotkey('enter')
time.sleep(2)

# Close MS Paint desktop app
ms_paint.kill()

# Remove the saved REF_Image.jpg
# os.remove(expanded_ref_image_path)
