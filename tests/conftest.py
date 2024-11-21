import pytest
import subprocess
import os
import shutil
import pyautogui
import time
import pyperclip
import logging
import json
import pytest_html
from pytest_metadata.plugin import metadata_key


@pytest.fixture(scope='class')
def current_build():
    with open('../builds/builds.json', 'r') as file:
        data = json.load(file)
        latest_build = str(data['builds'][-1])

    return latest_build


@pytest.fixture(autouse=True, scope='class')
def prepare_new_test_directory(current_build):
    try:
        os.mkdir(rf'./{current_build}/')
        os.mkdir(rf'./{current_build}/resources/')
        os.mkdir(rf'./{current_build}/results/')

    except FileExistsError:
        print(f"Folder '{current_build}' already exists.")

    time.sleep(1)
    return current_build


@pytest.fixture(autouse=True, scope='class')
def generate_resources(prepare_new_test_directory):
    folder = prepare_new_test_directory
    img_1 = r'../task/IMAGE_1.png'
    img_2 = r'../task/IMAGE_2.png'
    files_to_copy = [img_1, img_2]
    destination_dir = rf'../tests/{folder}/resources/'

    for file in files_to_copy:
        shutil.copy2(file, destination_dir)

    time.sleep(1)
    return f"Resources are created in '{destination_dir}'"


@pytest.fixture
def app_path():
    return os.path.splitdrive(os.path.expanduser("~"))[0] + r"\WINDOWS\system32\mspaint.exe"


@pytest.fixture
def original_image_path(current_build):
    return f'.\\{current_build}\\resources\\IMAGE_1.png'


@pytest.fixture
def secondary_original_image_path(current_build):
    return f'.\\{current_build}\\resources\\IMAGE_2.png'


@pytest.fixture
def image_editor_export_path(current_build):
    image_path = rf'~\Code\image_comparison\tests\{current_build}\resources\REF_Image.jpeg'
    expanded_image_path = os.path.expanduser(image_path)
    return expanded_image_path


@pytest.fixture
def screenshot_path(current_build):
    return f'.\\{current_build}\\resources\\REF_Image_screenshot.png'


def pytest_html_report_title(report):
    report.title = f"Test Automation report on class TestImageComparison."


def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "Antonio's Skill Check for Chaos"
