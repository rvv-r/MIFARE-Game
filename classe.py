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

#Classe permettant de charger l'arrière plan d'une scène
class Terrain:
    #constructeur
    def __init__(self, fond):
        self.fond = pygame.image.load(fond)


#############    PORTE       ####################

#Classe permettant de créer un objet porte qui peut être ouvert ou fermé
class Porte:
    #constructeur
    def __init__(self,imageOuverte, imageFerme,a):
        self.imageOuverte = pygame.image.load(imageOuverte)
        self.imageFerme = pygame.image.load(imageFerme)
        self.verouille = a #Variable permettant de gérer la porte ouverte ou non

############  BOUTON      #####################

#Classe permettant d'interagir grâce à des boutons
class Bouton:
    def __init__(self, imageBouton, imageHoover, imageSelect):
        self.imageLoad = pygame.image.load(imageBouton) #image courante
        self.imageHoover = imageHoover #image de survol
        self.imageSelect = imageSelect #image quand il est selectionné
        self.imageBouton = imageBouton #image du bouton sans action
        self.etat = False #essaie de voir si on peut bloquer l'image select avec cette variable
    
    #fonction qui défini l'image courante avec celle du survol
    def hoover(self):
        self.imageLoad = pygame.image.load(self.imageHoover)
    
    #fonction qui défini l'image courante avec celle selectionné
    def select(self):
        self.imageLoad = pygame.image.load(self.imageSelect)
    
    #fonction qui défini l'image courante avec celle de base sans action
    def reinit(self):
        self.imageLoad = pygame.image.load(self.imageBouton)


############## PANNEAU DE NIVEAU DANS SELECTEUR DE NIVEAU #####################

#Classe permettant d'afficher ou non un panneau dans la fenêtre
class PanneauNiveau:
    def __init__(self,imageVide, imagePanneau):
        self.imageLoad = pygame.image.load(imageVide) #image courante
        self.imageVide = imageVide #une image d'un seul pixel donnant l'illusion que le panneau a disparu
        self.imagePanneau = imagePanneau #image du panneau
    
    #fonction qui défini l'image courante avec celle du panneau
    def affichePanneau(self):
        self.imageLoad = pygame.image.load(self.imagePanneau)
    
    #fonction qui défini l'image courante comme celle d'un seul pixel
    def reinitPanneau(self):
        self.imageLoad = pygame.image.load(self.imageVide)

################################################################################### CLASSES LIÉES AU DISTRIBUTEUR  ##################################################################################################

############   OBJETS DU DISTRIBUTEUR    #####################

class Item:
    #constructeur
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price #prix de l'item
        self.stock = stock #nombre de cet item dans le stock

    def updateStock(self, stock):
        self.stock = stock

    def buyFromStock(self):
        if self.stock == 0:
            # raise not item exception
            pass
        self.stock -= 1

############   DISTRIBUTEUR    #####################

class Distributeur:
    #constructeur
    def __init__(self):
        self.items = []
        self.compteur = 0

    #fonction permettant d'ajouté 1 au compteur permmettant la condition de victoire dans les niveaux des distributeurs
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

