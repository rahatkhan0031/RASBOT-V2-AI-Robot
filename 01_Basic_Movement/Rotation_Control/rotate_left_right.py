import sys
import time
from McLumk_Wheel_Sports import *

def main():
    # Initialize the robot object if required by the library
    bot = McLumk_Wheel_Sports()

    # Define movement speed and duration
    duration = 1.25
    speed = 100

    try:
        rotate_left(speed)
        time.sleep(duration)
        stop_robot()
        time.sleep(1)

        rotate_right(speed)
        time.sleep(duration)
        stop_robot()
        time.sleep(1)

    except KeyboardInterrupt:
        # Stop the car safely on exit
        print("\nStopping robot...")
    finally:
        stop_robot()
        print("Off.")
        if 'bot' in locals():
            del bot

if __name__ == "__main__":
    main()
