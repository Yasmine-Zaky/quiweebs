import pygame # On import la biblioteque

pygame.init() # Initialiser les composants

# On peut aussi ajouter les dimensions de l'ecran de l'ordinateur
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Permet de lancer une fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # ((0, 0)) pour le pleine écran
# On donne le nom a la fenêtre
pygame.display.set_caption('Quiweebs') # ('Quiweebs', icontitle=None)

running = True # Variable pour ne pas fermer la page

while running: # Boucle while pour que la fenêtre reste ouverte, elle s'arrête quand l'utilisateur ferme la page
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False




pygame.quit()
# Le programme s'arrête si on ferme la page grâce à la boucle while running: au dessus