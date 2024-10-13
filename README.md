# Gesture-Controlled Light Display
---

This project uses the MediaPipe library to track the user's hand, detect the distance between two fingers (thumb and index), and control the number of LEDs on an Arduino board. The number of LEDs that light up is proportional to the distance between the fingers, with a maximum of five LEDs lighting when the fingers are farthest apart.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Components](#components)
4. [Hardware Setup](#hardware-setup)
5. [Software Setup](#software-setup)
6. [Usage](#usage)
7. [Future Improvements](#future-improvements)
---

## Overview

The project dynamically controls five LEDs connected to an Arduino board using hand gestures detected by a webcam. The distance between the thumb and index finger controls how many LEDs light up. As the distance increases, more LEDs turn on, with up to five LEDs turning on when the distance is maximized.

---

## Features

- **Hand Tracking:** Real-time hand tracking using MediaPipe and OpenCV.
- **Distance Measurement:** Calculates the distance between the user's thumb and index finger.
- **Arduino Integration:** Controls LEDs on the Arduino based on the detected finger distance.
- **Dynamic Light Control:** The number of LEDs that light up changes dynamically, depending on the finger distance.

---

## Components

### Hardware:

- Arduino board (with at least 5 digital pins)
- 5 LEDs
- Jumper wires
- 220Ω resistors (one per LED)
- Breadboard
- Webcam

### Software:

- Python 3.x
- [MediaPipe](https://pypi.org/project/mediapipe/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [NumPy](https://pypi.org/project/numpy/)
- [PySerial](https://pypi.org/project/pyserial/)
- Arduino IDE

---

## Hardware Setup

1. Connect 5 LEDs to the Arduino using the following pin configuration:
    - LED 1 → Pin 2
    - LED 2 → Pin 4
    - LED 3 → Pin 8
    - LED 4 → Pin 10
    - LED 5 → Pin 12
2. Use 220Ω resistors for each LED.
3. Ground the LEDs by connecting them to the Arduino GND pin.
4. Connect the Arduino board to your PC using a USB cable.

---

## Software Setup

### Step 1: Install Python Dependencies

Install the necessary Python libraries using the following command:

- mediapipe
- opencv-python
- numpy
- pyserial


### Step 2: Upload Arduino Code

Upload the provided [program](/Program.ino) file to your Arduino using the Arduino IDE.

---

## Usage

1. **Connect the Arduino**: Ensure the Arduino is connected to the PC via USB.
2. **Run the Python Script**: Execute [Runner.py](/Runner.py) to start the hand-tracking program.
3. **Select COM Port**: When prompted, enter the correct COM port for the Arduino.
4. **Watch the LEDs**: Move your thumb and index finger to control the number of LEDs that light up on the Arduino.

---

## Future Improvements

- **Gesture Recognition**: Add support for more gestures, such as full hand or multiple finger controls.
- **Automatic Calibration**: Implement a feature that calibrates the system to the user's hand size and distance from the camera.
- **Two-Handed Control**: Extend functionality to allow for the control of two independent sets of LEDs with two hands.


This project demonstrates how real-time hand tracking can be combined with Arduino to create interactive hardware projects. Feel free to build upon and customize it for different applications!
