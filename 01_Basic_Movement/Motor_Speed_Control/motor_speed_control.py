import time
from Raspbot_Lib import Raspbot
import ipywidgets as widgets
from ipywidgets import interact, Button, Output
from IPython.display import display

# Initialize the Raspbot instance
bot = Raspbot()

# Control individual motor speeds (-255 to 255)
def run_motor(M1, M2, M3, M4):
    bot.Ctrl_Muto(0, M1)
    bot.Ctrl_Muto(1, M2)
    bot.Ctrl_Muto(2, M3)
    bot.Ctrl_Muto(3, M4)
    return True

# Create interactive sliders for motor control
interact(
    run_motor,
    M1=widgets.IntSlider(min=-255, max=255, step=1, value=0, description='Motor 1:'),
    M2=widgets.IntSlider(min=-255, max=255, step=1, value=0, description='Motor 2:'),
    M3=widgets.IntSlider(min=-255, max=255, step=1, value=0, description='Motor 3:'),
    M4=widgets.IntSlider(min=-255, max=255, step=1, value=0, description='Motor 4:')
)

# Add a UI button to safely stop motors and cleanup object
stop_button = Button(description="Stop & Clean Up", button_style='danger')

def stop_and_cleanup(b):
    # Stop all 4 wheel channels
    bot.Ctrl_Car(0, 1, 0) # L1
    bot.Ctrl_Car(1, 1, 0) # L2
    bot.Ctrl_Car(2, 1, 0) # R1
    bot.Ctrl_Car(3, 1, 0) # R2
    print("Motors stopped and bot instance cleaned up.")

stop_button.on_click(stop_and_cleanup)
display(stop_button)
