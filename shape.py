import os
import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os


class Shape():

    def __init__(self, pos=[0, 0, 0], rotate=[0, 0, 0], scale=[1, 1, 1]):
        self.vao = None
        self.vbo = None
        self.program = None
        self.vertexes = None
        self.drawing_type = None
        self.vertex_length = None
        self.pos = np.array(pos, dtype=np.float32)
        self.rotate = np.array(rotate, dtype=np.float32)
        self.scale = np.array(scale, dtype=np.float32)

    def getFileContents(self, filename):
        p = os.path.join(os.getcwd(), "shaders", filename)
        return open(p, 'r').read()

    def update(self):
        moveLocation = glGetUniformLocation(self.program, "newPose")
        glUniform3fv(moveLocation, 1, self.pos)
        rotateLoc = glGetUniformLocation(self.program, "angles")
        glUniform3fv(rotateLoc, 1, self.rotate)
        rotateLoc = glGetUniformLocation(self.program, "scale")
        glUniform3fv(rotateLoc, 1, self.scale)
    
    def on_event(self, event):
        pass
        
