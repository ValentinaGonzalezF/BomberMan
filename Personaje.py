from OpenGL.GL import *
from Enemigo import *
from Funciones import *
from Salida import *

class Personaje:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rad = 5
        self.vivo=True
        self.amigo = True
        #self.pasar=True
        self.tipo="Personaje"
        self.vida=1
        self.bombas=1

    def EncuentraSalida(self,Salida):
        if self.x==Salida.x and self.y==Salida.y:
            return True
        return False
    def dibujar(self,a):
        rosado=[1.0, 0.0, 0.6, 1.0]

        glPushMatrix()
        glTranslatef(self.x, self.y, 0.0)
        Circulo(2.5, 0.0 * a, 4.45 * a, rosado)
        # Cara
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glBegin(GL_POLYGON)
        glVertex2f(0.66 * a, 4.41 * a)
        glVertex2f(1.03 * a, 4.25 * a)
        glVertex2f(1.27 * a, 3.66 * a)
        glVertex2f(1.27 * a, 3.03 * a)
        glVertex2f(1.15 * a, 2.37 * a)
        glVertex2f(0.87 * a, 2.13 * a)
        glVertex2f(-0.87 * a, 2.13 * a)
        glVertex2f(-1.15 * a, 2.37 * a)
        glVertex2f(-1.27 * a, 3.03 * a)
        glVertex2f(-1.27 * a, 3.66 * a)
        glVertex2f(-1.03 * a, 4.25 * a)
        glVertex2f(-0.66 * a, 4.41 * a)
        glEnd()

        glColor4f(0.96, 0.80, 0.69, 1.0)
        glBegin(GL_POLYGON)
        glVertex2f(-0.55 * a, 4.03 * a)
        glVertex2f(-0.90 * a, 3.63 * a)
        glVertex2f(-0.93 * a, 3.63 * a)
        glVertex2f(-0.93 * a, 3.06 * a)
        glVertex2f(-0.84 * a, 2.47 * a)
        glVertex2f(-0.41 * a, 2.38 * a)
        glVertex2f(0.41 * a, 2.38 * a)
        glVertex2f(0.84 * a, 2.47 * a)
        glVertex2f(0.93 * a, 3.06 * a)
        glVertex2f(0.93 * a, 3.63 * a)
        glVertex2f(0.90 * a, 3.63 * a)
        glVertex2f(0.55 * a, 4.03 * a)
        glEnd()

        glBegin(GL_POLYGON)
        #Torso

        glColor4f(0.2, 0.2, 1.0, 1.0) #Azul
        glVertex2f(-0.46 * a, 2.06 * a)
        glVertex2f(0.46 * a, 2.06 * a)
        glVertex2f(0.67 * a, 1.02 * a)
        glVertex2f(0.49 * a, 0.93 * a)
        glVertex2f(0.0 * a, 0.84 * a)
        glVertex2f(-0.49 * a, 0.93 * a)
        glVertex2f(-0.67 * a, 1.2 * a)
        glEnd()
        glBegin(GL_QUADS)
        # Brazo Izquierdo
        glColor4f(1.0, 1.0, 1.0, 1.0) #Blanco
        glVertex2f(-0.36 * a, 2.06 * a)
        glVertex2f(-0.59 * a, 2.09 * a)
        glVertex2f(-0.89 * a, 0.88 * a)
        glVertex2f(-0.57 * a, 0.82 * a)
        # Brazo Derecho
        glVertex2f(0.36 * a, 2.06 * a)
        glVertex2f(0.59 * a, 2.09 * a)
        glVertex2f(0.89 * a, 0.88 * a)
        glVertex2f(0.57 * a, 0.82 * a)
        # Ojo Derecho
        glColor4f(0.0,0.0,0.0,1.0)
        glVertex2f(-0.45 * a, 3.49 * a)
        glVertex2f(-0.25 * a, 3.49 * a)
        glVertex2f(-0.25 * a, 2.65 * a)
        glVertex2f(-0.45 * a, 2.65 * a)
        # Ojo Izquierdo
        glVertex2f(0.45 * a, 3.49 * a)
        glVertex2f(0.25 * a, 3.49 * a)
        glVertex2f(0.25 * a, 2.65 * a)
        glVertex2f(0.45 * a, 2.65 * a)

        glEnd()
        #Manos
        Circulo(2.5, -0.79 * a, 0.69 * a, rosado)
        Circulo(2.5, 0.79 * a, 0.69 * a, rosado)

        # Piernas
        glBegin(GL_QUADS)
        # Izquierda
        glColor4f(1.0, 1.0,1.0, 1.0)  # Blanco
        glVertex2f(0.0 * a, 0.84 * a)
        glVertex2f(-0.29 * a, 0.93 * a)
        glVertex2f(-0.17 * a, 0.2 * a)
        glVertex2f(-0.0 * a, 0.17 * a)
        # Derecha
        glVertex2f(0.0 * a, 0.84 * a)
        glVertex2f(0.29 * a, 0.93 * a)
        glVertex2f(0.17 * a, 0.2 * a)
        glVertex2f(0.0 * a, 0.17 * a)
        glEnd()
        # Pies
        glColor4f(1.0, 0.0, 0.6, 1.0)
        glBegin(GL_POLYGON)
        glVertex2f(0.0 * a, 0.17 * a)
        glVertex2f(-0.17 * a, 0.2 * a)
        glVertex2f(-0.61 * a, 0.14 * a)
        glVertex2f(-0.82 * a, -0.14 * a)
        glVertex2f(-0.63 * a, -0.2 * a)
        glVertex2f(0.63 * a, -0.2 * a)
        glVertex2f(0.82 * a, -0.14 * a)
        glVertex2f(0.61 * a, 0.14 * a)
        glVertex2f(0.17 * a, 0.2 * a)
        glVertex2f(0.0 * a, 0.17 * a)
        glEnd()

        glPopMatrix()