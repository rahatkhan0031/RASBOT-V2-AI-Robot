# RASBOT V2 | Interactive PWM Servo Control

Control two PWM servos on a **Yahboom RASBOT V2** using interactive sliders in **JupyterLab** on a **Raspberry Pi 5**. The interface also includes a button to return both servos to their configured default angles.

## Features

- Independent slider control for Servo 1 and Servo 2
- Angle adjustments in 1° increments
- A **Reset Servos** button to restore the default positions
- `continuous_update=False` to send updates after a slider is released, rather than on every intermediate drag position
- Hardware control through the `Raspbot_Lib` library

## Hardware and software

**Hardware**
- Yahboom RASBOT V2 with Raspberry Pi 5
- Two connected PWM servos (for example, a camera pan/tilt assembly)

**Software**
- Python 3
- JupyterLab or Jupyter Notebook
- `ipywidgets`
- `IPython`
- Yahboom `Raspbot_Lib` module, installed and accessible to the active Python environment

> The Yahboom hardware library is platform-specific. This notebook must be run on a compatible, connected Raspberry Pi, not on GitHub itself.

## Default servo settings

| Setting | Servo 1 | Servo 2 |
| --- | ---: | ---: |
| Initial angle | 90° | 25° |
| Slider minimum | 0° | 0° |
| Slider maximum | 180° | 110° |
| Slider step | 1° | 1° |

**Important:** These are *software limits from the example*, not guaranteed safe mechanical limits. Verify the permitted travel for your specific servos and mounting brackets before operating near either end of the range.

## Getting started

1. Connect the two servos to the correct channels on the Yahboom controller and power the robot according to its hardware instructions.
2. Confirm that `Raspbot_Lib` is available to the Python kernel used by JupyterLab.
3. If `ipywidgets` is missing, install it in the **same Python environment as the notebook kernel**:

   ```bash
   python3 -m pip install ipywidgets
   ```

   Use your existing virtual environment or your system's supported package-management method if direct `pip` installation is restricted.
4. Open `interactive_servo_control.ipynb` in JupyterLab.
5. Run the notebook cell that initializes `Raspbot()` and displays the controls.
6. Move one slider at a time to test the corresponding servo. Use **Reset Servos** to restore the configured defaults.

## How it works

The notebook initializes the controller:

```python
from Raspbot_Lib import Raspbot
bot = Raspbot()
```

The function below sends a requested angle to each servo:

```python
def control_pwm_servos(servo1_angle: int, servo2_angle: int) -> None:
    bot.Ctrl_Servo(1, servo1_angle)
    bot.Ctrl_Servo(2, servo2_angle)
```

Two `ipywidgets.IntSlider` controls select the target angles. `widgets.interactive_output()` connects the slider values to `control_pwm_servos()`, and a reset-button callback returns the slider values and the servo commands to 90° and 25°.

## Safety and operation

- Check each servo's actual permitted angles and the pan/tilt assembly's clearance before testing.
- Start with small movements around known-safe positions.
- Keep cables clear of moving parts and avoid forcing servos against mechanical stops.
- Do not control the same servos from multiple scripts simultaneously.
