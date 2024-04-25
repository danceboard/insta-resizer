# Insta-Resizer

Insta-Resizer is a simple tool to resize images to the 1080x1080 resolution required by Instagram. It is a simple Python script that uses the Python Imaging Library (PIL) to resize images. We use it to resize images in bulk for faster posting on Instagram.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To resize images, run the following command:

```bash
python resize.py
```

It will automatically resize all images in the 'input' folder and save the resized images in the 'output' folder.

Supported image extensions: .jpg, .jpeg, .png and .webp.