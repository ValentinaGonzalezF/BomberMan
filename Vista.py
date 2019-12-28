# -*- coding: iso-8859-1 -*-


from OpenGL.GL import *
from Funciones import *
import pygame

class Vista:
    def dibujar(self,Personajes,Bombas,MurosDestructible,Escena,reloj,t,puerta,PowerUps): #Escena falta
        # limpia la pantalla
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # dibujar
        Escena.dibujar()
        reloj.Actualizar(0)
        # itera los personajes
        if len(Personajes)>1:
            for i in range(1,len(Personajes)):
                if estanChocando(Personajes[0],Personajes[i]):
                    Personajes[0].vivo=False


        # itera los muros destructibles
        for M in MurosDestructible:
            M.dibujar()

        for Pw in PowerUps:
            if Personajes[0].amigo:
                if estanChocando(Personajes[0],Pw):
                    Pw.recogido = True

                    if Pw.power == "VidaExtra" and not Pw.activado:
                        Personajes[0].vida =2
                        Pw.activado = True
                    elif Pw.power=="BombaExtra" and not Pw.activado:
                        Personajes[0].bombas+=1
                        Pw.activado=True

                if not Pw.recogido and Pw.dibujar:
                    if Pw.power=="BombaExtra":
                        Pw.dibujarBombaExtra()

                    elif Pw.power=="VidaExtra":
                        Pw.dibujarVidaExtra()
            if not MuroPw(MurosDestructible,Pw):
                Pw.dibujar=True

        if not SeEncuentraMuroConSalida(MurosDestructible):
            puerta.dibujar(16)

        for B in Bombas:
            B.dibujar()

            if B.activada:
                if t>=1000:
                    B.tictac()

            if B.tiempo<=0:
                B.explosionCostados("Izquierda",Bombas,Escena.Muros,MurosDestructible,Personajes,PowerUps)
                B.explosionCostados("Derecha", Bombas, Escena.Muros,MurosDestructible, Personajes,PowerUps)
                B.explosionCostados("Arriba", Bombas,Escena.Muros,MurosDestructible, Personajes,PowerUps)
                B.explosionCostados("Abajo", Bombas,Escena.Muros,MurosDestructible, Personajes,PowerUps)
                B.explosionCentral(8)

        #Dibujo
        for P in Personajes:
            if P.vivo:
                P.dibujar(16)

        if not Personajes[0].amigo or reloj.tiempo==0:
            printText('GAME OVER',[100,250],300)

        elif Personajes[0].amigo:
            if Personajes[0].EncuentraSalida(puerta):
                printText('VICTORY',[150,250],300)

        # eliminar objetos
        limpiar(Bombas)
        limpiar(MurosDestructible)
        limpiar(Personajes)
        limpiar(PowerUps)
        glLoadIdentity()