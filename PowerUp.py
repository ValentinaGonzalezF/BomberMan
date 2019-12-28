from OpenGL.GL import *
from Funciones import *
import random
class PowerUp:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rad=5
        self.tipo="PowerUp"
        self.power=""
        self.usado = False
        self.recogido=False
        self.activado=False
        self.dibujar=False
        self.a=13

    def VidaExtra(self):
        self.power="VidaExtra"

    def BombaExtra(self):
        self.power="BombaExtra"

    def Aleatorio(self, ListaPw, ListaMu):
        while True:
            i = random.randint(0, len(ListaMu) - 1)
            if not ListaMu[i].salida:
                self.x = ListaMu[i].x
                self.y = ListaMu[i].y
                pw = PowerUp(self.x, self.y)
                j = random.randint(0, 1)
                if j == 1:
                    pw.VidaExtra()
                else:
                    pw.BombaExtra()
                if not (ElementoCompartido(pw, ListaPw)):
                    return pw

    def dibujarVidaExtra(self):
        a = self.a
        negro = [0.0, 0.0, 0.0, 1.0]
        glPushMatrix()
        glTranslatef(self.x, self.y, 0.0)
        glBegin(GL_QUADS)
        glColor4f(0.0, 0.6, 0.8, 1.0)

        glVertex2f(-2.2 * a, 4 * a)
        glVertex2f(2.2 * a, 4 * a)
        glVertex2f(2.2 * a, 0 * a)
        glVertex2f(-2.2 * a, 0 * a)

        glColor4f(1.0, 0.0, 0.0, 1.0)
        glVertex2f(-2 * a, 4 * a)
        glVertex2f(2 * a, 4 * a)
        glVertex2f(2 * a, 3.65 * a)
        glVertex2f(-2 * a, 3.65 * a)

        glVertex2f(1.8 * a, 4 * a)
        glVertex2f(2.2 * a, 4 * a)
        glVertex2f(2.2 * a, 0 * a)
        glVertex2f(1.8 * a, 0 * a)

        glVertex2f(-2 * a, 0.37 * a)
        glVertex2f(2.2 * a, 0.37 * a)
        glVertex2f(2.2 * a, 0 * a)
        glVertex2f(-2 * a, 0 * a)

        glVertex2f(-2.2 * a, 0 * a)
        glVertex2f(-2.2 * a, 4 * a)
        glVertex2f(-1.82 * a, 4 * a)
        glVertex2f(-1.82 * a, 0 * a)

        glEnd()

        glBegin(GL_POLYGON)
        glColor4f(1.0, 0.0, 0.0, 1.0)

        glVertex2f(0.0* a, 2.59 * a)
        glVertex2f(-0.34 * a, 3.07* a)
        glVertex2f(-1.08* a, 3.33 * a)
        glVertex2f(-1.48* a, 2.97 * a)
        glVertex2f(-1.39 * a, 2.29 * a)
        glVertex2f(-0.91 * a, 1.73 * a)
        glVertex2f(-0.37 * a, 1.17 * a)
        glVertex2f(0.0 * a, 0.73 * a)
        glVertex2f(0.37 * a, 1.17 * a)
        glVertex2f(0.91 * a, 1.73 * a)
        glVertex2f(1.39 * a, 2.29 * a)
        glVertex2f(1.48 * a, 2.97 * a)
        glVertex2f(1.08 * a, 3.33 * a)
        glVertex2f(0.34 * a, 3.07 * a)
        glEnd()
        glBegin(GL_QUADS)
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glVertex2f(0.37 * a, 2.34 * a)
        glVertex2f(0.37 * a, 2.62 * a)
        glVertex2f(0.7 * a, 2.62 * a)
        glVertex2f(0.7 * a, 2.34 * a)

        glVertex2f(0.7 * a, 2.62 * a)
        glVertex2f(0.7 * a, 2.93 * a)
        glVertex2f(1.0 * a, 2.93 * a)
        glVertex2f(1.0 * a, 2.62 * a)

        glColor4f(0.0, 0.0,0.0, 1.0)
        glVertex2f(-0.16 * a, 0.6 * a)
        glVertex2f(0.16 * a, 0.6 * a)
        glVertex2f(0.16* a,0.84 * a)
        glVertex2f(-0.16* a, 0.84 * a)

        glVertex2f(-0.16 * a, 2.59 * a)
        glVertex2f(0.16 * a, 2.59 * a)
        glVertex2f(0.16 * a, 2.74 * a)
        glVertex2f(-0.16 * a, 2.74 * a)

        glVertex2f(1.25 * a, 3.03 * a)
        glVertex2f(1.47 * a, 3.03* a)
        glVertex2f(1.47 * a, 2.07 * a)
        glVertex2f(1.25 * a, 2.07 * a)

        glVertex2f(-1.25 * a, 3.03 * a)
        glVertex2f(-1.47 * a, 3.03 * a)
        glVertex2f(-1.47 * a, 2.07 * a)
        glVertex2f(-1.25 * a, 2.07 * a)

        glVertex2f(-0.75 * a, 1.24 * a)
        glVertex2f(-0.53 * a, 1.44 * a)
        glVertex2f(-0.15 * a, 0.78 * a)
        glVertex2f(-0.25 * a, 0.75 * a)

        glVertex2f(0.75 * a, 1.24 * a)
        glVertex2f(0.53 * a, 1.44 * a)
        glVertex2f(0.15 * a, 0.78 * a)
        glVertex2f(0.25 * a, 0.75 * a)

        glVertex2f(-0.75 * a, 1.24 * a)
        glVertex2f(-0.53 * a, 1.44 * a)
        glVertex2f(-1.41 * a,2.29 * a)
        glVertex2f(-1.50 * a, 2.20 * a)

        glVertex2f(0.75 * a, 1.24 * a)
        glVertex2f(0.53 * a, 1.44 * a)
        glVertex2f(1.41 * a, 2.29 * a)
        glVertex2f(1.50 * a, 2.20 * a)

        glVertex2f(-1.2 * a, 2.97 * a)
        glVertex2f(-1.30 * a, 3.04 * a)
        glVertex2f(-1.1 * a, 3.37 * a)
        glVertex2f(-1.0 * a, 3.23 * a)

        glVertex2f(1.2 * a, 2.97 * a)
        glVertex2f(1.30 * a, 3.04 * a)
        glVertex2f(1.1 * a, 3.37 * a)
        glVertex2f(1.0 * a, 3.23 * a)

        glVertex2f(-0.11* a, 2.71 * a)
        glVertex2f(-0.04 * a, 2.77 * a)
        glVertex2f(-0.26* a, 3.09 * a)
        glVertex2f(-0.41* a, 3.03 * a)

        glVertex2f(0.11 * a, 2.71 * a)
        glVertex2f(0.04 * a, 2.77 * a)
        glVertex2f(0.26 * a, 3.09 * a)
        glVertex2f(0.41 * a, 3.03 * a)

        glVertex2f(-1.0 * a, 3.33 * a)
        glVertex2f(-1.04 * a, 3.44 * a)
        glVertex2f(-0.26 * a, 3.09 * a)
        glVertex2f(-0.41 * a, 3.03 * a)

        glVertex2f(1.0 * a, 3.33 * a)
        glVertex2f(1.04 * a, 3.44 * a)
        glVertex2f(0.26 * a, 3.09 * a)
        glVertex2f(0.41 * a, 3.03 * a)

        glEnd()
        glPopMatrix()

    def dibujarBombaExtra(self):
        a=self.a
        negro=[0.0,0.0,0.0,1.0]
        glPushMatrix()
        glTranslatef(self.x, self.y, 0.0)
        glBegin(GL_QUADS)
        glColor4f(0.0, 0.6, 0.8, 1.0)

        glVertex2f(-2.2 * a, 4 * a)
        glVertex2f(2.2 * a, 4 * a)
        glVertex2f(2.2 * a, 0 * a)
        glVertex2f(-2.2 * a, 0 * a)

        glColor4f(1.0, 0.0, 0.0, 1.0)
        glVertex2f(-2 * a, 4 * a)
        glVertex2f(2 * a, 4 * a)
        glVertex2f(2 * a, 3.65 * a)
        glVertex2f(-2 * a, 3.65 * a)

        glVertex2f(1.8 * a, 4 * a)
        glVertex2f(2.2 * a, 4 * a)
        glVertex2f(2.2 * a, 0 * a)
        glVertex2f(1.8 * a, 0 * a)

        glVertex2f(-2 * a, 0.37 * a)
        glVertex2f(2.2 * a, 0.37 * a)
        glVertex2f(2.2 * a, 0 * a)
        glVertex2f(-2 * a, 0 * a)

        glVertex2f(-2.2 * a, 0 * a)
        glVertex2f(-2.2 * a, 4 * a)
        glVertex2f(-1.82 * a, 4 * a)
        glVertex2f(-1.82 * a, 0 * a)

        glEnd()

        dibujarBomba(-2,4.5,0.85)
        glPopMatrix()


