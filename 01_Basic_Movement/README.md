# Basic Movement

This folder contains Python scripts for basic movement control of the Yahboom RASBOT V2 using a Raspberry Pi.

## Included Script

### `forward_backward.py`
Controls the robot to:

- Move forward
- Stop
- Move backward
- Stop safely when the program ends or is interrupted

## Requirements

- Raspberry Pi
- Yahboom RASBOT V2
- Python 3
- Yahboom Mecanum wheel driver library

The script uses:

```python
from McLumk_Wheel_Sports import *

## Attribution

The low-level RASBOT V2 motor-control functions are provided by the Yahboom driver library.  
This repository contains my integration, testing, and application-level Python scripts built around the RASBOT V2 platform.
