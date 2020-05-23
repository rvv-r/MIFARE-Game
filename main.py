import pygame
import serial
import tkinter as tk
from PIL import Image, ImageTk
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
                        thread_1.var = False

############ Création du thread #############################

thread_1 = Recevoir()

############## Fonction pour gérer les bouton tkinter ###############

def Start():
    app.destroy()
    thread_1.start()
    selecteurNiveau()

def fctderoulant1(*args):
    if variable.get() == "0":
        thread_1.nbSerialPort = "0"
    if variable.get() == "1":
        thread_1.nbSerialPort = "1"
    if variable.get() == "2":
        thread_1.nbSerialPort = "2"
    if variable.get() == "3":
        thread_1.nbSerialPort = "3"
    if variable.get() == "4":
        thread_1.nbSerialPort = "4" 

def fctderoulant2(*args):
    if variable2.get() == "Windows":
        thread_1.environnementSerial = "COM"
        print(thread_1.environnementSerial)
    if variable2.get() == "Linux":
        thread_1.environnementSerial = "/dev/ttyS"
        print(thread_1.environnementSerial)


#################  FENETRE TKINTER  #########################

OptionList = ["Numéro du port","0","1","2","3","4"] 
OptionList2 = ["Système","Windows", "Linux"]

app = tk.Tk()

app.geometry('1000x631')

"""image = PhotoImage(file="imageConfig.jpg")
imagefond.create_image(0,0,anchor = tk.NW, image=image)
imagefond.pack()

imagefond = Canvas(app,width=image.size[0],height=image.size[1],bg='yellow',bd=8,relief="ridge")
"""


## Ecriture en haut ##

labelTest = tk.Label(text="Configuration Hack This Mifare", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

## Menu déroulant 1 ##

variable = tk.StringVar(app)
variable.set(OptionList[0])
opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=15, font=('Helvetica', 12))
opt.pack(side="bottom")
variable.trace("w", fctderoulant1) #application de la fonction pour le menu déroulant 1

## Menu déroulant 2 ##

variable2 = tk.StringVar(app)
variable2.set(OptionList2[0])
opt2 = tk.OptionMenu(app, variable2, *OptionList2)
opt2.config(width=15, font=('Helvetica', 12))
opt2.pack(side="bottom")
variable2.trace("w", fctderoulant2) #application de la fonction pour le menu déroulant 2

## Bouton Quitter ##

bouton_quitter = Button(app, text="Quitter", command=quit, width=15)  #Bouton quitter
bouton_quitter.pack(side='left')

## Bouton Start ##

bouton_start = Button(app, text="Start", command=Start, width=15)   #Bouton Start
bouton_start.pack(side='right')

######################  LANCEMENT DU JEU  ################################

app.mainloop()
