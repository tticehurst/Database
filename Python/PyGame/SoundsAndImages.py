import pgzrun

alien = Actor('alien')
alien.pos = 100,56

WIDTH = 300
HEIGHT = alien.height + 20

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        sounds.alien_hurt.play()
        alien.image = 'alien_hurt'

def draw():
    screen.clear()
    alien.draw()

pgzrun.go()