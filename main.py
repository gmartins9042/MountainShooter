import pygame  # Importando o pygame dentro desse arquivo

print('Setup Start')
pygame.init()  # Está inicializando
window = pygame.display.set_mode(size=(600, 480))  # Está abrindo uma janela no jogo
print('Setup Finish')

print('Loop start')
while True:  # Loop no qual vai continuar rodando
    # Check for all events
    for event in pygame.event.get():  # Toda interação está indo para a variável event
        if event.type == pygame.QUIT: # Se o event trazer uma variável tipo ele ira encerrar o game
            pygame.quit() # Close window
            quit() # End pygame
