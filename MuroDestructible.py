from OpenGL.GL import *
from Funciones import *

class Murodestructible:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.destruido = False
        self.rad=25
        self.tipo="MuroDestructible"
        self.salida=False

    def dibujar(self):
        glPushMatrix()
        # Rectangulo de ancho 60 y largo 50
        glTranslatef(self.x, self.y, 0.0)
        glBegin(GL_QUADS)
        glColor4f(0.5, 0.5, 0.5, 1.0)
        glVertex2f(-30, 0)
        glVertex2f(-30, 50)
        glVertex2f(30, 50)
        glVertex2f(30, 0)

        glColor4f(0.4, 0.4, 0.4, 1.0)
        glVertex2f(30, 7)
        glVertex2f(30, 3)
        glVertex2f(-30, 3)
        glVertex2f(-30, 7)

        glVertex2f(30, 17)
        glVertex2f(30, 21)
        glVertex2f(-30, 21)
        glVertex2f(-30, 17)

        glVertex2f(30, 33)
        glVertex2f(30, 38)
        glVertex2f(-30, 38)
        glVertex2f(-30, 33)

        glColor4f(0.22, 0.22, 0.22, 1.0)
        #Sombras
        glVertex2f(30, 0)
        glVertex2f(30, 3)
        glVertex2f(-30, 3)
        glVertex2f(-30, 0)

        glVertex2f(-30, 14)
        glVertex2f(30, 14)
        glVertex2f(30, 17)
        glVertex2f(-30, 17)

        glVertex2f(-30, 34)
        glVertex2f(30, 34)
        glVertex2f(30, 31)
        glVertex2f(-30, 31)

        glVertex2f(-27,50)
        glVertex2f(-30, 50)
        glVertex2f(-30, 34)
        glVertex2f(-27, 34)

        glVertex2f(-25, 50)
        glVertex2f(-30, 50)
        glVertex2f(-30, 46)
        glVertex2f(-25, 46)

        glVertex2f(-10, 31)
        glVertex2f(-7, 31)
        glVertex2f(-7, 17)
        glVertex2f(-10, 17)

        glVertex2f(13, 3)
        glVertex2f(16, 3)
        glVertex2f(16, 17)
        glVertex2f(13, 17)

        glVertex2f(-5, 31)
        glVertex2f(-7, 31)
        glVertex2f(-7, 28)
        glVertex2f(-5, 28)

        glVertex2f(18, 11)
        glVertex2f(16, 11)
        glVertex2f(16, 14)
        glVertex2f(18, 14)

        #Luz
        glColor4f(0.6, 0.6, 0.6, 1.0)
        #Primer rectangulo
        glVertex2f(-23, 50)
        glVertex2f(30, 50)
        glVertex2f(30, 47)
        glVertex2f(-23, 47)

        glVertex2f(27, 50)
        glVertex2f(30, 50)
        glVertex2f(30, 34)
        glVertex2f(27, 34)

        #Segundo Rectangulo
        glVertex2f(-10, 31)
        glVertex2f(-13, 31)
        glVertex2f(-13, 17)
        glVertex2f(-10, 17)

        glVertex2f(-10, 31)
        glVertex2f(-30, 31)
        glVertex2f(-30, 28)
        glVertex2f(-10, 28)

        glVertex2f(-3, 31)
        glVertex2f(30, 31)
        glVertex2f(30, 28)
        glVertex2f(-3, 28)

        #Tercer rectangulo
        glVertex2f(13, 3)
        glVertex2f(10, 3)
        glVertex2f(10, 14)
        glVertex2f(13, 14)

        glVertex2f(20, 11)
        glVertex2f(30, 11)
        glVertex2f(30, 14)
        glVertex2f(20, 14)

        glVertex2f(-30,11)
        glVertex2f(13, 11)
        glVertex2f(13, 14)
        glVertex2f(-30, 14)

        glEnd()
        glPopMatrix()
