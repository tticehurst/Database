import pgzrun

alien = Actor('alien_normal')
alien.pos = 100,56

WIDTH = 300
HEIGHT = alien.height + 20

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()
        clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.alien_hurt.play()
    

def set_alien_normal():
    alien.image = 'alien_normal'



def draw():
    screen.clear()
    alien.draw()

pgzrun.go()