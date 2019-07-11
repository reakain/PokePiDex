# Logic control for Pokedex
import poke_epd_display
import poke_audio_control
import poke_data_handle
import poke_buttons
import pygame
from gpiozero import Button

up = Button(2)
left = Button(3)
right = Button(4)
down = Button(14)

XDIM = 176
YDIM = 264
windowSize = [XDIM, YDIM]
delta = 10.0
GAME_LEVEL = 1
GOAL_RADIUS = 10
MIN_DISTANCE_TO_ADD = 1.0
NUMNODES = 5000
pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode(windowSize)
listFont = pygame.font.SysFont('Comic Sans MS', 48)
pFont
WHITE = 255, 255, 255
BLACK = 0, 0, 0


def main():
    pList = import_plist()
    pCurrent = 1
    currentState = 'plist'
    
    while(true):
        #handle button events
        if up.is_pressed:
        
		for e in pygame.event.get():
			if e.type == KEYUP && pCurrent != 1:
                pCurrent = pCurrent - 1
                if currentState == 'plist':
                    ptext1 = listFont.render('Some Text', False, BLACK)
                    screen.blit(ptext1,(0,4))
                    ptext2 = listFont.render('Some Text', False, BLACK)
                    screen.blit(ptext2,(0,56))
                    ptext3 = listFont.render('Some Text', False, WHITE)
                    pygame.draw.rect(screen, BLACK, (0,106,176,52), filled)
                    screen.blit(ptext3,(0,108))
                    ptext4 = listFont.render('Some Text', False, BLACK)
                    screen.blit(ptext4,(0,160))
                    ptext5 = listFont.render('Some Text', False, BLACK)
                    screen.blit(ptext5,(0,212))
                    
                elif currentState == 'pone':
                    pName = listFont.render(get_pname(pCurrent), False, BLACK)
                    
                    
                elif currentState == 'ptwo':
                
            elif e.key == KEYDOWN && pCurrent != pList.len():
                pCurrent = pCurrent + 1
                # call the state render function
                
            elif e.key == KEYLEFT && currentState != 'plist':
                # call the state render function
                
            elif e.key == KEYRIGHT && currentState != 'ptwo':
                # call the state render function
                
            elif e.key == K_OKAY:
                if currentState == 'plist':
                    # render pone on current poke
                elif (currentState == 'pone' || currentState == 'ptwo'):
                    # play poke audio

		
		fpsClock.tick(10000)

    
   
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
            
    def get_poke_names(pList):
    
    def get_poke_deets(pId):
    
    def go_up():
        if pShowList:
            decrement_plist()
        elif pShowOne:
        elif pShowTwo:
    
    def go_down():
        if pShowList:
            increment_plist()
        elif pShowOne:
        elif pShowTwo:
    
    def go_left():
    
    def go_okay():
