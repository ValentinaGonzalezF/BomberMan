from OpenGL.GL import *
from MuroDestructible import *
from Bombas import *
from Escena import *
from Funciones import *
import random
class Enemigo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rad=5
        self.tipo="Personaje"
        self.amigo=False
        self.vivo = True
        self.random=random.randint(1,2)

    def mover(self, Bombas, MurosDestructibles, es):
        posicion = random.randint(1, 4)
        if posicion == 1:  # Arriba
            x = 0
            y = 50
        elif posicion == 2:  # Izquierda
            x = -60
            y = 0
        elif posicion == 3:  # Abajo
            x = 0
            y = -50
        else:  # Derecha
            x = 60
            y = 0

        auxpersonaje = Enemigo(self.x + x, self.y+ y)
        if PuedoPasar(auxpersonaje,Bombas,MurosDestructibles,es):
            self.x += x
            self.y += y
    def Aleatorio(self,Personajes,MurosInternos):
        Posicion_x = [90, 150, 210, 270, 330, 390, 450, 510, 570, 630, 690, 750, 810]
        Posicion_y = [20,70,120,170,220,270,320,370,420,470,520]
        while True:
            x = random.randint(0, 12)
            y = random.randint(0, 10)
            self.x=Posicion_x[x]
            self.y=Posicion_y[y]
            E = Enemigo(self.x,self.y)
            if not (ElementoCompartido(E, MurosInternos)):
                if not (ElementoCompartido(E,Personajes)):
                    return E

    def dibujar(self,a):
        if self.random==1:
            rosado = [1.0, 0.0, 0.6, 1.0]

            glPushMatrix()
            glTranslatef(self.x, self.y, 0.0)

            Circulo(2.5, 0.0 * a, 4.45 * a, rosado)
            # Cara
            glColor4f(0.0, 0.0, 0.0, 1.0)
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
            # Torso
            glColor4f(0.0, 0.0, 0.0, 1.0)
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
            glColor4f(0.96, 0.80, 0.69, 1.0)
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
            glColor4f(0.0, 0.0, 0.0, 1.0)
            glVertex2f(-0.45 * a, 3.49 * a)
            glVertex2f(-0.25 * a, 3.49 * a)
            glVertex2f(-0.25 * a, 2.65 * a)
            glVertex2f(-0.45 * a, 2.65 * a)
            # Ojo Izquierdo
            glVertex2f(0.45 * a, 3.49 * a)
            glVertex2f(0.25 * a, 3.49 * a)
            glVertex2f(0.25 * a, 2.65 * a)
            glVertex2f(0.45 * a, 2.65 * a)
            # Cejas
            # Izquierda
            glVertex2f(-0.71 * a, 3.93 * a)
            glVertex2f(-0.8 * a, 3.88 * a)
            glVertex2f(-0.2 * a, 3.36 * a)
            glVertex2f(-0.2 * a, 3.39 * a)
            # Derecha
            glVertex2f(0.71 * a, 3.93 * a)
            glVertex2f(0.8 * a, 3.88 * a)
            glVertex2f(0.2 * a, 3.36 * a)
            glVertex2f(0.2 * a, 3.39 * a)

            glEnd()
            # Manos
            Circulo(2.5, -0.79 * a, 0.69 * a, rosado)
            Circulo(2.5, 0.79 * a, 0.69 * a, rosado)

            # Piernas
            glBegin(GL_QUADS)
            # Izquierda
            glColor4f(0.96, 0.80, 0.69, 1.0)
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
        else:
            azul = [0.196078, 0.5, 1.0, 1.0]
            rojo = [1.0, 0.1, 0.1, 1.0]
            blanco = [1.0, 1.0, 1.0, 1.0]

            glPushMatrix()
            glTranslatef(self.x, self.y, 0.0)

            Circulo(2.5, 0.0 * a, 4.45 * a, blanco)
            # Cara
            glColor4f(0.096078, 0.4, 1.0, 1.0)
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

            glColor4f(0.2, 0.2, 0.2, 1.0)
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
            # Torso
            glColor4f(0.096078, 0.4, 1.0, 1.0)
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
            glColor4f(1.0, 1.0, 1.0, 1.0)
            glVertex2f(-0.36 * a, 2.06 * a)
            glVertex2f(-0.59 * a, 2.09 * a)
            glVertex2f(-0.89 * a, 0.88 * a)
            glVertex2f(-0.57 * a, 0.82 * a)
            # Brazo Derecho
            glVertex2f(0.36 * a, 2.06 * a)
            glVertex2f(0.59 * a, 2.09 * a)
            glVertex2f(0.89 * a, 0.88 * a)
            glVertex2f(0.57 * a, 0.82 * a)

            glEnd()
            glBegin(GL_POLYGON)
            # Ojo Izquierdo
            glColor4f(1.0, 1.0, 0.0, 1.0)
            glVertex2f(-0.72 * a, 3.51 * a)
            glVertex2f(-0.5 * a, 3.38 * a)
            glVertex2f(-0.20 * a, 3.25 * a)
            glVertex2f(-0.20 * a, 2.99 * a)
            glVertex2f(-0.49 * a, 2.92 * a)
            glVertex2f(-0.74 * a, 3.01 * a)
            glVertex2f(-0.81 * a, 3.2 * a)
            glEnd()

            glBegin(GL_POLYGON)
            # Ojo Derecho
            glColor4f(1.0, 1.0, 0.0, 1.0)
            glVertex2f(0.72 * a, 3.51 * a)
            glVertex2f(0.5 * a, 3.38 * a)
            glVertex2f(0.20 * a, 3.25 * a)
            glVertex2f(0.20 * a, 2.99 * a)
            glVertex2f(0.49 * a, 2.92 * a)
            glVertex2f(0.74 * a, 3.01 * a)
            glVertex2f(0.81 * a, 3.2 * a)
            glEnd()

            # U
            glBegin(GL_POLYGON)
            glColor4f(1.0, 0.5, 0.0, 1.0)
            glVertex2f(-0.37 * a, 4.28 * a)
            glVertex2f(-0.11 * a, 4.31 * a)
            glVertex2f(-0.1 * a, 3.73 * a)
            glVertex2f(0.0 * a, 3.63 * a)
            glVertex2f(0.0 * a, 3.44 * a)
            glVertex2f(-0.27 * a, 3.5 * a)
            glVertex2f(-0.37 * a, 3.57 * a)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex2f(0.37 * a, 4.28 * a)
            glVertex2f(0.11 * a, 4.31 * a)
            glVertex2f(0.1 * a, 3.73 * a)
            glVertex2f(0.0 * a, 3.63 * a)
            glVertex2f(0.0 * a, 3.44 * a)
            glVertex2f(0.27 * a, 3.5 * a)
            glVertex2f(0.37 * a, 3.57 * a)
            glEnd()

            # Manos
            Circulo(2.5, -0.79 * a, 0.69 * a, rojo)
            Circulo(2.5, 0.79 * a, 0.69 * a, rojo)

            # Piernas
            glBegin(GL_QUADS)
            # Izquierda
            glColor4f(1.0, 1.0, 1.0, 1.0)  # Blanco
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
            glColor4f(0.096078, 0.4, 1.0, 1.0)
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

def CrearEnemigos(Personajes,MurosInternos):
    while len(Personajes)!=5:
        a=Enemigo(1,1)
        Personajes.append(a.Aleatorio(Personajes,MurosInternos))