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

    # Game logic should go here


    # Drawing code should go here
    # First, clear the screen to black
    screen.fill(BLACK)
    # Draws the white line in the middle
    pygame.draw.line(screen, WHITE, [349,0], [349, 500], 5) # 349 = Top half and bottom half
    # Update the display with what was drawn
    pygame.display.flip()
    # Limit the game to 60 FPS
    clock.tick(60)

pygame.quit()