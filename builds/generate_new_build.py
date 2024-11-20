import json
from datetime import datetime


def generate_new_build(json_file):
    with open(json_file, 'r+') as file:
        data = json.load(file)
        new_build = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        data['builds'].append(new_build)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
        return new_build


if __name__ == "__main__":
    build = generate_new_build('builds.json')
    print(f'New build has been generated: {build}')