def dibujarBomba(x,y,a):
    azul = [0.1, 0.30, 0.35]
    azulotro=[0.1,0.25,0.3]
    azul1=[0.0, 0.2, 0.2, 1.0]
    azul2=[0.1,0.40,0.50]
    gris=[0.4,0.4,0.4,1.0]
    Circulo(5*a, x-2*a, (y+22)*a,azul1)
    Circulo(4.1*a, (x -7)*a, (y+23)*a, azulotro)
    Circulo(3.7*a, (x - 11)*a, (y+28)*a, azul)
    Circulo(3.2*a, (x - 12)*a, (y+30)*a, azul2)
    Circulo(2.5*a, (x +13)*a, (y + 37)*a,gris)

    glPushMatrix()
    glTranslatef(x*a, (y+22)*a, 0.0)
    glBegin(GL_QUADS)

    glColor4f(0.3, 0.6, 0.6, 1.0)

    glVertex2f(-7*a, 13*a)
    glVertex2f(-18*a, 13*a)
    glVertex2f(-18*a, 4*a)
    glVertex2f(-7*a, 4*a)

    glColor4f(1.0, 1.0, 1.0, 1.0)
    glVertex2f(-17*a,7*a)
    glVertex2f(-11*a, 7*a)
    glVertex2f(-11*a,13*a)
    glVertex2f(-17*a, 13*a)

    glVertex2f(11*a, 18*a)
    glVertex2f(8*a, 18*a)
    glVertex2f(8*a, 11*a)
    glVertex2f(11*a, 11*a)

    glColor4f(0.0, 0.15, 0.12, 1.0)

    glVertex2f(20*a, 7*a)
    glVertex2f(12*a, 7*a)
    glVertex2f(12*a, -14*a)
    glVertex2f(20*a, -14*a)

    glVertex2f(17*a, -10*a)
    glVertex2f(14*a, -10*a)
    glVertex2f(14*a, -14*a)
    glVertex2f(17*a, -14*a)

    glVertex2f(-13*a, 21*a)
    glVertex2f(8*a, 21*a)
    glVertex2f(8*a, 16*a)
    glVertex2f(-13*a, 16*a)

    glVertex2f(12*a,-10*a)
    glVertex2f(16*a, -10*a)
    glVertex2f(16*a, -14*a)
    glVertex2f(12*a, -14*a)

    glEnd()
    #MECHA BOMBA
    glBegin(GL_LINES)
    glColor4f(0.0, 0.3, 0.1, 1.0)
    glVertex2f(12*a, 16*a)
    glVertex2f(20*a, 24*a)
    glVertex2f(13*a, 14*a)
    glVertex2f(23*a, 23*a)
    glVertex2f(13*a, 13*a)
    glVertex2f(23*a, 24*a)
    glVertex2f(11*a, 14*a)
    glVertex2f(22*a, 24*a)
    glColor4f(0.8, 0.0, 0.0, 1.0)
    glVertex2f(21*a, 24*a)
    glVertex2f(25*a, 24*a)
    glVertex2f(21*a, 25*a)
    glVertex2f(25*a, 25*a)
    glVertex2f(21*a, 23*a)
    glVertex2f(25*a, 23*a)
    glColor4f(1.0, 1.0, 0.0, 1.0)
    glVertex2f(27*a, 24*a)
    glVertex2f(25*a, 24*a)
    glVertex2f(27*a, 25*a)
    glVertex2f(25*a, 25*a)
    glVertex2f(27*a, 23*a)
    glVertex2f(25*a, 23*a)
    glEnd()
    #Sombras
    glColor4f(0.0, 0.15, 0.12,1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-13*a, -20*a)
    glVertex2f(5*a, -20*a)
    glVertex2f(12*a, -20*a)
    glVertex2f(15*a, -16*a)
    glVertex2f(18*a, -15*a)
    glVertex2f(18*a, -10*a)
    glVertex2f(18*a, -17*a)
    glVertex2f(13*a, -18*a)
    glVertex2f(0*a, -20*a)
    glEnd()
    glPopMatrix()

def PowerUpsAleatorios(ListaPw,ListaMu):
    while len(ListaPw)!=int(len(ListaMu)/4):
        P=PowerUp(1,1)
        ListaPw.append(P.Aleatorio(ListaPw,ListaMu))