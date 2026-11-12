import sys
import time

# Add Yahboom library path and import Mecanum driver
sys.path.append('/home/pi/project_demo/lib')
from McLumk_Wheel_Sports import *


def drive_square(speed=100, forward_duration=1.0, strafe_duration=1.2, pause=1.0):
    """Drives the Raspbot in a square pattern using Mecanum strafing."""
    movements = [
        ("Forward", move_forward, forward_duration),
        ("Right", move_right, strafe_duration),
        ("Backward", move_backward, forward_duration),
        ("Left", move_left, strafe_duration),
    ]

    for direction, move_func, duration in movements:
        print(f"Moving {direction} at speed {speed}...")
        move_func(speed)
        time.sleep(duration)
        stop_robot()
        time.sleep(pause)


def main():
    try:
        drive_square(speed=100, forward_duration=1.0, strafe_duration=1.2, pause=1.0)
        print("Square routine complete.")
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    finally:
        # Always stop the motors on exit or error
        stop_robot()
        print("Motors stopped safely.")


if __name__ == "__main__":
    main()
