import json
import os
import shutil


def current_build():
    with open('../builds/builds.json', 'r') as file:
        data = json.load(file)
        latest_build = str(data['builds'][-1])

    return latest_build


def prepare_new_test_directory():
    latest_build = current_build()
    try:
        os.mkdir(rf'./{latest_build}/')
        os.mkdir(rf'./{latest_build}/resources/')
        os.mkdir(rf'./{latest_build}/results/')

    except FileExistsError:
        print(f"Folder '{latest_build}' already exists.")

    return f"Test directory '{latest_build}' has been created."


def generate_resources():
    img_1 = r'../task/IMAGE_1.png'
    img_2 = r'../task/IMAGE_2.png'
    files_to_copy = [img_1, img_2]
    destination_dir = rf'./{current_build()}/resources/'

    for file in files_to_copy:
        shutil.copy2(file, destination_dir)

    return f"Resources are created in '{destination_dir}'"
