from OpenGL.GL import *
from Muro import *
class Escena:
    def __init__(self,w,h):
        self.h=h
        self.w=w
        self.MurosInternos = []

    def FijarMuros(self):


        self.Muros= [Muro(150, 70), Muro(150, 170), Muro(150, 270), Muro(150, 370),Muro(150, 470) ,Muro(270, 70), Muro(270, 170),
                      Muro(270, 270), Muro(270, 370),Muro(270, 470), Muro(390, 70), Muro(390, 170), Muro(390, 270), Muro(390, 370),Muro(390, 470),
                      Muro(510, 70), Muro(510, 170), Muro(510, 270), Muro(510, 370),Muro(510, 470), Muro(630, 70), Muro(630, 170),
                      Muro(630, 270),Muro(630, 370),Muro(630, 470), Muro(750, 70), Muro(750, 170), Muro(750, 270), Muro(750, 370),Muro(750, 470),
                      Muro(30, -30), Muro(30, 20), Muro(30, 70), Muro(30, 120), Muro(30, 170), Muro(30, 220),
                      Muro(30, 270),Muro(30, 320), Muro(30, 370), Muro(30, 420), Muro(870, -30), Muro(870, 20),
                      Muro(870, 70),Muro(870, 120),Muro(870, 170), Muro(870, 220), Muro(870, 270), Muro(870, 320),
                      Muro(870, 370), Muro(870, 420),Muro(90, -30),Muro(150, -30), Muro(210, -30), Muro(270, -30), Muro(330, -30),
                      Muro(390, -30), Muro(450, -30), Muro(510, -30),Muro(570, -30),Muro(630, -30), Muro(690, -30), Muro(750, -30),
                      Muro(810, -30), Muro(870, -30), Muro(30, 570),Muro(90, 570),Muro(150, 570), Muro(210, 570),
                      Muro(270, 570), Muro(330, 570), Muro(390, 570), Muro(450, 570),Muro(510, 570),Muro(570, 570),
                      Muro(630, 570), Muro(690, 570), Muro(750, 570), Muro(810, 570), Muro(870, 570),Muro(30, 470),Muro(30, 520),Muro(870, 470),Muro(870, 520)]
        for i in range(0,30):
            self.MurosInternos.append(self.Muros[i])

    def dibujar(self):
        for M in self.Muros:
            M.dibujar()
        glPushMatrix()

        glBegin(GL_QUADS)
        glColor4f(1.0, 0.5, 0.0, 1.0)
        #Arriba
        glVertex2f(0,self.h)
        glVertex2f(self.w,self.h)
        glVertex2f(self.w,self.h-60)
        glVertex2f(0,self.h-60)

        #Franja
        glColor4f(0.7, 0.0, 0.0, 1.0)
        glVertex2f(0, self.h-60)
        glVertex2f(self.w, self.h-60)
        glVertex2f(self.w, self.h - 57)
        glVertex2f(0, self.h - 57)

        glVertex2f(400, self.h - 10)
        glVertex2f(500, self.h - 10)
        glVertex2f(500, self.h - 8)
        glVertex2f(400, self.h - 8)

        glVertex2f(400, self.h - 47)
        glVertex2f(500, self.h - 47)
        glVertex2f(500, self.h - 45)
        glVertex2f(400, self.h - 45)


        #Tiempo
        glColor4f(0.0, 0.0, 0.0, 1.0)
        glVertex2f(400, self.h -10)
        glVertex2f(500, self.h - 10)
        glVertex2f(500, self.h - 45)
        glVertex2f(400, self.h - 45)



        glEnd()
        glPopMatrix()

