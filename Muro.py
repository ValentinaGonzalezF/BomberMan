from OpenGL.GL import *
from Funciones import *
class Muro:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rad=25
        self.tipo="Muro"

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0.0)


        glBegin(GL_QUADS)
        #Rectangulo de ancho 60 y largo 50
        glColor4f(0.5, 0.5, 0.5, 1.0)
        glVertex2f(-30, 50)
        glVertex2f(-30, 0)
        glVertex2f(30, 0)
        glVertex2f(30, 50)
        #Sombra
        glColor4f(0.30, 0.30, 0.30, 1.0)
        glVertex2f(-25, 50)
        glVertex2f(-22, 50)
        glVertex2f(-22, 0)
        glVertex2f(-25, 0)


        glColor4f(0.22, 0.22, 0.22, 1.0)
        glVertex2f(-30, 0)
        glVertex2f(30,0)
        glVertex2f(30, 6)
        glVertex2f(-30, 6)

        glColor4f(0.25, 0.25, 0.25, 1.0)
        glVertex2f(-22, 6)
        glVertex2f(30, 6)
        glVertex2f(30, 10)
        glVertex2f(-22, 10)

        glColor4f(0.27, 0.27, 0.27, 1.0)
        glVertex2f(-30, 50)
        glVertex2f(-30, 4)
        glVertex2f(-25, 4)
        glVertex2f(-25, 50)

        #Luz
        glColor4f(0.9, 0.9, 0.9, 1.0)
        glVertex2f(-25, 50)
        glVertex2f(25, 50)
        glVertex2f(25, 47)
        glVertex2f(-25, 47)

        glColor4f(0.62, 0.62,0.62, 1.0)
        glVertex2f(25, 47)
        glVertex2f(25, 8)
        glVertex2f(22, 8)
        glVertex2f(22, 47)

        glColor4f(0.6, 0.6, 0.6, 1.0)
        glVertex2f(30, 50)
        glVertex2f(30, 4)
        glVertex2f(25, 4)
        glVertex2f(25, 50)

        glColor4f(0.4, 0.4, 0.4, 1.0)
        glVertex2f(-22, 47)
        glVertex2f(-18, 47)
        glVertex2f(-18, 8)
        glVertex2f(-22, 8)

        glVertex2f(-22,8)
        glVertex2f(22, 8)
        glVertex2f(22,12)
        glVertex2f(-22, 12)

        glEnd()
        glPopMatrix()