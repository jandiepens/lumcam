# Lumcam: A Python Package for Creating and Analyzing Luminance Maps on a Raspberry Pi 5
## Introduction
The human visual system is remarkable. Through the process of eye adaptation, our eyes can cope with a wide range of lighting conditions in the real world. This allows us to navigate on a starlit night and clearly distinguish colors and details on a bright sunny day. The human visual system can adapt to lighting conditions spanning nearly 10 orders of magnitude. Within a single scene, it can function over a range of about five orders of magnitude simultaneously.

Camera manufacturers and photographers have long strived to capture the same level of detail that the human eye can perceive. Although the first color photograph was achieved as early as 1861 by James Maxwell and Thomas Sutton, and the electronic video camera tube was invented in the 1920s, capturing the full range of light that the eye can see at any level of adaptation remains a significant challenge.

High dynamic range (HDR) imaging refers to the capture, storage, and display of images that more accurately represent the wide range of real-world lighting levels. With the advent of low-cost HDR cameras and years of experience, HDR is finally ready to enter the field of lighting studies for a large group of researchers and students. HDR imagery enables the creation of luminance maps of scenes, which can be used for glare analysis or for validating computed luminance maps with the Radiance software package.

## Lumcam
Is a package written in Python to capture, analyse and display High Dynamic Range (HDR) images. The capture part of the package is specific written for the Raspberry Pi 5 and HQ camera device with fisheye lens. The analyse and display code can be used an other hardware and operating systems.

## Installation
setup a virtual environment on your Raspberry Pi with
`uv venv --system-site-packages` to ensure you can use picamera2 module