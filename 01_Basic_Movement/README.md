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
