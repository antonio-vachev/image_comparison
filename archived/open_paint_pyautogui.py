import subprocess
import pyautogui as pgui
import time


def locate_image_with_retries(image_path, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        location = pgui.locateCenterOnScreen(image_path, confidence=0.6)
        if location:
            return location
        time.sleep(1)
    return None


subprocess.Popen("mspaint.exe")
time.sleep(5)  # Adjust the delay as needed

file_button = locate_image_with_retries('resources/paint_buttons/file_button.png')
if file_button:
    print("File button found at:", file_button)
    # Click the button or perform other actions
    pgui.moveTo(file_button)
    pgui.leftClick(file_button)
else:
    print("File button not found")


