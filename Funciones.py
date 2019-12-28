from OpenGL.GL import *
from Vector2D import *
from MuroDestructible import *
import math
import pygame
import random

def limpiar(cs):
    # saca los objetos destruidos del contenedor cs.
    n = len(cs)
    aux = []
    for i in range(n):
        c = cs.pop(0)
        if c.tipo=="Bomba":
            if not c.detonada:
                aux.append(c)
        elif c.tipo=="MuroDestructible":
            if not c.destruido:
                aux.append(c)
            if c.salida:
                a="Eliminado Muro Destructible que contiene salida"
        elif c.tipo=="Personaje":
            if c.vivo:
                aux.append(c)
        elif c.tipo=="PowerUp":
            if not c.usado:
                aux.append(c)

    for a in aux:
        cs.append(a)

def Circulo(rad,x,y,RGB):
    glPushMatrix()
    glTranslatef(x, y, 0.0)
    glScalef(rad, rad, 0.0)
    glColor4f(RGB[0], RGB[1], RGB[2], 1.0)
    glBegin(GL_POLYGON)
    for i in range(100) :
        calx=rad*math.cos(i)
        caly=rad*math.sin(i)
        glVertex2f(calx,caly)
    glEnd()
    glPopMatrix()

def estanChocando(c1,c2):
    x1=c1.x-c2.x
    y1=c1.y-c2.y
    distancia=(x1**2+y1**2)**0.5
    return distancia < (c1.rad + c2.rad)

def PuedoPasar(Personaje,Bombas,MurosDestructibles,Escena):
    for B in Bombas:
        if estanChocando(Personaje,B):
            return False
    for M in Escena.Muros:
        if estanChocando(Personaje,M):
            return False
    for MD in MurosDestructibles:
        if estanChocando(Personaje,MD):
            return False
    return True

