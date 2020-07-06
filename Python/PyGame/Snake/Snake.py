import pygame as pg

# Colors
red = pg.Color(255,0,0)
green = pg.Color(0,255,0)
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)
brown = pg.Color(165, 42, 42)

# Variables
screen_width = 400
screen_height = 400

# Initialize pygame
pg.init()

# The screen
wn = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Snake!')

# The mainloop
run = True
while run:
     # Catches all the events that have happened since the game started
     for event in pg.event.get():
         # When you press the close window button
         if event.type == pg.QUIT:
             run = False
    
    # Fills the screen with black color
     wn.fill(black)

# Exits pygame
pg.quit()

# The class for the food object
class Food():
    # Initialization
    def __init__(self):
        self.x = screen_width/2
        self.y = screen_height/4
        self.color = red
        self.width = 10
        self.height = 10
    # Makes the food visible
    def draw_food(self, surface):
        self.food = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(surface, self.color, self.food)
    # Has the food been eaten?
    def is_eaten(self, head):
        return self.food.colliderect(head)
    # Returns a new position for the food after it is eaten
    def new_pos(self):
        self.x = random.radint(0, screen_width-self.width)
        self.y = rando.radint(0, screen_height-self.height)