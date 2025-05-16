# ColorDetection
# Color Detection using OpenCV and PIL

## Overview
This project focuses on detecting specific colors in digital images using OpenCV and the Python Imaging Library (PIL). By converting images from BGR (Blue-Green-Red) to HSV (Hue-Saturation-Value) colorspace, color detection becomes more efficient and precise.

## How It Works
1. **Image Conversion** – The input image is converted from BGR to HSV colorspace using OpenCV.
2. **Mask Creation** – The `inRange` function of OpenCV is used to generate a mask that highlights pixels of the desired color (white) while turning all others black.
3. **Bounding Box using PIL** – The generated mask is converted into a PIL object to create a bounding box around the detected color region.
4. **Object Identification** – The detected colored regions can be used for various applications such as object tracking and automation.

## Applications
- **Object Tracking** – Used in robotics and automation to track specific objects in real time.
- **Industrial Automation** – Helps in sorting and quality control processes in factories.
- **Image Processing** – Useful in filtering and segmentation of images for further analysis.


