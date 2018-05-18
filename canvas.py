import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os


class Canvas:

    def __init__(self, screen=[500, 500]):
        self.shapes = []
        self.events = None
        self.screen = screen
        self.initialize()

    def add_shape(self, shape):
        self.shapes.append(shape)

    def initialize(self):
        pygame.init()
        display = self.screen
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        glClearColor(.10, 0.25, 0.20, 1.0)
        glViewport(0, 0, self.screen[0], self.screen[1])
        self.events = pygame.event.get()

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)

        for shape in self.shapes:

            glUseProgram(shape.program)
            glBindVertexArray(shape.vao)
            shape.update()
            glDrawArrays(shape.drawing_type, 0, shape.vertex_length)
            glBindVertexArray(0)

    def update(self):
        self.draw()
        self.events = pygame.event.get()
        pygame.display.flip()
        pygame.time.wait(10)

    def quit(self):
        pygame.quit()
        quit()
