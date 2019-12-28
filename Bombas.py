from OpenGL.GL import *
from Vector2D import *
from Funciones import *
import pygame
class Bomba:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.detonada=False
        self.activada=False
        self.tipo="Bomba"
        self.rad=5
        self.tiempo=3
        self.sonidoExplosion=pygame.mixer.Sound("musica/Bomb.wav")
        self.sonidotic = pygame.mixer.Sound("musica/tic.wav")

    def tictac(self):
        self.tiempo -= 1
        if self.tiempo>0:
            self.sonidotic.set_volume(0.5)
            self.sonidotic.play()

    def explosionCentral(self,a):
        amarillo= [1.0, 0.85, 0.0]
        Circulo(5.4, self.x, self.y+28,amarillo)
        glPushMatrix()
        glTranslatef(self.x, self.y+22, 0.0)
        Cruz(a)
        glPopMatrix()
        self.detonada = True
        self.sonidoExplosion.set_volume(0.5)
        self.sonidoExplosion.play()

    def explosionCostados(self,direccion,Bombas,Muros,MurosDestructibles,Personajes,PowerUps):
        if "Derecha"==direccion:
            d = [self.x + 60, self.y]
            angulo=270
            a = 6.5
        elif "Izquierda"==direccion:
            d = [self.x - 60, self.y]
            angulo =90
            a=6.5
        elif "Arriba"==direccion:
            d = [self.x, self.y + 50]
            angulo =0
            a=8
        elif "Abajo"==direccion:
            d = [self.x, self.y - 50]
            angulo =180
            a=8
        aux=Bomba(d[0],d[1])
        contador=0
        while True:

            for Mu in MurosDestructibles:
                if estanChocando(aux, Mu):
                    Mu.destruido=True
                    self.dibujarCostados(d,a,angulo)
                    contador += 1
                    break
            for M in Muros:
                if estanChocando(aux,M):
                    contador += 1
                    break
            for B in Bombas:
                if estanChocando(aux,B):
                    contador += 1
                    break
            for P in Personajes:
                if estanChocando(aux,P):
                    if not P.amigo:
                        P.vivo = False
                    else:
                        if P.vida == 1:
                            P.vivo = False
                        else:
                            P.vida -= 1
                            for p in PowerUps:
                                if p.power=="VidaExtra" and p.activado:
                                    p.usado=True
                    self.dibujarCostados(d,a,angulo)
                    contador+=1
                    break
            for Pw in PowerUps:
                if estanChocando(aux,Pw):
                    contador += 1
                    break


            if contador==1:
                break
            self.dibujarCostados(d,a,angulo)
            break
        for P in Personajes:
            if P.amigo:
                if P.bombas == 0:
                    P.bombas += 1
                else:
                    for p in PowerUps:
                        if p.activado and p.power=="BombaExtra":
                            p.usado = True

    def dibujarCostados(self,d,a,angulo):
        amarillo = [1.0, 0.85, 0.0]
        glPushMatrix()

        glTranslatef(d[0], d[1]+26, 0.0)
        glRotate(angulo, 0.0, 0.0, 1.0)

        glBegin(GL_POLYGON)
        #Externo
        glColor4f(1.0, 0.0, 0.0, 1.0)
        glVertex2f(-3.16*a,-6.0*a)
        glVertex2f(-3.26*a, -1.1*a)
        glVertex2f(-3.24*a, -0.21*a)
        glVertex2f(-3.19*a, 0.33*a)
        glVertex2f(-3.15*a, 1.3*a)
        glVertex2f(-2.84*a,1.6*a)
        glVertex2f(-1.86*a, 2.0*a)
        glVertex2f(1.86*a, 2.0*a)
        glVertex2f(2.84*a, 1.6*a)
        glVertex2f(3.15*a, 1.3*a)
        glVertex2f(3.19*a, 0.33*a)
        glVertex2f(3.24*a, -0.21*a)
        glVertex2f(3.26*a, -1.1*a)
        glVertex2f(3.16*a, -6.0*a)
        #Interno
        glVertex2f(2.83*a, -6.0*a)
        glVertex2f(2.9*a, 0.2*a)
        glVertex2f(2.72*a, 1.21*a)
        glVertex2f(2.54*a, 2.23*a)
        glVertex2f(1.83*a, 2.8*a)
        glVertex2f(0*a,3*a)
        glVertex2f(-1.83*a, 2.8*a)
        glVertex2f(-2.54*a, 2.23*a)
        glVertex2f(-2.72*a, 1.21*a)
        glVertex2f(-2.9*a, 0.2*a)
        glVertex2f(-2.83*a, -6.0*a)
        glEnd()

        glBegin(GL_POLYGON)
        # Externo
        glColor4f(1.0, 0.35, 0.0, 1.0)
        glVertex2f(2.83 * a, -6.0 * a)
        glVertex2f(2.9 * a, -0.2 * a)
        glVertex2f(2.72 * a, 0.21 * a)
        glVertex2f(2.54 * a, 1.23 * a)
        glVertex2f(1.83 * a, 2.2 * a)
        glVertex2f(0 * a, 2.3 * a)
        glVertex2f(-1.83 * a, 2.2 * a)
        glVertex2f(-2.54 * a, 1.23 * a)
        glVertex2f(-2.72 * a, 0.21 * a)
        glVertex2f(-2.9 * a, -0.2 * a)
        glVertex2f(-2.83 * a, -6.0 * a)
        glEnd()

        glBegin(GL_POLYGON)
        # Externo
        glColor4f(1.0, 0.75, 0.0, 1.0)
        glVertex2f(1.83 * a, -6.0 * a)
        glVertex2f(1.9 * a, -0.2 * a)
        glVertex2f(1.72 * a, 0.21 * a)
        glVertex2f(1.54 * a, 1.23 * a)
        glVertex2f(0.83 * a, 1.6 * a)
        glVertex2f(0 * a, 1.7 * a)
        glVertex2f(-0.83 * a, 1.6 * a)
        glVertex2f(-1.54 * a, 1.23 * a)
        glVertex2f(-1.72 * a, 0.21 * a)
        glVertex2f(-1.9 * a, -0.2 * a)
        glVertex2f(-1.83 * a, -6.0 * a)
        glEnd()
        glBegin(GL_QUADS)
        glColor4f(1.0, 0.85, 0.0,1.0)
        glVertex2f(0.83 * a, 1.6 * a)
        glVertex2f(-0.83 * a, 1.6 * a)
        glVertex2f(-0.83 * a, -5* a)
        glVertex2f(0.83 * a, -5* a)
        glEnd()
        glPopMatrix()

    def dibujar(self):
        azul = [0.1, 0.30, 0.35]
        azulotro=[0.1,0.25,0.3]
        azul1=[0.0, 0.2, 0.2, 1.0]
        azul2=[0.1,0.40,0.50]
        gris=[0.4,0.4,0.4,1.0]
        Circulo(5, self.x-2, self.y+22,azul1)
        Circulo(4.1, self.x -7, self.y+23, azulotro)
        Circulo(3.7, self.x - 11, self.y+28, azul)
        Circulo(3.2, self.x - 12, self.y+30, azul2)
        Circulo(2.5, self.x +13, self.y + 37,gris)

        glPushMatrix()
        glTranslatef(self.x, self.y+22, 0.0)
        glBegin(GL_QUADS)

        glColor4f(0.3, 0.6, 0.6, 1.0)

        glVertex2f(-7, 13)
        glVertex2f(-18, 13)
        glVertex2f(-18, 4)
        glVertex2f(-7, 4)

        glColor4f(1.0, 1.0, 1.0, 1.0)
        glVertex2f(-17,7)
        glVertex2f(-11, 7)
        glVertex2f(-11,13)
        glVertex2f(-17, 13)

        glVertex2f(11, 18)
        glVertex2f(8, 18)
        glVertex2f(8, 11)
        glVertex2f(11, 11)

        glColor4f(0.0, 0.15, 0.12, 1.0)

        glVertex2f(22, 7)
        glVertex2f(14, 7)
        glVertex2f(14, -14)
        glVertex2f(22, -14)

        glVertex2f(17, -10)
        glVertex2f(14, -10)
        glVertex2f(14, -14)
        glVertex2f(17, -14)

        glVertex2f(-13, 24)
        glVertex2f(8, 24)
        glVertex2f(8, 19)
        glVertex2f(-13, 19)

        glVertex2f(12,-10)
        glVertex2f(16, -10)
        glVertex2f(16, -14)
        glVertex2f(12, -14)

        glEnd()
        #MECHA BOMBA
        glBegin(GL_LINES)
        glColor4f(0.0, 0.3, 0.1, 1.0)
        glVertex2f(12, 16)
        glVertex2f(20, 24)
        glVertex2f(13, 14)
        glVertex2f(23, 23)
        glVertex2f(13, 13)
        glVertex2f(23, 24)
        glVertex2f(11, 14)
        glVertex2f(22, 24)
        glColor4f(0.8, 0.0, 0.0, 1.0)
        glVertex2f(21, 24)
        glVertex2f(25, 24)
        glVertex2f(21, 25)
        glVertex2f(25, 25)
        glVertex2f(21, 23)
        glVertex2f(25, 23)
        glColor4f(1.0, 1.0, 0.0, 1.0)
        glVertex2f(27, 24)
        glVertex2f(25, 24)
        glVertex2f(27, 25)
        glVertex2f(25, 25)
        glVertex2f(27, 23)
        glVertex2f(25, 23)
        glEnd()
        #Sombras
        glColor4f(0.0, 0.15, 0.12, 1.0)
        glBegin(GL_POLYGON)
        glVertex2f(-13, -24)
        glVertex2f(5, -24)
        glVertex2f(12, -24)
        glVertex2f(15, -20)
        glVertex2f(17, -20)
        glVertex2f(20, -15)
        glVertex2f(22, -10)
        glVertex2f(19, -17)
        glVertex2f(13, -22)
        glVertex2f(13, -24)
        glVertex2f(0, -24)
        glEnd()
        glPopMatrix()