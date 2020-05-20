import serial
from threading import Thread, RLock
import sys
import pygame
import time
from pygame.locals import *
from classe import *
pygame.init()
pygame.display.set_caption("Hack this Mifare")


############ Définition du Thread #############################

class Jeu(Thread):

    def __init__(self):
            Thread.__init__(self)


    def run(self):
    
############ Fonctions de la boucle des niveaux  #####################


        def bouclePrincipale(bool1, bool2):



####### CREATION DES FONDS ############################

            fenetre_niveau1 = Terrain("scene.jpg")
            fenetre_niveau2 = Terrain("mur2.jpg")
            #fenetre_gameover = Terrain("Gameover.png")


####### CREATION DE LA PORTE #########################

            porte = Porte("porteOuverte.png","porteFerme.png",1)
            porte2 = Porte("porteOuverte2.jpg","porteFerme2.jpg",1)
        
        
####### Création de la fenêtre ########################
    
            fenetre = pygame.display.set_mode((1000, 661), pygame.RESIZABLE)
            pygame.key.set_repeat(10, 30)

            niveau1 = bool1
            niveau2 = bool2
################ BOUCLE DES NIVEAUX #######################

            while niveau1 == True:
                fenetre.blit(fenetre_niveau1.fond,(0,0))
                clock = pygame.time.Clock()
                clock.tick(30)
                pygame.display.update()
                pygame.display.flip()
                if porte.verouille == 1:
                    fenetre.blit(porte.imageFerme, (0,0))
                    pygame.display.flip()
                if porte.verouille == 0:
                    fenetre.blit(porte.imageOuverte, (0,0))
                    pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p: #ouvre la porte (code a remplacé popur la detection de carte)
                            print("bravo la porte est ouverte")
                            porte.verouille = 0
                        if event.key == pygame.K_c and porte.verouille == 0:  #Permet de continuer seulement si la porte a été ouverte
                            niveau1 = False
                            niveau2 = True
                        if event.key == pygame.K_r :  #Retourne à la selection de niveau
                            selecteurNiveau()
                            niveau1 = False
                            niveau2 = False
                        if event.key == pygame.K_a: #qwerty de base il faut appuyer sur q pour un azerty Permet de quitter
                            niveau1 = False
                            pygame.quit()


            while niveau2 == True:
                fenetre.blit(fenetre_niveau2.fond,(0,0))
                clock = pygame.time.Clock()
                clock.tick(30)
                pygame.display.update()
                pygame.display.flip()
                if porte2.verouille == 1:
                    fenetre.blit(porte2.imageFerme, (400,310))
                    pygame.display.flip()
                if porte2.verouille == 0:
                    fenetre.blit(porte2.imageOuverte, (400,310))
                    pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:    #ouvre la porte (code a remplacé popur la detection de carte)
                        if event.key == pygame.K_p :    
                            print("bravo la porte est ouverte")
                            porte2.verouille = 0
                        if event.key == pygame.K_c and porte2.verouille == 0 : #Permet de continuer seulement si la porte a été ouverte
                            selecteurNiveau() #Comme c'est le dernier niveau on retombe sur la sélection de menu """""""A CHANGER SI CE N'EST PLUS LE DERNIER NIVEAU"""""""""
                            niveau1 = False
                            niveau2 = False
                        if event.key == pygame.K_r :  #Retourne à la selection de niveau
                            selecteurNiveau()
                            niveau1 = False
                            niveau2 = False
                        if event.key == pygame.K_a: #qwerty de base il faut appuyer sur q pour un azerty
                            niveau2 = False
                            pygame.quit()


############ Fonction menu principale selection des niveaux  #############################


            def selecteurNiveau(): #Premiere interface qui permet de selectionner les niveaux
                gameStart = True

                while gameStart == True:
                    fenetre = pygame.display.set_mode((1000, 661), pygame.RESIZABLE)
                    fenetre_selection = Terrain("selection.png")
                    fenetre.blit(fenetre_selection.fond,(0,0))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:    
                                if event.key == pygame.K_1 : #On appuie sur 1(&) pour choisir le niveau 1
                                    bouclePrincipale(True,False)
                                    gameStart = False
                                if event.key == pygame.K_2: #On appuie sur 2(é) pour choisir le niveau 2
                                    bouclePrincipale(False,True)
                                    gameStart = False
                                if event.key == pygame.K_a: #q en azerty pour quitter
                                    gameStart = False
                                    pygame.quit() 


            selecteurNiveau()


############ Définition du Thread #############################

class Recevoir(Thread):
    
    def __init__(self):
        Thread.__init__(self)

        nbSerialPort = str(input("Rentrez le numéro du port série : "))
        serialPort = 'COM'+nbSerialPort
        ser = 0
        

        def init_serial(numeroPort):
            global var
            global ser
            ser = serial.Serial()
            ser.baudrate = 9600
            ser.port = 'COM'+numeroPort
            ser.timeout = 3
            ser.open()

            if ser.isOpen():
                print('Open : ' + ser.portstr)
            
        init_serial(nbSerialPort)

    def run(self):
        
        var = True
        while var == True:
            data = str(ser.readline())
            data = data[2:-1]
            print("reçu : " + data)
            if data == "quit":
                print("connection fermé")
                var = False

# Création des threads
thread_1 = Recevoir()
thread_2 = Jeu()

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent