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


############   OBJETS DU DISTRIBUTEUR    #####################

class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def updateStock(self, stock):
        self.stock = stock

    def buyFromStock(self):
        if self.stock == 0:
            # raise not item exception
            pass
        self.stock -= 1

############   SOLDE DU CLIENT    ##################### (en attendant d'avoir la carte)

class Solde:
    def __init__(self):
        self.amount = -1

############### Portique metro #################

class Portique:
    def __init__(self, imageOuverte, imageFerme, a):
        self.imageOuverte = pygame.image.load(imageOuverte)
        self.imageFerme = pygame.image.load(imageFerme)
        self.verouille = a #Variable permettant de gérer la porte ouverte ou non
        self.passage = 0

############   DISTRIBUTEUR    #####################

class Distributeur:
    def __init__(self):
        self.items = []
        self.solde = Solde().amount

    def addItem(self, item):
        self.items.append(item)

    def containsItem(self, wanted):
        ret = False
        for item in self.items:
            if item.name == wanted:
                ret = True
                break
        return ret

    def getItem(self, wanted):
        ret = None
        for item in self.items:
            if item.name == wanted:
                ret = item
                break
        return ret

############## PANNEAU DE NIVEAU DANS SELECTEUR DE NIVEAU #####################

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
        self.environnementSerial = ""  #'COM' pour windows, '/dev/pts/' pour Linux
        self.var = True             #Variable qui permettra d'arrêter le thread
        self.indexNiveau1 = -1

    def run(self):
        serialPort = self.environnementSerial+self.nbSerialPort 
        ser = serial.Serial(serialPort, 9600, timeout=3) #ouverture du port série sur python
        while self.var == True:
            self.data = str(ser.readline()) #lit les données envoie sur le port série
            self.data = self.data[2:-1]  #on recoit b'message' permet d'avoir juste message
            self.indexNiveau1 = self.data.find("09CDF05D")
            if self.data == "quit": # si on reçoit quit ferme la connection
                print("connection fermé")
                self.var = False

def texte(Texte, Police, Taille, Couleur):
    police = pygame.font.SysFont(Police, Taille)
    text = police.render(Texte, True, pygame.Color(Couleur))
    return(text)