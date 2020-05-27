import pygame
import serial
from threading import Thread
from pygame.locals import *
from tkinter import * 


##############     TERRAIN     #####################

class Terrain:
    #constructeur
    def __init__(self, fond):
        self.fond = pygame.image.load(fond)


#############    PORTE       ####################

class Porte:
    #constructeur
    def __init__(self,imageOuverte, imageFerme,a):
        self.imageOuverte = pygame.image.load(imageOuverte)
        self.imageFerme = pygame.image.load(imageFerme)
        self.verouille = a #Variable permettant de gérer la porte ouverte ou non

############  BOUTON      #####################

class Bouton:
    def __init__(self, imageBouton, imageHoover, imageSelect):
        self.imageLoad = pygame.image.load(imageBouton)
        self.imageHoover = imageHoover
        self.imageSelect = imageSelect
        self.imageBouton = imageBouton
        self.etat = False #essaie de voir si on peut bloquer l'image select avec cette variable
    
    def hoover(self):
        self.imageLoad = pygame.image.load(self.imageHoover)
    
    def select(self):
        self.imageLoad = pygame.image.load(self.imageSelect)
    
    def reinit(self):
        self.imageLoad = pygame.image.load(self.imageBouton)

class PanneauNiveau:
    def __init__(self,imageVide, imagePanneau):
        self.imageLoad = pygame.image.load(imageVide)
        self.imageVide = imageVide
        self.imagePanneau = imagePanneau
    
    def affichePanneau(self):
        self.imageLoad = pygame.image.load(self.imagePanneau)
    
    def reinitPanneau(self):
        self.imageLoad = pygame.image.load(self.imageVide)



#################  THREAD POUR LA COMMUNICATION SERIE   #################

class Recevoir(Thread):
    #constructeur
    def __init__(self):
        Thread.__init__(self)
        self.data = None         # Données reçues par le port série
        self.nbSerialPort = ""   # permet la configuration du numéro de port
        self.environnementSerial = ""  #'COM' pour windows, '/dev/ttyS' pour Linux
        self.var = True             #Variable qui permettra d'arrêter le thread

    def run(self):
        serialPort = self.environnementSerial+self.nbSerialPort 
        ser = serial.Serial(serialPort, 9600, timeout=3) #ouverture du port série sur python
        while self.var == True:
            self.data = str(ser.readline()) #lit les données envoie sur le port série
            self.data = self.data[2:-1]  #on recoit b'message' permet d'avoir juste message
            if self.data == "quit": # si on reçoit quit ferme la connection
                print("connection fermé")
                self.var = False