import pygame
import serial
import tkinter as tk
from threading import Thread
from pygame.locals import *
from classe import *

pygame.init()
pygame.display.set_caption("Hack this Mifare")


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

################ BOUCLE DES NIVEAUX #######################
        niveau1 = bool1
        niveau2 = bool2

        while niveau1 == True:
            thread_1.data = ""
            fenetre.blit(fenetre_niveau1.fond,(0,0))
            clock = pygame.time.Clock()
            clock.tick(60)
            pygame.display.update()
            if porte.verouille == 1:
                fenetre.blit(porte.imageFerme, (0,0))
                pygame.display.flip()
            if porte.verouille == 0:
                fenetre.blit(porte.imageOuverte, (0,0))
                pygame.display.flip()
            if thread_1.data == "ouvre": #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
                porte.verouille = 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:    #ancien code qui ouvrait la porte avec p
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
            thread_1.data = ""
            fenetre.blit(fenetre_niveau2.fond,(0,0))
            clock = pygame.time.Clock()
            clock.tick(60)
            pygame.display.update()
            if porte2.verouille == 1:
                fenetre.blit(porte2.imageFerme, (400,310))
                pygame.display.flip()
            if porte2.verouille == 0:
                fenetre.blit(porte2.imageOuverte, (400,310))
                pygame.display.flip()
            if thread_1.data == "ouvre": #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
                porte2.verouille = 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_p:    #ancien code qui ouvrait la porte avec p
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

############ Création du thread #############################

thread_1 = Recevoir()

############## Fonction pour gérer les bouton tkinter ###############

def Start():
    thread_1.start()
    selecteurNiveau()



def callback(*args):
    if variable.get() == "1":
        thread_1.nbSerialPort = "1"
        print(thread_1.nbSerialPort)
    if variable.get() == "2":
        thread_1.nbSerialPort = "2"
    if variable.get() == "3":
        thread_1.nbSerialPort = "3"
    if variable.get() == "4":
        thread_1.nbSerialPort = "4" 


#################  FENETRE TKINTER  #########################

OptionList = ["1","2","3","4"] 

app = tk.Tk()

app.geometry('300x200')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=10, font=('Helvetica', 12))
opt.pack(side="bottom")

labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red') #Menu déroulant
labelTest.pack(side="top")

variable.trace("w", callback) #application de la fonction pour le menu déroulant

bouton_quitter = Button(app, text="Quitter", command=quit)  #Bouton quitter
bouton_quitter.pack(side='left')

bouton_start = Button(app, text="Start", command=Start)   #Bouton Start
bouton_start.pack(side='right')



app.mainloop()
# Attend que les threads se terminent