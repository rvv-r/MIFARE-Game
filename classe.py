#####################################################################
#Auteur : Florian Neuville, Jean-Laurent Rouvière Hesse, Dan Nacache#
#####################################################################

import pygame
import serial
from threading import Thread
from pygame.locals import *
from tkinter import * 

################################################################################### CLASSES DU JEU EN LUI-MÊME ##################################################################################################

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

################################################################################### CLASSES LIÉES AU DISTRIBUTEUR  ##################################################################################################

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

############   DISTRIBUTEUR    #####################

class Distributeur:
    def __init__(self):
        self.items = []
        self.solde = Solde().amount
        self.compteur = 0

    def addcompteur(self):
        self.compteur += 1

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

################################################################################### CLASSE POUR LA COMMUNICATION SÉRIE #################################################################################################

class Recevoir(Thread):

    #constructeur
    def __init__(self):
        Thread.__init__(self)
        self.data = None         # Données reçues par le port série
        self.nbSerialPort = ""   # permet la configuration du numéro de port
        self.environnementSerial = ""  #'COM' pour windows, '/dev/pts/' pour Linux
        self.var = True             #Variable qui permettra d'arrêter le thread
        self.soldeAvant = 0
        self.soldeApres = 0


        self.indexNiveauPorte1 = -1
        self.indexNiveauPorte2 = -1
        self.indexNiveauPorte3 = -1
        self.indexNiveauPorte4 = -1
        self.indexNiveauHotel1_1 = -1
        self.indexNiveauHotel1_2 = -1
        self.indexNiveauHotel1_3 = -1
        self.indexNiveauHotel2 = -1
        self.indexNiveauHotel3 = -1
        self.baliseSolde = -1
        self.baliseSolde2 = -1
        self.soldeInsuffisant = -1
        self.insuffisant = 1
        self.carteNonPresente = -1
        self.obtenuCoca = -1
        self.obtenuEvian = -1
        self.obtenuSprite = -1
        self.obtenuIceTea = -1
        self.obtenuBoisson = 0

        self.choixNiveauSerial = ""
        self.ser = None

    def run(self):
        serialPort = self.environnementSerial+self.nbSerialPort 
        self.ser = serial.Serial(serialPort, 9600, timeout=3) #ouverture du port série sur python
        while self.var == True:
            lineb = str.encode(self.choixNiveauSerial)
            self.ser.write(lineb)
            self.data = str(self.ser.readline()) #lit les données envoie sur le port série
            self.data = self.data[2:-1]  #on recoit b'message' permet d'avoir juste message
            self.indexNiveauPorte1 = self.data.find("09CDF05D")
            self.indexNiveauPorte2 = self.data.find("726574726F506F72746532")
            self.indexNiveauPorte3 = self.data.find("726574726F506F72746533")
            self.indexNiveauPorte4 = self.data.find("726574726F506F72746534")
            self.indexNiveauHotel2 = self.data.find("243")
            self.indexNiveauHotel3 = self.data.find("23041998")
            self.baliseSolde = self.data.find("A")
            self.baliseSolde2 = self.data.find("E")
            self.soldeInsuffisant = self.data.find("insuffisant")
            self.carteNonPresente = self.data.find("non")
            self.obtenuCoca = self.data.find("Coca")
            self.obtenuEvian = self.data.find("evian")
            self.obtenuSprite = self.data.find("Sprite")
            self.obtenuIceTea = self.data.find("Ice")
            self.indexNiveauHotel1_1 = self.data.find("Suivant")
            self.indexNiveauHotel1_2 = self.data.find("Suivant")
            self.indexNiveauHotel1_3 = self.data.find("Suivant")

            if self.obtenuCoca >= 0 or self.obtenuEvian >= 0 or self.obtenuSprite >= 0 or self.obtenuIceTea >= 0 :
                self.obtenuBoisson = 1
            if self.soldeInsuffisant == 0:
                self.insuffisant = 1
            if self.baliseSolde >= 0:
                self.soldeAvant = traitement(self.data, "A", "B")
                #print("solde avant : " + self.soldeAvant)
            if self.baliseSolde2 >= 0:
                self.soldeApres = traitement(self.data, "E", "F")
                #print("solde après : " + self.soldeApres)
            print(self.data)

    def envoieSerialDistributeur1Coca(self):
        self.ser.write(str.encode("h"))
        self.ser.write(str.encode("h"))

    def envoieSerialDistributeur1Evian(self):
        self.ser.write(str.encode("i"))
        self.ser.write(str.encode("i"))

    def envoieSerialDistributeur1Sprite(self):
        self.ser.write(str.encode("j"))
        self.ser.write(str.encode("j"))

    def envoieSerialDistributeur1IceTea(self):
        self.ser.write(str.encode("k"))
        self.ser.write(str.encode("k"))
    
    def envoieSerialDistributeur3Coca(self):
        self.ser.write(str.encode("p"))
        self.ser.write(str.encode("p"))

    def envoieSerialDistributeur3Evian(self):
        self.ser.write(str.encode("q"))
        self.ser.write(str.encode("q"))

    def envoieSerialDistributeur3Sprite(self):
        self.ser.write(str.encode("r"))
        self.ser.write(str.encode("r"))

    def envoieSerialDistributeur3IceTea(self):
        self.ser.write(str.encode("s"))
        self.ser.write(str.encode("s"))

def texte(Texte, Police, Taille, Couleur):
    police = pygame.font.SysFont(Police, Taille)
    text = police.render(Texte, True, pygame.Color(Couleur))
    return(text)

def traitement(texte, balise1, balise2):
    texter = texte
    i = 0
    j = 0
    for k in range(len(texter)):
        if str(texter[k]) == balise1:
            i = k+1
        if str(texter[k]) == balise2:
            j = k
            break
    return(texter[i:j])


