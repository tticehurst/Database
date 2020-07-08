import pygame
pygame.init()

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong!")

# This loop will carry on until the user exists the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Main program loop
while carryOn:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False