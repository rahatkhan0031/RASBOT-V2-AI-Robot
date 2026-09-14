import sys
import time

# Add custom library path
sys.path.append('/home/pi/project_demo/lib')

# Import Mecanum Car Driver Library
from McLumk_Wheel_Sports import *


def execute_movement(move_func, speed=100, duration=1.0, pause=0.6):
    """Executes a directional move, waits, and stops."""
    move_func(speed)
    time.sleep(duration)
    stop_robot()
    time.sleep(pause)


def main():
    speed = 100
    duration = 1.0
    pause = 0.6

    # Ordered sequence of movements
    movements = [
        move_diagonal_left_front,
        move_diagonal_right_back,
        move_diagonal_right_front,
        move_diagonal_left_back,
    ]

    try:
        for move in movements:
            execute_movement(move, speed=speed, duration=duration, pause=pause)

    except KeyboardInterrupt:
        print("\nStopping car...")
    finally:
        # Ensures the motors stop and hardware safely cleans up
        stop_robot()
        if "bot" in globals():
            del bot
        print("Robot turned off.")


if __name__ == "__main__":
    main()
