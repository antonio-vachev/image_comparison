
![Image](https://i.ibb.co/M8cz2YF/IMAGE-1.png)



# Image Comparison Testing / Skill Check

The following repository contains test cases based on PyTest used for verification of image similarities.



## Prerequisites

- Python => v3.10
- pip => v24.0
- Windows OS

## Environment Setup

1. **Setup a virtual environment**  

   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment**

   ```cmd
   .venv\Scripts\activate
   ```

3. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Generate new *build* number

The testing process uses a new "build" number mockup to create a unique test folder for each testing cycle. In order to generate a _new build number_, execute the generate_new_build.py script inside .\builds
This will add a unique "build" number to an existing .json file.

   ```bash
   python .\builds\generate_new_build.py
   ```

### Testing

To proceed with testing the newly generated "build", use the following commands:

   ```bash
   cd .\tests
   pytest
   ```
The initial setup process creates a unique testing folder for the "build" within .\tests, which contains resources and results. Two original test images are generated inside .\tests\\*{build_number}*\resources. A set of test cases are then performed as per the task requirements.

As a result, testing generates the following output:

- **differences.png** - visualizes the differences between the two images
- **differences_overlay.png** - visualizes the differences between the two images overlayed on top of each other. Original image is shown in greyscale while the different pixels are overlayed on top in red color to enhance visual identification by the user.
- **ImageComparisonReport.html** - report containing all test case results with info regarding the environment, test results and duration, filtering and log calls.

![Image](https://i.ibb.co/vV7D1tx/differences-overlay.png)
