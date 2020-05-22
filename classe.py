import pygame
import serial
from threading import Thread
from pygame.locals import *


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
        self.verouille = a


#################  THREAD POUR LA COMMUNICATION SERIE   #################

class Recevoir(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.data = None

    def run(self):
        nbSerialPort = str(input("Rentrez le numéro du port série : "))
        serialPort = 'COM'+nbSerialPort
        ser = serial.Serial(serialPort, 9600, timeout=3)
        var = True
        while var == True:
            self.data = str(ser.readline())
            self.data = self.data[2:-1]
            print("reçu : " + self.data)
            if self.data == "quit":
                print("connection fermé")
                var = False
