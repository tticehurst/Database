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