#Classe permettant de gérer un thread qui ici servira à la communication série en parralèle du jeu sous pygame
class Recevoir(Thread):
    #constructeur
    def __init__(self):
        Thread.__init__(self)    #superconstruction de la classe Thread
        self.data = None         # Données reçues par le port série
        self.nbSerialPort = ""   # permet la configuration du numéro de port
        self.environnementSerial = ""  #'COM' pour windows, '/dev/pts/' pour Linux
        self.var = True             #Variable qui permettra d'arrêter le thread
        self.soldeAvant = 0      #défini le solde avant le paiement pour les distributeur
        self.soldeApres = 0      #défini le solde après le paiement pour les distributeur

        #Les index, balises, etc, sont en liens avec les self.data.find qui incrémente de 1 si la valeur est trouvé dans une string

        #L'index de chaque niveau est la data (le secret) permetant de passer le niveau. -1 quand c'est faux 0 ou plus quand c'est trouvé.
        self.indexNiveauPorte1 = -1
        self.indexNiveauPorte2 = -1
        self.indexNiveauPorte3 = -1
        self.indexNiveauPorte4 = -1
        self.indexNiveauHotel1_1 = -1
        self.indexNiveauHotel1_2 = -1
        self.indexNiveauHotel1_3 = -1
        self.indexNiveauHotel2 = -1
        self.indexNiveauHotel3 = -1
        self.indexMetro = -1
        self.compteurMetro = 0

        #Solde pour le distributeur envoyé sous la forme ASoldeB, ici la balise retourne 0 quand il trouve un A dans une string
        self.baliseSolde = -1 
        self.baliseSolde2 = -1

        #gère le solde insuffisant
        self.soldeInsuffisant = -1
        self.insuffisant = -1

        #Pour vérifier si le badge est manquant
        self.carteNonPresente = -1

        #Permet de gérer si l'on a bien reçu une boisson
        self.obtenuCoca = -1
        self.obtenuEvian = -1
        self.obtenuSprite = -1
        self.obtenuIceTea = -1
        self.obtenuBoisson = 0

        #Pour pemettre de choix la lettre a envoyer à l'arduino, c'est celle la qui determinera le niveau dans lequel on se trouve
        self.choixNiveauSerial = ""
        self.ser = None

    def run(self):
        #initialisation de la communication série
        serialPort = self.environnementSerial+self.nbSerialPort 
        self.ser = serial.Serial(serialPort, 9600, timeout=3) #ouverture du port série sur python
        while self.var == True:
            #échange avec la liaison série (écriture et lecture)
            lineb = str.encode(self.choixNiveauSerial)
            self.ser.write(lineb)
            self.data = str(self.ser.readline()) #lit les données envoie sur le port série
            self.data = self.data[2:-1]  #on recoit b'message' permet d'avoir juste message*
            #toutes les valeurs d'index en lien avec les secret dans la data des badge mifare 
            self.indexNiveauPorte1 = self.data.find("09CDF05D")
            self.indexNiveauPorte2 = self.data.find("726574726F506F72746532")
            self.indexNiveauPorte3 = self.data.find("726574726F506F72746533")
            self.indexNiveauPorte4 = self.data.find("726574726F506F72746534")
            self.indexNiveauHotel2 = self.data.find("243")
            self.indexNiveauHotel3 = self.data.find("23041998")
            #balise permettant de savoir de quelle solde on parle
            self.baliseSolde = self.data.find("A")
            self.baliseSolde2 = self.data.find("E")
            #Pour savoir si le solde est insuffisant ou non 
            self.soldeInsuffisant = self.data.find("insuffisant")
            #L'arduino envoie non si la carte n'est pas présente
            self.carteNonPresente = self.data.find("non")
            #Vérification de la boisson obtenu
            self.obtenuCoca = self.data.find("Coca")
            self.obtenuEvian = self.data.find("evian")
            self.obtenuSprite = self.data.find("Sprite")
            self.obtenuIceTea = self.data.find("Ice")
            #Permet de savoir si on peut passer sur le portique de metro
            self.indexNiveauHotel1_1 = self.data.find("Suivant")
            self.indexNiveauHotel1_2 = self.data.find("Suivant")
            self.indexNiveauHotel1_3 = self.data.find("Suivant")
            self.indexMetro = self.data.find("ok")
            
            
            #Condition pour réunir sous une seule variable si la boisson a été obtenu ou non
            if self.obtenuCoca >= 0 or self.obtenuEvian >= 0 or self.obtenuSprite >= 0 or self.obtenuIceTea >= 0 :
                self.obtenuBoisson = 1

            if self.indexMetro >= 0 and self.compteurMetro < 1:
                self.ser.write(str.encode("e"))
                self.ser.write(str.encode("e"))
                self.compteurMetro += 1
                

            #Permet d'avoir le solde insuffisant d'être affiché une seule fois
            if self.soldeInsuffisant == 0:
                self.insuffisant = 1
            #Permet d'identifier si le début de la balise est présente puis la fonctionne récupère uniquement ce qui a entre les deux balises
            if self.baliseSolde >= 0:
                self.soldeAvant = traitement(self.data, "A", "B")
            if self.baliseSolde2 >= 0:
                self.soldeApres = traitement(self.data, "E", "F")
            print(self.data)

    #En lien avec les boutons du distributeur il permette d'envoie sur le port serial la lettre en fonction du niveau au quel on se trouve.
    def envoieSerialDistributeur1Coca(self):
        self.ser.write(str.encode("h"))
        self.ser.write(str.encode("h"))#on envoie 2 lettre car l'arduino fonctionne exactement une fois sur 2

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
    
    

#fonction permettant d'automatiser la création de texte dans pygame
def texte(Texte, Police, Taille, Couleur):
    police = pygame.font.SysFont(Police, Taille)
    text = police.render(Texte, True, pygame.Color(Couleur))
    return(text)

#fonction permettant de récuperer du texte entre 2 balises
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


