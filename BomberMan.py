# -*- coding: iso-8859-1 -*-

import pygame,os,sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Vector2D import *
from Bombas import *
from Enemigo import *
from Escena import *
from Muro import *
from MuroDestructible import *
from Personaje import *
from Vista import *
from Funciones import *
from Reloj import *
from PowerUp import *

#####################################################################
# Funciones de graficos
#####################################################################

def init_pygame(w, h, title=""):
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = str(200) + "," + str(30)
    pygame.display.set_mode((w, h), OPENGL | DOUBLEBUF)
    pygame.display.set_caption(title)

def init():
    glClearColor(0.0, .5, 0.0, 0.0)
    glClearDepth(1.0)
    glDisable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)

def reshape(width, height):
    if height == 0:
        height = 1
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, width, 0.0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def init_opengl(w, h):
    init()
    reshape(w, h)

def main(argv):
    w = 900  # ancho
    h = 650  # alto

    PowerUps=[]
    Bombas = []
    MurosDestructibles = []
    Personajes = [Personaje(90, 420)]
    vista = Vista()
    # inicializando ...
    init_pygame(w, h, "BomberMan")
    init_opengl(w, h)

    # música de fondo
    pygame.mixer.music.load("musica/BomberMan.mid")
    pygame.mixer.music.play(-1, 0.0)
    #sonidos
    sonidoMuerte= pygame.mixer.Sound("musica/Gameover.wav")
    sonidoGana = pygame.mixer.Sound("musica/Victory.wav")
    sonido=True

    es = Escena(w, h)
    es.FijarMuros()

    CrearEnemigos(Personajes,es.MurosInternos)
    CrearMurosDestructibles(Personajes,es.MurosInternos,MurosDestructibles)
    Puerta=Salida(PosicionSalidaAleatoria(MurosDestructibles))
    PowerUpsAleatorios(PowerUps,MurosDestructibles)
    reloj=Reloj()
    run = True
    t = 0
    t0 = pygame.time.get_ticks()
    while run:
        t1 = pygame.time.get_ticks()  # tiempo actual
        dt = (t1 - t0)  # diferencial de tiempo asociado a la iteración
        t0 = t1  # actualizar tiempo inicial para siguiente iteración

        for event in pygame.event.get():
            # cerrar
            if event.type == QUIT:
                run = False

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    auxpersonaje = Personaje(Personajes[0].x+60,Personajes[0].y)
                    if PuedoPasar(auxpersonaje,Bombas,MurosDestructibles,es):
                        Personajes[0].x+=60
                elif event.key == K_LEFT:
                    auxpersonaje = Personaje(Personajes[0].x-60,Personajes[0].y)
                    if PuedoPasar(auxpersonaje, Bombas,MurosDestructibles,es):
                        Personajes[0].x-=60
                elif event.key == K_DOWN:
                    auxpersonaje = Personaje(Personajes[0].x,Personajes[0].y-50)
                    if PuedoPasar(auxpersonaje, Bombas, MurosDestructibles,es):
                        Personajes[0].y-=50
                elif event.key == K_UP:
                    auxpersonaje = Personaje(Personajes[0].x,50+Personajes[0].y)
                    if PuedoPasar(auxpersonaje, Bombas, MurosDestructibles,es):
                        Personajes[0].y+=50
                elif event.key == K_a:
                    if(Personajes[0].bombas>=1):
                        NuevaBomba=Bomba(Personajes[0].x,Personajes[0].y)
                        NuevaBomba.activada=True
                        Bombas.append(NuevaBomba)
                        Personajes[0].bombas -= 1

                # cerrara
                elif event.key == K_ESCAPE:
                    run = False
                elif event.key==K_SPACE:
                    main(sys.argv)


        t = t + dt
        vista.dibujar(Personajes,Bombas,MurosDestructibles,es,reloj,t,Puerta,PowerUps)
        if t>=1000:#tiempo sea un segundo
            reloj.Actualizar(1)
            MoverEnemigos(Personajes, Bombas, MurosDestructibles, es)
            t=0
        if not Personajes[0].amigo or reloj.tiempo==0:
            reloj.Actualizar(0)
            t=0
            if sonido:
                sonido=False
                pygame.mixer.music.stop()
                sonidoMuerte.play()
        elif Personajes[0].amigo :
            if Personajes[0].EncuentraSalida(Puerta):
                reloj.Actualizar(0)
                t=0
                if sonido:
                    sonido = False
                    pygame.mixer.music.stop()
                    sonidoGana.play()
        # pone el dibujo en la pantalla
        pygame.display.flip()
        # ajusta para trabajar a 30 fps.
        pygame.time.wait(int(1000/30))

    # termina pygame (cerrar ventana)
    pygame.quit()

if __name__ == "__main__":
    import sys
    main(sys.argv)

