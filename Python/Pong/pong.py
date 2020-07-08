import pygame
from paddle import Paddle
from ball import Ball
pygame.init()

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong!")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

# This is a list that cotains all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add the paddles and the ball to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
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
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: # Pressing the x Key will quit the game
                carryOn = False
    
    # Moving the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    # Game logic should go here
    all_sprites_list.update()

    # Check if the ball is hitting the side of the window
    if ball.rect.x>=690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]

    # Drawing code should go here
    # First, clear the screen to black
    screen.fill(BLACK)
   
    # Draws the white line in the middle
    pygame.draw.line(screen, WHITE, [349,0], [349, 500], 5) # 349 = Top half and bottom half
    
    # Draw the sprites all in one go
    all_sprites_list.draw(screen)

    # Update the display with what was drawn
    pygame.display.flip()
    # Limit the game to 60 FPS
    clock.tick(60)

pygame.quit()