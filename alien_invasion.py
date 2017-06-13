#Importing modules
import sys
import pygame

#Main func
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion v0")

    while True:
        #Checking keydowns
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    #Flipping display
    pygame.display.flip()
run_game()