def printText(text,point,tamaño):
    fuente = pygame.font.Font("Letra.ttf", tamaño)
    mensaje = fuente.render(str(text) + '  ', True, (255, 255, 255))
    textData = pygame.image.tostring(mensaje, "RGBA", True)
    glRasterPos2d(point[0],point[1])
    glDrawPixels(mensaje.get_width(), mensaje.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

def MuroAleatorio(Personajes,MurosInternos,Lista):
    Muro_x =[90,150,210,270,330,390,450,510,570,630,690,750,810]
    Muro_y=[20,70,120,170,220,270,320,370,420,470,520]
    while True:
        x= random.randint(0, 12)
        y= random.randint(0, 10)
        if not(ElementoCompartido(Murodestructible(Muro_x[x],Muro_y[y]),MurosInternos)):
            if not(ElementoCompartido(Murodestructible(Muro_x[x],Muro_y[y]),Lista)):
                if not(ElementoCompartido(Murodestructible(Muro_x[x],Muro_y[y]),Personajes)):
                    return Murodestructible(Muro_x[x], Muro_y[y])

def MuroPw(Muros,Pw):
    for M in Muros:
        if estanChocando(M,Pw):
            return True
    return False

def CrearMurosDestructibles(Personajes,MurosInternos,Lista):
    while len(Lista)!=85:
        Lista.append(MuroAleatorio(Personajes,MurosInternos,Lista))

def PosicionSalidaAleatoria(Lista):
    i=random.randint(0,len(Lista)-1)
    Lista[i].salida=True
    return [Lista[i].x,Lista[i].y]

def ElementoCompartido(Object,List):
    if len(List)!=0:
        if List[0].tipo=="Personaje":
            for l in List:
                if (Object.x == l.x and Object.y == l.y) or (Object.x == l.x and Object.y == l.y+50) \
                or (Object.x == l.x and Object.y == l.y-50) or(Object.x == l.x+60 and Object.y == l.y) or (Object.x == l.x-60 and Object.y == l.y):
                    return True
            return False
    for l in List:
        if Object.x==l.x and Object.y==l.y:
            return True
    return False

def MoverEnemigos(Personajes,Bombas, MurosDestructibles, es):
    for i in range(0, len(Personajes)):
        if not Personajes[i].amigo:
            Personajes[i].mover(Bombas,MurosDestructibles,es)

def SeEncuentraMuroConSalida(Lista):
    for M in Lista:
        if M.salida:
            return True
    return False

def Cruz(a):
    glBegin(GL_QUADS)
    glColor4f(1.0, 0.35, 0.0, 1.0)
    #Cruz Naranja

    #IZQUIERDO
    glVertex2f(-2.61 * a, 2.57 * a)
    glVertex2f(-2.68 * a, 3.34* a)
    glVertex2f(-1.85 * a, 3.63 * a)
    glVertex2f(-1.75 * a, 2.57 * a)

    glVertex2f(-3.02 * a, 2.61 * a)
    glVertex2f(-1.55 * a, 2.6 * a)
    glVertex2f(-1.66 * a, 1.95 * a)
    glVertex2f(-3.5 * a, 1.9 * a)

    #Derecho
    glVertex2f(2.61 * a, 2.57 * a)
    glVertex2f(2.68 * a, 3.34* a)
    glVertex2f(1.85 * a, 3.63 * a)
    glVertex2f(1.75 * a, 2.6 * a)

    glVertex2f(3.02 * a, 2.61 * a)
    glVertex2f(1.55 * a, 2.6 * a)
    glVertex2f(1.66 * a, 1.95 * a)
    glVertex2f(3.5 * a, 1.9 * a)
    #Abajo Izquierda

    glVertex2f(-2.61 * a, -1.57 * a)
    glVertex2f(-2.68 * a, -2.34* a)
    glVertex2f(-1.85 * a, -2.63 * a)
    glVertex2f(-1.75 * a, -1.6 * a)

    glVertex2f(-3.02 * a, -1.61 * a)
    glVertex2f(-1.55 * a, -1.6 * a)
    glVertex2f(-1.66 * a, -0.95 * a)
    glVertex2f(-3.5 * a, -0.9 * a)

    #Abajo Derecha
    glVertex2f(2.61 * a, -1.57 * a)
    glVertex2f(2.68 * a, -2.34 * a)
    glVertex2f(1.85 * a, -2.63 * a)
    glVertex2f(1.75 * a, -1.6 * a)

    glVertex2f(3.02 * a, -1.61 * a)
    glVertex2f(1.55 * a, -1.6 * a)
    glVertex2f(1.66 * a, -0.95 * a)
    glVertex2f(3.5 * a, -0.9 * a)
    #Amarillo
    glColor4f(1.0, 0.75, 0.0, 1.0)
    glVertex2f(-3.5 * a, 1.9 * a)
    glVertex2f(-0.93 * a, 1.95 * a)
    glVertex2f(-0.93 * a, 1.08 * a)
    glVertex2f(-3.8 * a, 1.22 * a)

    glVertex2f(-1.66 * a, 1.95 * a)
    glVertex2f(-1.65 * a, 3.63 * a)
    glVertex2f(-0.92 * a, 3.88 * a)
    glVertex2f(-0.93 * a, 1.08 * a)

    glVertex2f(3.5 * a, 1.9 * a)
    glVertex2f(0.93 * a, 1.95 * a)
    glVertex2f(0.93 * a, 1.08 * a)
    glVertex2f(3.8 * a, 1.22 * a)

    glVertex2f(1.66 * a, 1.95 * a)
    glVertex2f(1.65 * a, 3.63 * a)
    glVertex2f(0.92 * a, 3.88 * a)
    glVertex2f(0.93 * a, 1.08 * a)

    glVertex2f(-3.5 * a, -0.9 * a)
    glVertex2f(-0.93 * a, -0.95 * a)
    glVertex2f(-0.93 * a, -0.08 * a)
    glVertex2f(-3.8 * a, -0.22 * a)

    glVertex2f(-1.66 * a, -0.95 * a)
    glVertex2f(-1.65 * a, -3.0 * a)
    glVertex2f(-0.92 * a, -3.2 * a)
    glVertex2f(-0.93 * a, -0.08 * a)

    glVertex2f(3.5 * a, -0.9 * a)
    glVertex2f(0.93 * a, -0.95 * a)
    glVertex2f(0.93 * a, -0.08 * a)
    glVertex2f(3.8 * a, -0.22 * a)

    glVertex2f(1.66 * a, -0.95 * a)
    glVertex2f(1.65 * a, -3.0 * a)
    glVertex2f(0.92 * a, -3.2 * a)
    glVertex2f(0.93 * a, -0.08 * a)
    glEnd()