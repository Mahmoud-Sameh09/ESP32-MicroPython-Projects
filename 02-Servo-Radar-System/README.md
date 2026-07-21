# Servo Radar System

## Overview
The Servo Radar System is an ESP32-based project developed with MicroPython that simulates the behavior of a radar. An HC-SR04 ultrasonic sensor is mounted on an SG90 servo motor, allowing it to scan the surrounding area from 0° to 180° and back.

When an object is detected within a predefined distance, the system stops scanning, activates a visual and audio alarm using an LED and a buzzer, and resumes scanning once the object is removed.

---

## Features

- 180° servo scanning
- Real-time distance measurement
- Object detection using the HC-SR04 ultrasonic sensor
- LED and buzzer warning system
- Automatic pause when an object is detected
- Automatic resume after the object is removed
- Clean and modular MicroPython code

---

## Components

- ESP32 DevKit V4
- HC-SR04 Ultrasonic Sensor
- SG90 Servo Motor
- LED
- Buzzer
- Jumper Wires

---

## How It Works

1. The servo rotates from **0° to 180°** while the ultrasonic sensor measures the distance.
2. After reaching **180°**, it rotates back to **0°**.
3. If an object is detected closer than **20 cm**, the scanning process pauses.
4. The LED and buzzer remain active until the object is removed.
5. The radar then continues scanning automatically.

---

## Future Improvements

- Real-time radar visualization on a PC using Python and Pygame.
- Display detected objects on a radar interface.
- Adjustable detection distance.
- Multiple alert levels based on object distance.

---

## Author

**Mahmoud Sameh**
