import sys
import time

# Append custom library path for Yahboom Raspbot / Mecanum driver
sys.path.append('/home/pi/project_demo/lib')

# Import Mecanum Car Driver functions
from McLumk_Wheel_Sports import *

def main():
    # Movement configuration parameters
    duration = 1.0  # seconds
    speed = 100     # PWM speed (0 to 255)

    try:
        print("Strafing right...")
        move_right(speed)
        time.sleep(duration)

        stop_robot()
        time.sleep(1.0)

        print("Strafing left...")
        move_left(speed)
        time.sleep(duration)

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

    finally:
        # Guarantee motors stop on completion, Ctrl+C, or error
        stop_robot()
        print("Robot stopped successfully.")

if __name__ == "__main__":
    main()
