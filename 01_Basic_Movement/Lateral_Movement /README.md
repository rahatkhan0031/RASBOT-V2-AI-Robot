
# RASBOT V2 - Lateral Movement Control

## Overview

This project demonstrates sideways movement
(strafing) of the Yahboom RASBOT V2 robot
using Raspberry Pi 5 and Python.

The robot uses four Mecanum wheels to move
left and right without intentionally changing
its heading.

## Features

- Move sideways to the right
- Move sideways to the left
- Adjustable PWM motor speed
- Configurable movement duration
- Automatic motor stop on program exit
- KeyboardInterrupt handling

## Hardware

- Raspberry Pi 5
- Yahboom RASBOT V2
- Four Mecanum wheels
- Yahboom motor controller

## Software

Python 3

Yahboom motor driver:
McLumk_Wheel_Sports.py

Expected library path:
/home/pi/project_demo/lib

## Configuration

| Parameter | Value |
|---|---|
| Speed | 100 (0-255) |
| Movement duration | 1.0 second |
| Pause | 1.0 second |
| Startup delay | 2.0 seconds |

## Running the Program

```bash
python3 left_right_strafing.py
```

## Movement Sequence

1. Wait for 2 seconds
2. Move sideways right for 1 second
3. Stop for 1 second
4. Move sideways left for 1 second
5. Stop all motors

## Safety

Test with the wheels lifted off the ground
before operating on the floor.

Use a clear, flat surface and keep the robot
away from obstacles.
