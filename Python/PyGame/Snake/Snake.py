import pgzrun
import pygame

pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update

for event in pygame.event.get():
    print(event)

pgzrun.go()
