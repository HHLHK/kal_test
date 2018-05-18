from shape import Shape
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
import numpy as np


class Traingle(Shape):

    def __init__(self):
        Shape.__init__(self)
        self.drawing_type = GL_TRIANGLES
        self.setup_shaders()
        self.setup_buffers()

    def setup_shaders(self):
        vertexShaderContent = self.getFileContents("d.vertex.shader")
        fragmentShaderContent = self.getFileContents("d.fragment.shader")
        
        vertexShader = compileShader(vertexShaderContent, GL_VERTEX_SHADER)
        fragmentShader = compileShader(
            fragmentShaderContent, GL_FRAGMENT_SHADER)

        self.program = glCreateProgram()
        glAttachShader(self.program, vertexShader)
        glAttachShader(self.program, fragmentShader)
        glLinkProgram(self.program)

    def setup_buffers(self):
        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)
        
        self.vertexes = np.array([
            [0.5, 0.0, 0.0,  1.0, 0.0, 0.0],
            [-0.5, 0.0, 0.0,  0.0, 1.0, 0.0],
            [0.0, 0.5, 0.0,  0.0, 0.0, 1.0]
        ], dtype=np.float32)

        self.vertex_length = len(self.vertexes)

        # vertex buffer
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertexes.nbytes,self.vertexes, GL_STATIC_DRAW)
        
        glBindVertexArray(self.vao)

        positionLocation = glGetAttribLocation(self.program, "position")
        glVertexAttribPointer(positionLocation, 3, GL_FLOAT, GL_FALSE,
                              6 * self.vertexes.itemsize, ctypes.c_void_p(0))
        glEnableVertexAttribArray(positionLocation)

        colorLocation = glGetAttribLocation(self.program, "newColor")
        glVertexAttribPointer(colorLocation, 3, GL_FLOAT, GL_FALSE,
                              6 * self.vertexes.itemsize, ctypes.c_void_p(12))
        glEnableVertexAttribArray(colorLocation)
        
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)
