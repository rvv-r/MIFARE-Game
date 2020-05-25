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

        fenetre_niveau1 = Terrain("image/scene.jpg")
        fenetre_niveau2 = Terrain("image/mur2.jpg")
        #fenetre_gameover = Terrain("Gameover.png")


####### CREATION DE LA PORTE #########################

        porte = Porte("image/porteOuverte.png","image/porteFerme.png",1)
        porte2 = Porte("image/porteOuverte2.jpg","image/porteFerme2.jpg",1)
        
        
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
                        thread_1.var = False


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
            if thread_1.data == "ouvre2": #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
                porte2.verouille = 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_p:    #ancien code qui ouvrait la porte avec p
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
                        thread_1.var = False


############ Fonction menu principale selection des niveaux  #############################


def selecteurNiveau(): #Premiere interface qui permet de selectionner les niveaux
    gameStart = True

    while gameStart == True:
        fenetre = pygame.display.set_mode((1000, 661), pygame.RESIZABLE)
        fenetre_selection = Terrain("image/selection.png")
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
    if variable2.get() == "Linux":
        thread_1.environnementSerial = "/dev/ttyS"

def fctderoulant3(*args):
    if variable3.get() == "0":
        #thread_1.nbSerialPort = "0"
        print("")
    if variable3.get() == "1":
        #thread_1.nbSerialPort = "1"
        print("")
    if variable3.get() == "2":
        #thread_1.nbSerialPort = "2"
        print("")
    if variable3.get() == "3":
        #thread_1.nbSerialPort = "3"
        print("")
    if variable3.get() == "4":
        #thread_1.nbSerialPort = "4" 
        print("")


#################  FENETRE TKINTER  #########################

OptionList = ["Numéro du port","0","1","2","3","4"] 
OptionList2 = ["Système","Windows", "Linux"]

app = tk.Tk()
app.title("Hack this Mifare Configuration")

app.geometry('866x631')

canvas = Canvas(app, width = 866, height = 380)
canvas.pack()

## Zone blanche ou sont positionner les boutons
zoneSelection = Frame(app, bg = 'white', width = 800, height = 200) 
zoneSelection.pack_propagate(0) #Evite que la frame ne s'adapte aux boutons
zoneSelection.pack()

imagefond = PhotoImage(file="image/imageConfig.gif")
canvas.create_image(0,0,anchor=NW, image=imagefond)


## Zone de texte ##

labelTest = tk.Label(zoneSelection, bg = 'white', text="Configuration", font=('Helvetica', 16), fg='black')
labelTest.pack(side="top")

texteDeroulant1 = tk.Label(zoneSelection, bg = 'white', text = "Système d'exploitation", font=('Helvetica', 11))
texteDeroulant1.place(x = 190 , y = 65)

texteDeroulant1 = tk.Label(zoneSelection, bg = 'white', text = "Numéro de port", font=('Helvetica', 11))
texteDeroulant1.place(x = 190 , y = 105)

texteDeroulant1 = tk.Label(zoneSelection, bg = 'white', text = "Numéro de port du lecteur", font=('Helvetica', 11))
texteDeroulant1.place(x = 190 , y = 145)

## Menu déroulant 1 ##

variable = tk.StringVar(app)
variable.set(OptionList[0])
opt = tk.OptionMenu(zoneSelection, variable, *OptionList)
opt.config(width=15, font=('Helvetica', 12))
opt.place(x = 400, y = 100)
variable.trace("w", fctderoulant1) #application de la fonction pour le menu déroulant 1

## Menu déroulant 2 ##

variable2 = tk.StringVar(app)
variable2.set(OptionList2[0])
opt2 = tk.OptionMenu(zoneSelection, variable2, *OptionList2)
opt2.config(width=15, font=('Helvetica', 12))
opt2.place(x = 400, y = 60)
variable2.trace("w", fctderoulant2) #application de la fonction pour le menu déroulant 2

## Menu déroulant 2 ##

variable3 = tk.StringVar(app)
variable3.set(OptionList[0])
opt3 = tk.OptionMenu(zoneSelection, variable3, *OptionList)
opt3.config(width=15, font=('Helvetica', 12))
opt3.place(x = 400, y = 140)
variable2.trace("w", fctderoulant3) #application de la fonction pour le menu déroulant 2


## Bouton Quitter ##

bouton_quitter = Button(app, text="Quit", command=quit, width=15)  #Bouton quitter
bouton_quitter.place(x = 600, y = 600)

## Bouton Start ##

bouton_start = Button(app, text="Start", command=Start, width=15)   #Bouton Start
bouton_start.place(x = 730, y = 600)

######################  LANCEMENT DU JEU  ################################

app.mainloop()
