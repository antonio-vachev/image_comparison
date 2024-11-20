import subprocess
import time
import logging
import pyautogui
from PIL import Image, ImageChops
import pytest
import pyperclip
import os
from overlay_images import process_and_overlay as overlay


log = logging.getLogger()


class TestImageComparison:

    @pytest.mark.skip
    def test_get_screenshot_from_editor(self, app_path, original_image_path, screenshot_path):

        # Open the IMAGE_1.png with MS Paint desktop app
        editor_app = subprocess.Popen([app_path, original_image_path])
        time.sleep(1)
        # Extend to full screen
        pyautogui.hotkey('f11')
        time.sleep(0.5)
        # Take a screenshot of the full screen app view
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        # Exit full screen mode
        pyautogui.hotkey('esc')
        # Close the Editor App
        editor_app.kill()
        # Check if the file exists in the directory
        assert os.path.isfile(screenshot_path), f"Screenshot export has failed. '{screenshot_path}' was not found"

    @pytest.mark.skip
    def test_screenshot_image_match_original(self, screenshot_path, original_image_path, current_build):

        img1 = Image.open(original_image_path)
        img2 = Image.open(screenshot_path)

        img1.resize(img2.size)
        images = [img1, img2]

        for image in images:
            image.convert('RGB')

        difference = ImageChops.difference(img1, img2)
        difference_path = f'.\\{current_build}\\results\\difference_screenshot_to_original.png'

        if difference.getbbox():
            difference.save(difference_path)
            difference.show()
            difference.close()

        assert os.path.isfile(difference_path) == False, 'The provided images are NOT identical.'

    @pytest.mark.skip
    def test_export_image_from_editor(self, app_path, original_image_path, image_editor_export_path):

        # Copy the REF_image screenshot path to the clipboard
        pyperclip.copy(image_editor_export_path)
        # Open the IMAGE_1.png with MS Paint desktop app
        editor_app = subprocess.Popen([app_path, original_image_path])
        time.sleep(1)
        # Engage 'Save As' in the app
        pyautogui.hotkey('f12')
        time.sleep(1)
        # Paste the path from the clipboard
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        # Press 'Save'
        pyautogui.hotkey('enter')
        time.sleep(1)
        # Press 'Yes' to .png warning from MS Paint
        pyautogui.hotkey('enter')
        time.sleep(1)
        # Close MS Paint desktop app
        editor_app.kill()

        assert os.path.isfile(image_editor_export_path), f"Export has failed. '{image_editor_export_path}' was not found"

    # @pytest.mark.xfail(reason="This test is expected to fail due to Ray tracing settings.")
    def test_export_image_match_original(self, secondary_original_image_path, image_editor_export_path, current_build):

        img1 = Image.open(secondary_original_image_path)
        img2 = Image.open(image_editor_export_path)

        # img1.resize(img2.size)
        images = [img1, img2]

        for image in images:
            image.convert('RGBA')

        difference = ImageChops.difference(img1, img2)
        difference_path = f'.\\{current_build}\\results\\difference_export_to_original.png'

        if difference.getbbox():
            difference.save(difference_path)
            difference.show()
            difference.close()
            overlay_image_path = f'.\\{current_build}\\results\\difference_export_to_original_overlay.png'
            overlay(secondary_original_image_path, image_editor_export_path, overlay_image_path)

        assert os.path.isfile(difference_path) == True, 'The provided images are identical.'

