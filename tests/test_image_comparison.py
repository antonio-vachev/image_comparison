import subprocess
import time
import logging
import pyautogui
from PIL import Image, ImageChops
import pytest
import pyperclip
import os
from ..tests.overlay.overlay_images import overlay_images

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class TestImageComparison:

    # @pytest.mark.skip
    def test_get_screenshot_from_editor(self, app_path, original_image_path, screenshot_path):

        # Open the IMAGE_1.png with MS Paint desktop app
        editor_app = subprocess.Popen([app_path, original_image_path])
        logger.debug('Editor app successfully launched.')
        time.sleep(1)
        # Extend to full screen
        pyautogui.hotkey('f11')
        logger.debug('Full screen successfully engaged.')
        time.sleep(0.5)
        # Take a screenshot of the full screen app view
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        logger.debug('Screenshot successfully saved.')
        # Exit full screen mode
        pyautogui.hotkey('esc')
        # Close the Editor App
        editor_app.kill()
        logger.debug('Editor app successfully closed.')
        # Check if the file exists in the directory
        assert os.path.isfile(screenshot_path), f"Screenshot export has failed. '{screenshot_path}' was not found"

    # @pytest.mark.skip
    def test_screenshot_image_match_original(self, screenshot_path, original_image_path, current_build):

        img1 = Image.open(original_image_path)
        img2 = Image.open(screenshot_path)
        logger.debug('Images successfully loaded.')

        img1.resize(img2.size)
        logger.debug('Images successfully resized.')
        images = [img1, img2]

        for image in images:
            image.convert('RGB')
        logger.debug('Images successfully converted to RGB.')

        difference = ImageChops.difference(img1, img2)
        difference_path = f'.\\{current_build}\\results\\difference_screenshot_to_original.png'

        if difference.getbbox():
            logger.debug('Significant differences are found between the two images.')
            difference.save(difference_path)
            logger.debug(f"Difference image saved at '{difference_path}'.")

        assert os.path.isfile(difference_path) == False, 'The provided images are NOT identical.'

    # @pytest.mark.skip
    def test_export_image_from_editor(self, app_path, original_image_path, image_editor_export_path):

        # Copy the REF_image screenshot path to the clipboard
        pyperclip.copy(image_editor_export_path)
        # Open the IMAGE_1.png with MS Paint desktop app
        editor_app = subprocess.Popen([app_path, original_image_path])
        logger.debug('Editor app successfully launched.')
        time.sleep(1)
        # Engage 'Save As' in the app
        pyautogui.hotkey('f12')
        logger.debug('Starting Save As process.')
        time.sleep(1)
        # Paste the path from the clipboard
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        # Press 'Save'
        pyautogui.hotkey('enter')
        time.sleep(1)
        # Press 'Yes' to .png warning from MS Paint
        pyautogui.hotkey('enter')
        logger.debug('Image successfully exported.')
        time.sleep(1)
        # Close MS Paint desktop app
        editor_app.kill()
        logger.debug('Editor App successfully closed.')

        assert os.path.isfile(image_editor_export_path), f"Export has failed. '{image_editor_export_path}' was not found"

    @pytest.mark.xfail(reason="This test is expected to fail due to Ray tracing settings.")
    def test_export_image_match_original(self, secondary_original_image_path, image_editor_export_path, current_build):
        img1_path = rf'.\{current_build}\resources\IMAGE_2.png'
        img2_path = rf'.\{current_build}\resources\REF_Image.jpeg'

        if os.path.isfile(img1_path) and os.path.isfile(img2_path):
            img1 = Image.open(rf'.\{current_build}\resources\IMAGE_2.png')
            img2 = Image.open(rf'.\{current_build}\resources\REF_Image.jpeg')
            logger.debug('Images successfully loaded.')

            img1 = img1.convert('RGB')
            img2 = img2.convert('RGB')
            logger.debug('Images are converted to RGB.')

            difference = ImageChops.difference(img1, img2)
            difference_path = rf'.\{current_build}\results\differences.png'

            if difference.getbbox():
                difference.save(difference_path)
                logger.debug('Differences are found.')
            else:
                logger.debug('Images are identical.')
        else:
            logger.debug('Images are missing or path inputs are wrong.')
            difference_path = None

        assert os.path.isfile(difference_path) == False, ("Significant differences are "
                                                                "found in both images.")

    def test_overlay_image_differences(self, current_build, secondary_original_image_path):

        difference_path = rf'.\{current_build}\results\differences.png'
        original_path = secondary_original_image_path
        output_path = rf'.\{current_build}\results\differences_overlay.png'
        if os.path.isfile(difference_path) and os.path.isfile(original_path):
            logger.debug('Images successfully loaded.')

        if os.path.isfile(difference_path):
            overlay_images(original_path, difference_path, output_path)
            logger.debug('Images successfully overlayed.')

        assert os.path.isfile(output_path), "Differences overlay processing has failed."

    def test_generate_report(self, current_build):

        current_report_path = r".\ImageComparisonReport.html"
        assert os.path.isfile(current_report_path), 'Report generation has failed.'
