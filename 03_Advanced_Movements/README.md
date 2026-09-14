# Advanced Movements

This folder contains Python scripts for advanced movement control of the Yahboom RASBOT V2 using Mecanum wheels.

## Included Script

### `mecanum_diagonal_test.py`

Tests diagonal movement in four directions:

- Diagonal left-front
- Diagonal right-back
- Diagonal right-front
- Diagonal left-back

The robot stops between each movement and safely stops when the program finishes or is interrupted.

## Requirements

- Raspberry Pi 5
- Yahboom RASBOT V2
- Python 3
- Yahboom Mecanum wheel driver library

## Driver Library

The script uses functions from:

```python
from McLumk_Wheel_Sports import *
