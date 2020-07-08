import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    # This class repesents a paddle
    def __init__(self,color,width,height):
        super().__init__()

        # Pass in the color of the paddle, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw a paddle
        pygame.draw.rect(self.image, color, [0,0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
    
    def moveUp(self, pixels):
        self.rect.y -= pixels # If y is lower than the pixels
        # Checks that you are not going too far (off the screen)
        if self.rect.y < 0:
            self.rect.y = 0
    
    def moveDown(self, pixels):
        self.rect.y += pixels # If y is higher than the pixels
        if self.y > 400:
            self.rect.y = 400

        