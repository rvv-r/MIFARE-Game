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

############### PORTIQUE METRO #################

class Portique:
    def __init__(self, imageOuverte, imageFerme, a):
        self.imageOuverte = pygame.image.load(imageOuverte)
        self.imageFerme = pygame.image.load(imageFerme)
        self.verouille = a #Variable permettant de gérer la porte ouverte ou non
        self.passage = 0

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
            self.indexNiveauPorte2 = self.data.find("01010101010101010101010101010101")
            self.indexNiveauPorte3 = self.data.find("02020202020202020202020202020202")
            self.indexNiveauPorte4 = self.data.find("03030303030303030303030303030303")
            self.indexNiveauHotel2 = self.data.find("243")
            self.indexNiveauHotel3 = self.data.find("23041998")
            self.baliseSolde = self.data.find("B")
            self.baliseSolde2 = self.data.find("A")
            self.soldeInsuffisant = self.data.find("insuffisant")
            if self.baliseSolde >= 0:
                self.soldeAvant = traitement(self.data, "B", "Y")
                print(self.soldeAvant)
            if self.baliseSolde2 >= 0:
                self.soldeApres = traitement(self.data, "A", "Z")
                print(self.soldeApres)
            print(self.data)

    def envoieSerialDistributeurCoca(self):
        self.ser.write(str.encode("h"))
        self.ser.write(str.encode("h"))

    def envoieSerialDistributeurEvian(self):
        self.ser.write(str.encode("i"))
        self.ser.write(str.encode("i"))

    def envoieSerialDistributeurSprite(self):
        self.ser.write(str.encode("j"))
        self.ser.write(str.encode("j"))

    def envoieSerialDistributeurIceTea(self):
        self.ser.write(str.encode("k"))
        self.ser.write(str.encode("k"))

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


