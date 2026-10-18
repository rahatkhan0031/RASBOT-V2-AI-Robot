# RASBOT V2 Rotation Control

## Description
This Python program demonstrates left and right rotation movements of the Raspberry Pi 5-based RASBOT V2 robot using the Yahboom motor control library.

## Features
- Rotate the robot to the left.
- Rotate the robot to the right.
- Configure movement speed and duration.
- Stop the robot between movements.
- Handle keyboard interruption to stop the robot.

## Requirements
- Raspberry Pi 5
- Yahboom RASBOT V2 robot
- Compatible `McLumk_Wheel_Sports` Python library

## Usage

```bash
python3 rotate_left_right.py
```

## Configuration
- **Speed:** 100
- **Rotation duration:** 1.25 seconds
- **Pause between movements:** 1 second

## Note
The program must be tested with the correct Yahboom motor control library and hardware configuration.
