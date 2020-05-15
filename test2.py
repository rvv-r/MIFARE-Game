import pygame
import time
from pygame.locals import *
from classe import *
pygame.init()
pygame.display.set_caption("Hack this Mifare")



############ Boucle des niveaux  #####################


def selecteurNiveau():



####### CREATION DES FONDS ############################

        fenetre_niveau1 = Terrain("mur.jpg")
        fenetre_niveau2 = Terrain("mur2.jpg")
        fenetre_gameover = Terrain("Gameover.png")


####### CREATION DE LA PORTE #########################

        porte = Porte("porteOuverte2.jpg","porteFerme2.jpg",1)
        porte2 = Porte("porteOuverte2.jpg","porteFerme2.jpg",1)
        
        
####### Création de la fenêtre ########################
    
        fenetre = pygame.display.set_mode((800, 530), pygame.RESIZABLE)
        pygame.key.set_repeat(10, 30)

########## SELECTION DES NIVEAUX #######################

        niveau1 = True
        niveau2 = False

        while niveau1 == True:
            fenetre.blit(fenetre_niveau1.fond,(0,0))
            clock = pygame.time.Clock()
            clock.tick(30)
            pygame.display.update()
            pygame.display.flip()
            if porte.verouille == 1:
                fenetre.blit(porte.imageFerme, (350,175))
                pygame.display.flip()
            if porte.verouille == 0:
                fenetre.blit(porte.imageOuverte, (350,150))
                pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        print("bravo la porte est ouverte")
                        porte.verouille = 0
                    if event.key == pygame.K_c and porte.verouille == 0:
                        niveau1 = False
                        niveau2 = True
                    if event.key == pygame.K_a: #qwerty de base il faut appuyer sur q pour un azerty
                        niveau1 = False
                        pygame.quit()


        while niveau2 == True:
            fenetre.blit(fenetre_niveau2.fond,(0,0))
            clock = pygame.time.Clock()
            clock.tick(30)
            pygame.display.update()
            pygame.display.flip()
            if porte2.verouille == 1:
                fenetre.blit(porte2.imageFerme, (350,175))
                pygame.display.flip()
            if porte2.verouille == 0:
                fenetre.blit(porte2.imageOuverte, (350,150))
                pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:    #code a remplacé popur la detection de carte
                    if event.key == pygame.K_p :    
                        print("bravo la porte est ouverte")
                        porte2.verouille = 0
                    if event.key == pygame.K_a: #qwerty de base il faut appuyer sur q pour un azerty
                        niveau2 = False
                        pygame.quit()


        

selecteurNiveau()
                
            
