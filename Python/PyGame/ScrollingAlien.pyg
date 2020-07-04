import pgzrun

alien = Actor('alien')
alien.topright = 0,10

WIDTH = 300
# HEIGHT = 300
HEIGHT = alien.height + 20

def update():
    alien.left +=2 # Sets speed
    if alien.left > WIDTH:
        alien.right = 0

def draw():
    screen.clear()
    alien.draw()

pgzrun.go()
