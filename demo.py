from canvas import Canvas
from triangle import Traingle
import pygame
import numpy as np
from cube import Cube
import pygame

c = Canvas(screen=(700, 700))
t = Traingle()
cube = Cube()
c.add_shape(t)
c.add_shape(cube)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        c.update()