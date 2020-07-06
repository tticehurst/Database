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
    def new_pos(self, random):
        self.x = random.radint(0, screen_width-self.width)
        self.y = random.radint(0, screen_height-self.height)

# The snake object
class Player():
    # Initialization
    def __init__(self, screen):
        self.x = screen.width/2
        self.y = screen_height/2
        self.width = 10
        self.height = 10
        self.velocity = 10
        self.direction = 'stop'
        self.body = []
        self.head.color = green
        self.body.color = brown
    # Draws the snake on the given surface
    def draw_player(self, surface):
        self.seg = []
        self.head = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(surface, self.head_color, self.head)
        if len(self.body) > 0:  # len = Length # If the length of the body is more than 0
            for unit in self.body:
                segment = pg.Rect(unit[0], unit[1], self.width, self.height)
                pg.draw.rect(surface, self.body_color, segment) # Telling it where it moves (I think)
                self.seg.append(segment)
    # Increases length of the snake
    def add_unit(self):
        if len(self.body) != 0: # if lenghth is not equal to 0
            index.len(self.body)-1
            x = self.body[index][0]
            y = self.body[index][1]
            self.body.append([x,y])
            
        else:
            self.body.append([1000,1000])
    # Checks if there is a collision
    def is_collision(self):
        # Collision with itself
        for segment in self.seg:
            if self.head.colliderect(segment):
                return True
        # Collision with the boundries
        if self.y < 0 or self.y > screen_height - self.height or self.x < 0 or self.x > screen_width - self.width:
            return True
