# RASBOT V2: Square Movement

A Python movement demonstration for the **Yahboom RASBOT V2** using a **Raspberry Pi 5** and four Mecanum wheels. The robot attempts a square path by moving forward, right, backward, and left **without intentionally rotating**.

## How it works

The script `square_movement.py` runs these movements in order:

1. **Forward** for 1.0 second
2. **Strafe right** for 1.2 seconds
3. **Backward** for 1.0 second
4. **Strafe left** for 1.2 seconds

The motors stop between steps, with a 1.0-second pause after each movement. The script also issues a stop command when it exits, including after a keyboard interrupt.

## Hardware

- Raspberry Pi 5
- Yahboom RASBOT V2 chassis and motor controller
- Four Mecanum wheels
- Suitable robot power supply

## Software requirements

- Python 3
- Yahboom's `McLumk_Wheel_Sports` motor driver available at `/home/pi/project_demo/lib`

The script expects these driver functions to exist: `move_forward`, `move_right`, `move_backward`, `move_left`, and `stop_robot`. Confirm their names against your installed library before running.

## Run

From the `Square_Movement` directory on the Raspberry Pi:

```bash
python3 square_movement.py
```

Run this script on the Raspberry Pi connected to the robot, not on GitHub.

## Default configuration

| Parameter | Default | Meaning |
| --- | --- | --- |
| `speed` | `100` | Motor speed command (expected range: 0–255) |
| `forward_duration` | `1.0` s | Forward and backward movement time |
| `strafe_duration` | `1.2` s | Right and left movement time |
| `pause` | `1.0` s | Stop interval after each movement |

Example call from the script:

```python
drive_square(speed=100, forward_duration=1.0, strafe_duration=1.2, pause=1.0)
```

## Movement sequence

```text
Start → Forward → Stop → Right → Stop → Backward → Stop → Left → Stop → Finish
```

The robot's orientation is intended to stay the same throughout the maneuver. The actual path may not be a perfect square: motor calibration, wheel slip, and surface friction affect travel distance, so the forward and lateral durations may need adjustment.

## Safety and limitations

- For the first test, lift the wheels clear of the ground and verify each direction.
- Then test on a flat, clear surface at a low speed, with the power switch accessible.
- Press **Ctrl+C** to interrupt the script. Its `finally` block sends a motor-stop command, but software cannot guarantee a stop if hardware communication fails.
- This is **time-based, open-loop control**, not position-controlled navigation. The script does not use wheel encoders, odometry, or obstacle detection.

## Future improvements

- Calibrate forward and sideways travel distances.
- Add encoder feedback or odometry for more accurate square trajectories.
- Add obstacle detection before and during each movement.

## Attribution

Movement functions rely on Yahboom's motor driver. See the parent repository for licensing and attribution details.
