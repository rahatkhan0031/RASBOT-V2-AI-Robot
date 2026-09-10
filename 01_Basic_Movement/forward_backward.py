import sys
import time

# Append custom driver path
sys.path.append("/home/pi/project_demo/lib")

# Import Mecanum Car Driver functions
from McLumk_Wheel_Sports import *


def main():
    # Movement parameters
    duration = 1.0  # seconds
    speed = 100

    try:
        # Move forward
        move_forward(speed)
        time.sleep(duration)
        stop_robot()
        time.sleep(0.5)

        # Move backward
        move_backward(speed)
        time.sleep(duration)

    except KeyboardInterrupt:
        print("\nInterrupted by user. Shutting down...")

    finally:
        # Always ensure motors stop on exit or error
        stop_robot()
        print("Motors stopped.")

        # Clean up bot instance if defined by the library
        if "bot" in globals():
            del globals()["bot"]


if __name__ == "__main__":
    main()