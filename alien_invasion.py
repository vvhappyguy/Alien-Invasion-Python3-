#Importing modules
import sys
import pygame

#Main func
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("KeyLogger")
    bg_color = (230,230,230)
    print(screen)
    while True:
        #Checking keydowns
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if pygame.KEYDOWN:
                print(str(event) + "\n")
        screen.fill(bg_color)
        #Flipping display
        pygame.display.flip()
run_game()