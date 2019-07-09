# Logic control for Pokedex
import poke_epd_display
import poke_audio_control
import poke_data_handle
import poke_buttons

def main():
    
    
    
from . import poke_pins
class PokeButtons:

    def __init__(self):
        self.b_up = poke_pins.b_up
        self.b_down = poke_pins.b_down
        self.b_left = poke_pins.b_left
        self.b_right = poke_pins.b_right
        self.b_okay = poke_pins.b_okay
        self.b_sound = poke_pins.b_sound
        
    def sample_buttons():
        self.b_up.switch_to_input(Pull.UP)
        self.b_down.switch_to_input(Pull.UP)
        self.b_left.switch_to_input(Pull.UP)
        self.b_right.switch_to_input(Pull.UP)
        self.b_okay.switch_to_input(Pull.UP)
        self.b_sound.switch_to_input(Pull.UP)
        for k in (self.b_up, self.b_down, self.b_left, self.b_right, self.b_okay, self.b_sound):
            yield not k.value  # False is pressed