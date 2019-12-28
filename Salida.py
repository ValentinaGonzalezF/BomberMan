from OpenGL.GL import *
from Funciones import *
class Salida:
    def __init__(self,list):
        self.x = list[0]
        self.y = list[1]
        self.rad=25

    def dibujar(self,a):
        glPushMatrix()
        # Rectangulo de ancho 60 y largo 50
        glTranslatef(self.x, self.y, 0.0)
        glBegin(GL_QUADS)
        glColor4f(0.46, 0.35, 0.30, 1.0)
        #Rectangulo Central
        glVertex2f(-1.7*a, 3*a)
        glVertex2f(1.7*a, 3*a)
        glVertex2f(1.7*a, 0*a)
        glVertex2f(-1.7*a, 0*a)
        #Bordes
        glColor4f(0.36, 0.25, 0.20, 1.0)

        glVertex2f(-1.7 * a, 3 * a)
        glVertex2f(-1.37* a, 3 * a)
        glVertex2f(-1.37 * a, 0 * a)
        glVertex2f(-1.7 * a, 0 * a)

        glVertex2f(1.7 * a, 3 * a)
        glVertex2f(1.37 * a, 3 * a)
        glVertex2f(1.37 * a, 0 * a)
        glVertex2f(1.7 * a, 0 * a)

        glVertex2f(-1.7 * a, 3 * a)
        glVertex2f(1.7* a, 3 * a)
        glVertex2f(1.7 * a, 2.65 * a)
        glVertex2f(-1.7 * a, 2.65 * a)

        glVertex2f(-1.7 * a, 0.35 * a)
        glVertex2f(1.7 * a, 0.35 * a)
        glVertex2f(1.7* a, 0 * a)
        glVertex2f(-1.7 * a, 0 * a)

        glVertex2f(-0.15 * a, 3 * a)
        glVertex2f(0.15 * a, 3 * a)
        glVertex2f(0.15 * a, 0 * a)
        glVertex2f(-0.15 * a, 0 * a)

        glVertex2f(-0.72 * a, 1.7 * a)
        glVertex2f(-0.47 * a, 1.7 * a)
        glVertex2f(-0.47 * a, 1.25 * a)
        glVertex2f(-0.72 * a, 1.25 * a)

        glVertex2f(0.72 * a, 1.7 * a)
        glVertex2f(0.47 * a, 1.7 * a)
        glVertex2f(0.47 * a, 1.25 * a)
        glVertex2f(0.72 * a, 1.25 * a)
        glEnd()
        glPopMatrix()
