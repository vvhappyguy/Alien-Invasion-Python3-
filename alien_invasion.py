#Importing modules
import sys
import pygame
from settings import Settings
from ship import Ship

#Main func
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion v0")
    ship = Ship(screen)
    while True:
        #Checking keydowns
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #Flipping display
        pygame.display.flip()
run_game()