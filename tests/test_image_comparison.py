import subprocess
import time
import logging
import pyautogui

import pretest_setup as setup
import pyperclip
import os

log = logging.getLogger()


class TestImageComparison:

    def test_screenshot_from_editor(self, app_path, original_image_path, screenshot_path):

        pyperclip.copy(screenshot_path)

        editor_app = subprocess.Popen([app_path, original_image_path])
        time.sleep(1)

        pyautogui.hotkey('f11')
