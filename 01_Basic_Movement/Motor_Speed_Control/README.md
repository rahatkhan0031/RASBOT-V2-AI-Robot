# Individual Motor Speed Control Using JupyterLab

## Overview

This project provides an interactive interface for controlling the four DC motors of the Yahboom Raspbot V2, powered by a Raspberry Pi 5.

The interface uses Python and ipywidgets inside JupyterLab to adjust each motor's speed and direction independently.

## Features

- Independent speed control for four motors
- Adjustable speed range from -255 to +255
- Forward and reverse motor rotation
- Interactive JupyterLab sliders
- Stop button to set all motor speeds to zero

## Hardware

- Yahboom Raspbot V2
- Raspberry Pi 5
- Four DC motors
- Yahboom motor control board

## Software Requirements

- Python 3
- JupyterLab
- ipywidgets
- Yahboom Raspbot_Lib

## How to Use

1. Open JupyterLab on the Raspberry Pi 5.
2. Open the Python code in a notebook or compatible Jupyter environment.
3. Run the code to display the motor control interface.
4. Adjust the sliders to control the individual motors.
5. Press **STOP ALL MOTORS** to stop the robot.

## Safety

Test the controls with the robot's wheels lifted off the ground. Keep the hardware power switch accessible, and do not rely on the software stop button as an emergency stop.

## Motor Speed Reference

| Speed | Function |
|---|---|
| -255 | Maximum reverse speed |
| -100 | Reduced reverse speed |
| 0 | Stop |
| +100 | Reduced forward speed |
| +255 | Maximum forward speed |

The actual wheel movement depends on motor orientation and wiring.
