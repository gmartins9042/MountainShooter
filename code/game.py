#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame  # Importando o pygame dentro desse arquivo

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # Está inicializando
        self.window = pygame.display.set_mode(size=(600, 480))  # Está abrindo uma janela no jogo

    def run(self):
        print('Setup Start')

        print('Setup Finish')

        print('Loop start')
        while True:  # Loop no qual vai continuar rodando

            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            #for event in pygame.event.get():  # Toda interação está indo para a variável event
                #if event.type == pygame.QUIT: # Se o event trazer uma variável tipo ele ira encerrar o game
                    #pygame.quit() # Close window
                    #quit() # End pygame
