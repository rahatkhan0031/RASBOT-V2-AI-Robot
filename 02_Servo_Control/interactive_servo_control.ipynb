from Raspbot_Lib import Raspbot
import ipywidgets as widgets
from ipywidgets import interact

# Initialize the Raspbot controller
bot = Raspbot()

# Default/reset angles for Servo 1 and Servo 2
DEFAULT_S1_ANGLE = 90
DEFAULT_S2_ANGLE = 25

def control_pwm_servos(servo1_angle: int, servo2_angle: int) -> None:
"""
Control two PWM servos simultaneously.

Args:
servo1_angle (int): Target angle for Servo 1 (0 to 180).
servo2_angle (int): Target angle for Servo 2 (0 to 110).
"""
bot.Ctrl_Servo(1, servo1_angle)
bot.Ctrl_Servo(2, servo2_angle)


# Create two interactive sliders to control the PWM servos
interact(
control_pwm_servos,
servo1_angle=widgets.IntSlider(
min=0, max=180, step=1, value=DEFAULT_S1_ANGLE, description="Servo 1"
),
servo2_angle=widgets.IntSlider(
min=0, max=110, step=1, value=DEFAULT_S2_ANGLE, description="Servo 2"
),
)

# Reset servos to their default positions
control_pwm_servos(DEFAULT_S1_ANGLE, DEFAULT_S2_ANGLE)

# Release the Raspbot object so other programs can access the hardware
del bot
