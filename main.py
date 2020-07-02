#####################################################################
#Auteur : Florian Neuville, Jean-Laurent Rouvière Hesse, Dan Nacache#
#####################################################################

import pygame
import serial
import tkinter as tk
import time
import sys
from tkinter import ttk
from threading import Thread
from pygame.locals import *
from classe import *

pygame.init()
pygame.display.set_caption("Hack this Mifare")



############ Fonctions de la boucle des niveaux  #####################


def bouclePrincipale(boolp1, boolp2, boolp3, boolp4, boold1, boold2, boold3, boolh1, boolh2, boolh3):


####### CREATION DES FONDS ############################


    fenetre_porteNiveau1 = Terrain("image/scene/scene.jpg")
    fenetre_porteNiveau2 = Terrain("image/scene/scene2.png")
    fenetre_porteNiveau3_1 = Terrain("image/scene/scenePorte3_1.jpg")
    fenetre_porteNiveau3_2 = Terrain("image/scene/scenePorte3_2.jpg")
    fenetre_porteNiveau4 = Terrain("image/scene/scenePorte4.jpg")
    fenetre_distribNiveau1 = Terrain("image/scene/sceneDistrib1.jpg")
    fenetre_distribNiveau2 = Terrain("image/scene/sceneDistrib1.jpg")
    fenetre_distribNiveau3 = Terrain("image/scene/sceneDistrib1.jpg")
    fenetre_hotelNiveau1_1 = Terrain("image/scene/sceneMetro1.jpg")
    fenetre_hotelNiveau1_2 = Terrain("image/scene/sceneMetro2.png")
    fenetre_hotelNiveau1_3 = Terrain("image/scene/sceneMetro3.jpg")
    fenetre_hotelNiveau2 = Terrain("image/scene/sceneHotel1.jpg")
    fenetre_hotelNiveau3 = Terrain("image/scene/sceneHotel1.jpg")

######## AUTRE IMAGE  ############################

    habitScientifique = pygame.image.load("image/habitScientifique.png")
    screen = pygame.image.load("image/screenDistrib1.jpg")


####### CREATION DES BOUTONS #####################

    #boutons interaction
    bouton_quitter = Bouton("image/boutons/boutonQuitter.png", "image/boutons/boutonQuitterHoover.png", "image/boutons/boutonQuitterSelect.png")
    bouton_continuer = Bouton("image/boutons/boutonContinuer.png", "image/boutons/boutonContinuerHoover.png", "image/boutons/boutonContinuer.png")
    bouton_retour = Bouton("image/boutons/boutonRetour2.png", "image/boutons/boutonRetourHoover2.png", "image/boutons/boutonRetour2.png")
    bouton_suivant = Bouton("image/boutons/boutonSuivant2.png", "image/boutons/boutonSuivant2Hoover.png", "image/boutons/boutonSuivant2.png")
    bouton_aide = Bouton("image/boutons/boutonAide2.png", "image/boutons/boutonAideHoover2.png", "image/boutons/boutonAide2.png")
    testAide = PanneauNiveau("image/presqueRien.png", "image/texteAide2.png")

    #bouton blouse niveau 3_1
    bouton_blouse = Bouton("image/boutons/boutonBlouse.png", "image/boutons/boutonBlouseHoover.png", "image/boutons/boutonBlouse.png")

    #bouton distributeur
    bouton_coca = Bouton("image/boutons/boutonCoca.png", "image/boutons/boutonCoca.png", "image/boutons/boutonCocaSelect.png")
    bouton_evian = Bouton("image/boutons/boutonEvian.png", "image/boutons/boutonEvian.png", "image/boutons/boutonEvianSelect.png")
    bouton_sprite = Bouton("image/boutons/boutonSprite.png", "image/boutons/boutonSprite.png", "image/boutons/boutonSpriteSelect.png")
    bouton_iceTea = Bouton("image/boutons/boutonIceTea.png", "image/boutons/boutonIceTea.png", "image/boutons/boutonIceTeaSelect.png")

######## CREATION DE LA POLICE D'ÉCRITURE #############

    police_aide = pygame.font.SysFont("arial", 20)

######## CREATION DU TEXTE DISTRIBUTEUR #############

    texte_bienvenue = texte("Bienvenue sur le distributeur !", None, 20, "#000000")
    texte_Cartes = texte("Veuillez poser votre carte", None, 20, "#000000")
    texte_Selection_Objets = texte("Sélectionnez une boisson", None, 20, "#000000")
    texte_Pas_Bras_Pas_De_Chocolat = texte("Solde insuffisant", None, 20, "#000000")
    texte_etoiles = texte("***************", None, 20, "#000000")

########### CREATION DU DISTRIBUTEUR #################

    distributeur1 = Distributeur()
    item1 = Item('Coca',  2,  2)
    item2 = Item('Evian', 1,  1)
    item3 = Item('Ice Tea',  1.5,  3)
    item4 = Item('Sprite',  2, 1)
    distributeur1.addItem(item1)
    distributeur1.addItem(item2)
    distributeur1.addItem(item3)
    distributeur1.addItem(item4)

    distributeur2 = Distributeur()
    distributeur2.addItem(item1)
    distributeur2.addItem(item2)
    distributeur2.addItem(item3)
    distributeur2.addItem(item4)

    distributeur3 = Distributeur()
    distributeur3.addItem(item1)
    distributeur3.addItem(item2)
    distributeur3.addItem(item3)
    distributeur3.addItem(item4)

####### CREATION DES PORTES #########################

    porteN1 = Porte("image/portes/porteOuverte.png","image/portes/porteFerme.png",1)
    porteN2 = Porte("image/portes/porteOuverte2.png","image/portes/porteFerme2.png",1)
    porteN3 = Porte("image/portes/porteOuverte3.png","image/portes/porteFerme3.png",1)
    porteN4 = Porte("image/portes/porteOuverte4.png","image/portes/porteFerme4.png",1)
    porteNH1_1 = Porte("image/portes/metroOuvert.png", "image/portes/metroFerme.png", 1)
    porteNH1_2 = Porte("image/portes/metroOuvert.png", "image/portes/metroFerme.png", 1)
    porteNH1_3 = Porte("image/portes/metroOuvert.png", "image/portes/metroFerme.png", 1)
    porteNH2 = Porte("image/portes/porteOuverteHotel1.png", "image/portes/porteFermeHotel1.png", 1)
    porteNH3 = Porte("image/portes/porteOuverteHotel1.png", "image/portes/porteFermeHotel1.png", 1)


####### Création de la fenêtre ########################

    fenetre = pygame.display.set_mode((1000, 661))
    pygame.key.set_repeat(10, 30)

############### BOOLEEN DE NIVEAU #######################

    porteNiveau1 = boolp1
    porteNiveau2 = boolp2
    porteNiveau3_1 = boolp3
    suivant3_1 = False
    porteNiveau3_2 = False
    porteNiveau4 = boolp4
    distributeurNiveau1 = boold1
    distributeurNiveau2 = boold2
    distributeurNiveau3 = boold3
    hotelNiveau1_1 = boolh1
    hotelNiveau1_2 = False
    hotelNiveau1_3 = False
    hotelNiveau2 = boolh2
    hotelNiveau3 = boolh3

    #booleen pour les aide dans chaques niveaux
    aideP1 = True
    aideP2 = True
    aideP3_1 = True
    aideP3 = True
    aideP4 = True
    aideD1 = True
    aideD2 = True
    aideD3 = True
    aideH1 = True
    aideH2 = True
    aideH3 = True

###################################### BOUCLE DES NIVEAUX ##################################################################


##################################################################################################
#                                                                                                #
#                                       Niveau 1 Porte                                           #
#                                                                                                #
##################################################################################################

    while porteNiveau1 == True:
        thread_1.choixNiveauSerial = "a"
        fenetre.blit(fenetre_porteNiveau1.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (30, -10))
        fenetre.blit(testAide.imageLoad, (60,200))

        if aideP1 == True:
            testAide.affichePanneau()
            fenetre.blit(police_aide.render("PORTE NIVEAU 1", True, (242, 200, 105)),(200, 230))
            fenetre.blit(police_aide.render("Apparemment, quelque chose se trame dans ", True, (242, 200, 105)),(100, 290))
            fenetre.blit(police_aide.render("cette ruelle. Vous vous trouvez devant une  ", True, (242, 200, 105)),(100, 320))
            fenetre.blit(police_aide.render("porte à laquelle vous n’avez pas accès.  ", True, (242, 200, 105)),(100, 350))
            fenetre.blit(police_aide.render("Un badge est encastré dans le mur et  ", True, (242, 200, 105)),(100, 410))
            fenetre.blit(police_aide.render("vous ne pouvez pas l’utiliser directement   ", True, (242, 200, 105)),(100, 440))
            fenetre.blit(police_aide.render("pour ouvrir la porte, vous pouvez seulement  ", True, (242, 200, 105)),(100, 470))
            fenetre.blit(police_aide.render("le consulter en lecture.", True, (242, 200, 105)),(100, 500))
            fenetre.blit(bouton_suivant.imageLoad, (350,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aideP1 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (900, 10))

        if porteN1.verouille == 1:
            fenetre.blit(porteN1.imageFerme, (0,0))
        if porteN1.verouille == 0:
            fenetre.blit(porteN1.imageOuverte, (0,0))
            fenetre.blit(bouton_continuer.imageLoad, (50, 560))
        if thread_1.indexNiveauPorte1 >= 0: #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
            porteN1.verouille = 0

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON POUR RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 191 or event.pos[0] <= 30 or event.pos[1] >= 82 or event.pos[1] <= 0) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0:
                bouton_retour.select()
                bouton_quitter.etat = False
                bouton_retour.etat = True
                bouton_continuer.etat = False
                selecteurNiveau()
                porteNiveau1 = False
            
            ###### BOUTON POUR CONTINUER QUE SI LA PORTE EST OUVERTE #####
            if porteN1.verouille == 0:
                if event.type == MOUSEMOTION and event.pos[0] <= 211 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 211 or event.pos[0] <= 50 or event.pos[1] >= 630 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = True
                    porteNiveau1 = False
                    porteNiveau2 = True
                    bouton_continuer.etat = False #Pour rénitialiser le bouton continuer entre les niveaux
            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 511 or event.pos[0] <= 350 or event.pos[1] >= 570 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500:
                bouton_suivant.select()
                aideP1 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 970 or event.pos[0] <= 900 or event.pos[1] >= 80 or event.pos[1] <= 10) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10:
                bouton_aide.select()
                aideP1 = True

##################################################################################################
#                                                                                                #
#                                       Niveau 2 Porte                                           #
#                                                                                                #
##################################################################################################

    while porteNiveau2 == True:
        thread_1.data = ""
        thread_1.choixNiveauSerial = "b"
        fenetre.blit(fenetre_porteNiveau2.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (30, -10))
        fenetre.blit(testAide.imageLoad, (450,200))

        if aideP2 == True:
            testAide.affichePanneau()
            fenetre.blit(police_aide.render("PORTE NIVEAU 2", True, (242, 200, 105)),(580, 230))
            fenetre.blit(police_aide.render("Une fois entré, vous avez accès à l’accueil", True, (242, 200, 105)),(480, 290))
            fenetre.blit(police_aide.render("du bâtiment, mais êtes bloqué par une porte.", True, (242, 200, 105)),(480, 320))
            fenetre.blit(police_aide.render("Vous apercevez sur le comptoir du bureau de ", True, (242, 200, 105)),(480, 380))
            fenetre.blit(police_aide.render("l’accueil le badge d’accès d’une personne. ", True, (242, 200, 105)),(480, 410))
            fenetre.blit(police_aide.render("Copiez le avant que cette personne ne revienne.   ", True, (242, 200, 105)),(480, 440))
            fenetre.blit(bouton_suivant.imageLoad, (740,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aideP2 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (900, 10))
        if porteN2.verouille == 1:
            fenetre.blit(porteN2.imageFerme, (0,0))
        if porteN2.verouille == 0:
            fenetre.blit(porteN2.imageOuverte, (0,0))
            fenetre.blit(bouton_continuer.imageLoad, (50, 560))
        if thread_1.indexNiveauPorte2 >= 0: #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
            porteN2.verouille = 0


        pygame.display.update()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON POUR RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 191 or event.pos[0] <= 30 or event.pos[1] >= 82 or event.pos[1] <= 0) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0:
                bouton_retour.select()
                bouton_quitter.etat = False
                bouton_retour.etat = True
                bouton_continuer.etat = False
                selecteurNiveau()
                porteNiveau2 = False
           
            ###### BOUTON POUR CONTINUER QUE SI LA PORTE EST OUVERTE #####
            if porteN2.verouille == 0:
                if event.type == MOUSEMOTION and event.pos[0] <= 211 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 211 or event.pos[0] <= 50 or event.pos[1] >= 630 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = False
                    porteNiveau2 = False
                    porteNiveau3_1 = True

            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 901 and event.pos[0] >= 740 and event.pos[1] <= 570 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 901 or event.pos[0] <= 740 or event.pos[1] >= 570 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 901 and event.pos[0] >= 740 and event.pos[1] <= 570 and event.pos[1] >= 500:
                bouton_suivant.select()
                aideP2 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 970 or event.pos[0] <= 900 or event.pos[1] >= 80 or event.pos[1] <= 10) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10:
                bouton_aide.select()
                aideP2 = True


##################################################################################################
#                                                                                                #
#                                       Niveau 3_1 Porte                                         #
#                                                                                                #
##################################################################################################

    while porteNiveau3_1 == True:
        thread_1.data = ""
        fenetre.blit(fenetre_porteNiveau3_1.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (30, -10))
        fenetre.blit(bouton_blouse.imageLoad, (0,0))
        

        if suivant3_1 == True:
            fenetre.blit(habitScientifique, (0,0))
            fenetre.blit(bouton_continuer.imageLoad, (50, 560))

        fenetre.blit(testAide.imageLoad, (60,200))
        if aideP3_1 == True:
            testAide.affichePanneau()
            fenetre.blit(police_aide.render("PORTE NIVEAU 3.1", True, (242, 200, 105)),(200, 230))
            fenetre.blit(police_aide.render("Vous ne passez pas inaperçue avec votre  ", True, (242, 200, 105)),(100, 290))
            fenetre.blit(police_aide.render("jogging il faudrait trouver quelque chose   ", True, (242, 200, 105)),(100, 320))
            fenetre.blit(police_aide.render("pour se fondre dans la masse.  ", True, (242, 200, 105)),(100, 350))
            fenetre.blit(bouton_suivant.imageLoad, (350,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aideP3_1 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (900, 10))
        
        

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON POUR RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 191 or event.pos[0] <= 30 or event.pos[1] >= 82 or event.pos[1] <= 0) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0:
                bouton_retour.select()
                bouton_quitter.etat = False
                bouton_retour.etat = True
                bouton_continuer.etat = False
                selecteurNiveau()
                porteNiveau3_1 = False
            
            ###### BOUTON POUR SELECTIONNER BLOUSE #####
            if event.type == MOUSEMOTION and event.pos[0] <= 280 and event.pos[0] >= 150 and event.pos[1] <= 530 and event.pos[1] >= 220 and bouton_quitter.etat == False:
                bouton_blouse.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 280 or event.pos[0] <= 150 or event.pos[1] >= 530 or event.pos[1] <= 220) and bouton_quitter.etat == False:
                bouton_blouse.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 280 and event.pos[0] >= 150 and event.pos[1] <= 530 and event.pos[1] >= 220:
                suivant3_1 = True
            
            ###### BOUTON POUR CONTINUER QUE SI LA BLOUSE EST PRISE #####
            if suivant3_1 == True:
                if event.type == MOUSEMOTION and event.pos[0] <= 211 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 211 or event.pos[0] <= 50 or event.pos[1] >= 630 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = True
                    porteNiveau3_1 = False
                    suivant3_1 = False
                    porteNiveau3_2 = True
                    bouton_continuer.etat = False #Pour rénitialiser le bouton continuer entre les niveaux

            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 511 or event.pos[0] <= 350 or event.pos[1] >= 570 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500:
                bouton_suivant.select()
                aideP3_1 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 970 or event.pos[0] <= 900 or event.pos[1] >= 80 or event.pos[1] <= 10) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10:
                bouton_aide.select()
                aideP3_1 = True

##################################################################################################
#                                                                                                #
#                                       Niveau 3_2 Porte                                         #
#                                                                                                #
##################################################################################################

    while porteNiveau3_2 == True:
        thread_1.data = ""
        thread_1.choixNiveauSerial = "c"
        fenetre.blit(fenetre_porteNiveau3_2.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (30, -10))
        fenetre.blit(testAide.imageLoad, (450,200))

        if aideP3 == True:
            testAide.affichePanneau()
            fenetre.blit(police_aide.render("PORTE NIVEAU 3", True, (242, 200, 105)),(580, 230))
            fenetre.blit(police_aide.render("Après avoir enfilé votre blouse, vous vous ", True, (242, 200, 105)),(480, 290))
            fenetre.blit(police_aide.render("retrouvez dans une salle blanche devant ", True, (242, 200, 105)),(480, 320))
            fenetre.blit(police_aide.render("une nouvelle porte, cependant impossible  ", True, (242, 200, 105)),(480, 350))
            fenetre.blit(police_aide.render("d’y entrer. Essayer de copier le badge  ", True, (242, 200, 105)),(480, 380))
            fenetre.blit(police_aide.render("sans que l’employé ne vous voie.   ", True, (242, 200, 105)),(480, 410))
            fenetre.blit(bouton_suivant.imageLoad, (740,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aideP3 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (900, 10))
        if porteN3.verouille == 1:
            fenetre.blit(porteN3.imageFerme, (0,0))
        if porteN3.verouille == 0:
            fenetre.blit(porteN3.imageOuverte, (0,0))
            fenetre.blit(bouton_continuer.imageLoad, (50, 560))
        if thread_1.indexNiveauPorte3 >= 0: #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
            porteN3.verouille = 0


        pygame.display.update()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON POUR RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 191 or event.pos[0] <= 30 or event.pos[1] >= 82 or event.pos[1] <= 0) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0:
                bouton_retour.select()
                bouton_quitter.etat = False
                bouton_retour.etat = True
                bouton_continuer.etat = False
                selecteurNiveau()
                porteNiveau3_2 = False
           
            ###### BOUTON POUR CONTINUER QUE SI LA PORTE EST OUVERTE #####
            if porteN3.verouille == 0:
                if event.type == MOUSEMOTION and event.pos[0] <= 211 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 211 or event.pos[0] <= 50 or event.pos[1] >= 630 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = False
                    porteNiveau3_2 = False
                    porteNiveau4 = True

            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 901 and event.pos[0] >= 740 and event.pos[1] <= 570 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 901 or event.pos[0] <= 740 or event.pos[1] >= 570 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 901 and event.pos[0] >= 740 and event.pos[1] <= 570 and event.pos[1] >= 500:
                bouton_suivant.select()
                aideP3 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 970 or event.pos[0] <= 900 or event.pos[1] >= 80 or event.pos[1] <= 10) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10:
                bouton_aide.select()
                aideP3 = True


##################################################################################################
#                                                                                                #
#                                       Niveau 4 Porte                                           #
#                                                                                                #
##################################################################################################

    while porteNiveau4 == True:
        thread_1.data = ""
        thread_1.choixNiveauSerial = "d"
        fenetre.blit(fenetre_porteNiveau4.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (30, -10))

        if porteN4.verouille == 1:
            fenetre.blit(porteN4.imageFerme, (0,0))
        if porteN4.verouille == 0:
            fenetre.blit(porteN4.imageOuverte, (0,0))
            fenetre.blit(bouton_continuer.imageLoad, (50, 560))
        fenetre.blit(testAide.imageLoad, (450,200))
        if aideP4 == True:
            testAide.affichePanneau()
            fenetre.blit(police_aide.render("PORTE NIVEAU 4", True, (242, 200, 105)),(580, 230))
            fenetre.blit(police_aide.render("Vous faites face à la porte du coffre-fort,", True, (242, 200, 105)),(480, 290))
            fenetre.blit(police_aide.render("l’équipe de sécurité a mis le paquet pour ", True, (242, 200, 105)),(480, 320))
            fenetre.blit(police_aide.render(" sécuriser les badges.", True, (242, 200, 105)),(480, 350))
            fenetre.blit(police_aide.render("Il se sera pas de tout repos pour copier ce", True, (242, 200, 105)),(480, 410))
            fenetre.blit(police_aide.render("dernier badge. Attention copier ce badge vous", True, (242, 200, 105)),(480, 440))
            fenetre.blit(police_aide.render("prendra beaucoup de temps.", True, (242, 200, 105)),(480, 470))
            fenetre.blit(bouton_suivant.imageLoad, (740,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aideP4 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (900, 10))
        if thread_1.indexNiveauPorte4 >= 0: #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
            porteN4.verouille = 0


        pygame.display.update()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON POUR RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 191 or event.pos[0] <= 30 or event.pos[1] >= 82 or event.pos[1] <= 0) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0:
                bouton_retour.select()
                bouton_quitter.etat = False
                bouton_retour.etat = True
                bouton_continuer.etat = False
                selecteurNiveau()
                porteNiveau4 = False
           
            ###### BOUTON POUR CONTINUER QUE SI LA PORTE EST OUVERTE #####
            if porteN4.verouille == 0:
                if event.type == MOUSEMOTION and event.pos[0] <= 211 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 211 or event.pos[0] <= 50 or event.pos[1] >= 630 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = False
                    selecteurNiveau() #Comme c'est le dernier niveau on retombe sur la sélection de menu """""""A CHANGER SI CE N'EST PLUS LE DERNIER NIVEAU"""""""""
                    porteNiveau4 = False

            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 901 and event.pos[0] >= 740 and event.pos[1] <= 570 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 901 or event.pos[0] <= 740 or event.pos[1] >= 570 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 901 and event.pos[0] >= 740 and event.pos[1] <= 570 and event.pos[1] >= 500:
                bouton_suivant.select()
                aideP4 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 970 or event.pos[0] <= 900 or event.pos[1] >= 80 or event.pos[1] <= 10) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10:
                bouton_aide.select()
                aideP4 = True



##################################################################################################
#                                                                                                #
#                                   Niveau 1 Distributeur                                        #
#                                                                                                #
##################################################################################################

    valeure = True

    while distributeurNiveau1 == True:
        thread_1.data = ""

        fenetre.blit(fenetre_distribNiveau1.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (30, -10))
        fenetre.blit(bouton_coca.imageLoad, (0, 0))
        fenetre.blit(bouton_evian.imageLoad, (0, 0))
        fenetre.blit(bouton_sprite.imageLoad, (0, 0))
        fenetre.blit(bouton_iceTea.imageLoad, (0, 0))
        fenetre.blit(testAide.imageLoad, (60,200))
        fenetre.blit(texte_bienvenue, (355, 85))
        fenetre.blit(texte_etoiles, (355, 95))
        fenetre.blit(texte_Cartes, (355, 105))
        fenetre.blit(texte_etoiles, (355, 115))

        if aideD1 == True:
            testAide.affichePanneau()
            fenetre.blit(police_aide.render("DISTRIBUTEUR NIVEAU 1", True, (242, 200, 105)),(180, 230))
            fenetre.blit(police_aide.render("Vous possédez un badge de paiement,", True, (242, 200, 105)),(100, 290))
            fenetre.blit(police_aide.render("cependant son solde (1 €) est insuffisant", True, (242, 200, 105)),(100, 320))
            fenetre.blit(police_aide.render("pour acheter plusieurs boisson.", True, (242, 200, 105)),(100, 350))
            fenetre.blit(police_aide.render("Achetez en 3 il vaut mieux en avoir trop ", True, (242, 200, 105)),(100, 410))
            fenetre.blit(police_aide.render("que pas assez.", True, (242, 200, 105)),(100, 440))
            fenetre.blit(bouton_suivant.imageLoad, (350,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aideD1 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (900, 10))

        if distributeur1.compteur >= 3:
            fenetre.blit(bouton_continuer.imageLoad, (50, 560))

        if thread_1.obtenuBoisson == 1:
            distributeur1.addcompteur()
            thread_1.obtenuBoisson = 0
        
        if thread_1.carteNonPresente >= 0:
            bouton_evian.etat = False
            bouton_sprite.etat = False
            bouton_iceTea.etat = False
            bouton_coca.etat = False
            thread_1.insuffisant = -1
            pygame.display.flip()

        if thread_1.soldeInsuffisant == -1:

            if bouton_coca.etat == True:
                ########### GET ITEM ###########
                item = distributeur1.getItem("Coca")
                            
                ########## BUY ITEM ############                  
                if thread_1.insuffisant >= 0:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()

                else:
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Votre Solde : " + str(thread_1.soldeAvant) + "€", None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name) + " à 3€", None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    fenetre.blit(texte("Nouveau Solde : " + str(thread_1.soldeApres) + "€", None, 20, "#000000"), (355,125))
                    fenetre.blit(texte_etoiles, (355, 135))
                    fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                    fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()


            if bouton_evian.etat == True:
                ########### GET ITEM ###########
                item = distributeur1.getItem("Evian")
                            
                ########## BUY ITEM ############

                if thread_1.insuffisant >= 0 and thread_1.soldeInsuffisant == -1:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()

                else:
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Votre Solde : " + str(thread_1.soldeAvant) + "€", None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name) + " à 1€", None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    
                    
                    fenetre.blit(texte("Nouveau Solde : " + str(thread_1.soldeApres) + "€", None, 20, "#000000"), (355,125))
                    fenetre.blit(texte_etoiles, (355, 135))
                    fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                    fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()


            if bouton_sprite.etat == True:
                ########### GET ITEM ###########
                item = distributeur1.getItem("Sprite")
                            
                ########## BUY ITEM ############

                if thread_1.insuffisant >= 0 and thread_1.soldeInsuffisant == -1:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()

                else:
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Votre Solde : " + str(thread_1.soldeAvant) + "€", None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name) + " à 2€", None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    
                    
                    fenetre.blit(texte("Nouveau Solde : " + str(thread_1.soldeApres) + "€", None, 20, "#000000"), (355,125))
                    fenetre.blit(texte_etoiles, (355, 135))
                    fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                    fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()


            if bouton_iceTea.etat == True:
                ########### GET ITEM ###########
                item = distributeur1.getItem("Ice Tea")
                            
                ########## BUY ITEM ############

                if thread_1.insuffisant >= 0 and thread_1.soldeInsuffisant == -1:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()

                else:
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Votre Solde : " + str(thread_1.soldeAvant) + "€", None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name) + " à 2€", None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    
                    
                    fenetre.blit(texte("Nouveau Solde : " + str(thread_1.soldeApres) + "€", None, 20, "#000000"), (355,125))
                    fenetre.blit(texte_etoiles, (355, 135))
                    fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                    fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()

        if thread_1.soldeInsuffisant >= 0:
            fenetre.blit(screen, (355,85))
            fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
            fenetre.blit(texte_etoiles, (355, 95))
            pygame.display.flip()

        pygame.display.update()

        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 191 or event.pos[0] <= 30 or event.pos[1] >= 82 or event.pos[1] <= 0) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0:
                bouton_retour.select()
                bouton_quitter.etat = False
                bouton_retour.etat = True
                bouton_continuer.etat = False
                selecteurNiveau()
                distributeurNiveau1 = False
                

            ##### BOUTON COCA ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_coca.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 327 and event.pos[1] >= 296:
                bouton_evian.etat = False
                bouton_sprite.etat = False
                bouton_iceTea.etat = False
                bouton_coca.select()
                thread_1.envoieSerialDistributeur1Coca()
                bouton_coca.etat = True
                pygame.time.wait(250)
            
            
            ###### BOUTON EVIAN ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_evian.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 365 and event.pos[1] >= 334:
                bouton_sprite.etat = False
                bouton_iceTea.etat = False
                bouton_coca.etat = False
                bouton_evian.select()
                thread_1.envoieSerialDistributeur1Evian()
                bouton_evian.etat = True
                pygame.time.wait(250)

            ###### BOUTON SPRITE ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_sprite.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 404 and event.pos[1] >= 373:
                bouton_iceTea.etat = False
                bouton_coca.etat = False
                bouton_evian.etat = False
                bouton_sprite.select()
                thread_1.envoieSerialDistributeur1Sprite()
                bouton_sprite.etat = True
                pygame.time.wait(250)

            ####### BOUTON ICE TEA ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_iceTea.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 442 and event.pos[1] >= 411:
                bouton_coca.etat = False
                bouton_evian.etat = False
                bouton_sprite.etat = False
                bouton_iceTea.select()
                thread_1.envoieSerialDistributeur1IceTea()
                bouton_iceTea.etat = True
                pygame.time.wait(250)
            
            ####### BOUTON CONTINUER ######
            if distributeur1.compteur >= 3:
                if event.type == MOUSEMOTION and event.pos[0] <= 211 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 211 or event.pos[0] <= 50 or event.pos[1] >= 630 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = False
                    distributeurNiveau1 = False
                    distributeurNiveau2 = True


            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 511 or event.pos[0] <= 350 or event.pos[1] >= 570 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500:
                bouton_suivant.select()
                aideD1 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 970 or event.pos[0] <= 900 or event.pos[1] >= 80 or event.pos[1] <= 10) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10:
                bouton_aide.select()
                aideD1 = True


##################################################################################################
#                                                                                                #
#                                   Niveau 2 Distributeur                                        #
#                                                                                                #
##################################################################################################


    while distributeurNiveau2 == True:
        thread_1.data = ""

        fenetre.blit(fenetre_distribNiveau2.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (30, -10))
        fenetre.blit(bouton_coca.imageLoad, (0, 0))
        fenetre.blit(bouton_evian.imageLoad, (0, 0))
        fenetre.blit(bouton_sprite.imageLoad, (0, 0))
        fenetre.blit(bouton_iceTea.imageLoad, (0, 0))
        fenetre.blit(testAide.imageLoad, (60,200))
        fenetre.blit(texte_bienvenue, (355, 85))
        fenetre.blit(texte_etoiles, (355, 95))
        fenetre.blit(texte_Cartes, (355, 105))
        fenetre.blit(texte_etoiles, (355, 115))

        if aideD2 == True:
            testAide.affichePanneau()
            fenetre.blit(police_aide.render("DISTRIBUTEUR NIVEAU 2", True, (242, 200, 105)),(180, 230))
            fenetre.blit(police_aide.render("Vous devez réussir à acheter 2 boissons à 2 €" , True, (242, 200, 105)),(100, 290))
            fenetre.blit(police_aide.render("alors que votre solde actuel est de 2 €.", True, (242, 200, 105)),(100, 320))
            fenetre.blit(police_aide.render("Il semble qu’un petit temps d’attente", True, (242, 200, 105)),(100, 380))
            fenetre.blit(police_aide.render("se passe avant le débit de la carte.", True, (242, 200, 105)),(100, 410))
            fenetre.blit(police_aide.render("que pas assez.", True, (242, 200, 105)),(100, 440))
            fenetre.blit(bouton_suivant.imageLoad, (350,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aideD2 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (900, 10))

        if thread_1.soldeAvant == thread_1.soldeApres and distributeur2.compteur >= 1:
            fenetre.blit(bouton_continuer.imageLoad, (50, 560))

        if thread_1.obtenuBoisson == 1:
            distributeur2.addcompteur()
            thread_1.obtenuBoisson = 0
        
        if thread_1.carteNonPresente >= 0:
            bouton_evian.etat = False
            bouton_sprite.etat = False
            bouton_iceTea.etat = False
            bouton_coca.etat = False
            thread_1.insuffisant = -1
            pygame.display.flip()

        if thread_1.soldeInsuffisant == -1:

            if bouton_coca.etat == True:
                ########### GET ITEM ###########
                item = distributeur2.getItem("Coca")
                            
                ########## BUY ITEM ############                  
                if thread_1.insuffisant >= 0:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()

                else:
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Votre Solde : " + str(thread_1.soldeAvant) + "€", None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name) + " à 3€", None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    fenetre.blit(texte("Nouveau Solde : " + str(thread_1.soldeApres) + "€", None, 20, "#000000"), (355,125))
                    fenetre.blit(texte_etoiles, (355, 135))
                    fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                    fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()


            if bouton_evian.etat == True:
                ########### GET ITEM ###########
                item = distributeur2.getItem("Evian")
                            
                ########## BUY ITEM ############

                if thread_1.insuffisant >= 0 and thread_1.soldeInsuffisant == -1:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()

                else:
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Votre Solde : " + str(thread_1.soldeAvant) + "€", None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name) + " à 1€", None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    
                    
                    fenetre.blit(texte("Nouveau Solde : " + str(thread_1.soldeApres) + "€", None, 20, "#000000"), (355,125))
                    fenetre.blit(texte_etoiles, (355, 135))
                    fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                    fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()


            if bouton_sprite.etat == True:
                ########### GET ITEM ###########
                item = distributeur2.getItem("Sprite")
                            
                ########## BUY ITEM ############

                if thread_1.insuffisant >= 0 and thread_1.soldeInsuffisant == -1:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()

                else:
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Votre Solde : " + str(thread_1.soldeAvant) + "€", None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name) + " à 2€", None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    
                    
                    fenetre.blit(texte("Nouveau Solde : " + str(thread_1.soldeApres) + "€", None, 20, "#000000"), (355,125))
                    fenetre.blit(texte_etoiles, (355, 135))
                    fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                    fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()


            if bouton_iceTea.etat == True:
                ########### GET ITEM ###########
                item = distributeur2.getItem("Ice Tea")
                            
                ########## BUY ITEM ############

                if thread_1.insuffisant >= 0 and thread_1.soldeInsuffisant == -1:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()

                else:
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Votre Solde : " + str(thread_1.soldeAvant) + "€", None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name) + " à 2€", None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    
                    
                    fenetre.blit(texte("Nouveau Solde : " + str(thread_1.soldeApres) + "€", None, 20, "#000000"), (355,125))
                    fenetre.blit(texte_etoiles, (355, 135))
                    fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                    fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()

        if thread_1.soldeInsuffisant >= 0:
            fenetre.blit(screen, (355,85))
            fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
            fenetre.blit(texte_etoiles, (355, 95))
            pygame.display.flip()

        pygame.display.update()

        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 191 or event.pos[0] <= 30 or event.pos[1] >= 82 or event.pos[1] <= 0) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0:
                bouton_retour.select()
                bouton_quitter.etat = False
                bouton_retour.etat = True
                bouton_continuer.etat = False
                selecteurNiveau()
                distributeurNiveau2 = False
                

            ##### BOUTON COCA ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_coca.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 327 and event.pos[1] >= 296:
                bouton_evian.etat = False
                bouton_sprite.etat = False
                bouton_iceTea.etat = False
                bouton_coca.select()
                thread_1.envoieSerialDistributeur1Coca()
                bouton_coca.etat = True
                pygame.time.wait(150)
            
            
            ###### BOUTON EVIAN ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_evian.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 365 and event.pos[1] >= 334:
                bouton_sprite.etat = False
                bouton_iceTea.etat = False
                bouton_coca.etat = False
                bouton_evian.select()
                thread_1.envoieSerialDistributeur1Evian()
                bouton_evian.etat = True
                pygame.time.wait(150)

            ###### BOUTON SPRITE ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_sprite.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 404 and event.pos[1] >= 373:
                bouton_iceTea.etat = False
                bouton_coca.etat = False
                bouton_evian.etat = False
                bouton_sprite.select()
                thread_1.envoieSerialDistributeur1Sprite()
                bouton_sprite.etat = True
                pygame.time.wait(150)

            ####### BOUTON ICE TEA ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_iceTea.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 442 and event.pos[1] >= 411:
                bouton_coca.etat = False
                bouton_evian.etat = False
                bouton_sprite.etat = False
                bouton_iceTea.select()
                thread_1.envoieSerialDistributeur1IceTea()
                bouton_iceTea.etat = True
                pygame.time.wait(150)
            
            ####### BOUTON CONTINUER ######
            if thread_1.soldeAvant == thread_1.soldeApres and distributeur2.compteur >= 1:
                if event.type == MOUSEMOTION and event.pos[0] <= 211 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 211 or event.pos[0] <= 50 or event.pos[1] >= 630 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = False
                    distributeurNiveau2 = False
                    selecteurNiveau() #DISTRIBUTEUR 3 NON FONCTIONNEL DONC FIN DU SCÉNARIO ICI
                    


            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 511 or event.pos[0] <= 350 or event.pos[1] >= 570 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500:
                bouton_suivant.select()
                aideD2 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 970 or event.pos[0] <= 900 or event.pos[1] >= 80 or event.pos[1] <= 10) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10:
                bouton_aide.select()
                aideD2 = True


##################################################################################################
#                                                                                                #
#                                   Niveau 3 Distributeur (Non fonctionnel)                      #
#                                                                                                #
##################################################################################################


    """while distributeurNiveau3 == True:
        

        fenetre.blit(fenetre_distribNiveau3.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (30, -10))
        fenetre.blit(bouton_coca.imageLoad, (0, 0))
        fenetre.blit(bouton_evian.imageLoad, (0, 0))
        fenetre.blit(bouton_sprite.imageLoad, (0, 0))
        fenetre.blit(bouton_iceTea.imageLoad, (0, 0))
        fenetre.blit(testAide.imageLoad, (60,200))
        fenetre.blit(texte_bienvenue, (355, 85))
        fenetre.blit(texte_etoiles, (355, 95))
        fenetre.blit(texte_Cartes, (355, 105))
        fenetre.blit(texte_etoiles, (355, 115))

        if aideD3 == True:
            testAide.affichePanneau()
            fenetre.blit(police_aide.render("DISTRIBUTEUR NIVEAU 3", True, (242, 200, 105)),(180, 230))
            fenetre.blit(police_aide.render("Vous avez 2 badges mais l'un d’eux a un solde", True, (242, 200, 105)),(100, 290))
            fenetre.blit(police_aide.render("de 0€.", True, (242, 200, 105)),(100, 320))
            fenetre.blit(police_aide.render("Serait-il possible de le recharger sans payer ?", True, (242, 200, 105)),(100, 380))
            fenetre.blit(bouton_suivant.imageLoad, (350,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aideD3 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (900, 10))

        if int(thread_1.soldeAvant) < int(thread_1.soldeApres) and distributeur3.compteur >= 1: #CONDITION DE VICTOIRE NON FONCTIONNEL.
            fenetre.blit(bouton_continuer.imageLoad, (50, 560))

        if thread_1.obtenuBoisson == 1:
            distributeur3.addcompteur()
            thread_1.obtenuBoisson = 0
        
        if thread_1.carteNonPresente >= 0:
            bouton_evian.etat = False
            bouton_sprite.etat = False
            bouton_iceTea.etat = False
            bouton_coca.etat = False
            thread_1.insuffisant = -1
            pygame.display.flip()

        if thread_1.soldeInsuffisant == -1:

            if bouton_coca.etat == True:
                ########### GET ITEM ###########
                item = distributeur3.getItem("Coca")
                            
                ########## BUY ITEM ############                  
                if thread_1.insuffisant >= 0:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()

                else:
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Votre Solde : " + str(thread_1.soldeAvant) + "€", None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name) + " à 3€", None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))
                    pygame.time.wait(100)
                    fenetre.blit(texte("Nouveau Solde : " + str(thread_1.soldeApres) + "€", None, 20, "#000000"), (355,125))
                    fenetre.blit(texte_etoiles, (355, 135))
                    fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                    fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()


            if bouton_evian.etat == True:
                ########### GET ITEM ###########
                item = distributeur3.getItem("Evian")
                            
                ########## BUY ITEM ############

                if thread_1.insuffisant >= 0:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()
                    

                else:
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Votre Solde : " + str(thread_1.soldeAvant) + "€", None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name) + " à 1€", None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    
                    
                    fenetre.blit(texte("Nouveau Solde : " + str(thread_1.soldeApres) + "€", None, 20, "#000000"), (355,125))
                    fenetre.blit(texte_etoiles, (355, 135))
                    fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                    fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()


            if bouton_sprite.etat == True:
                ########### GET ITEM ###########
                item = distributeur3.getItem("Sprite")
                            
                ########## BUY ITEM ############

                if thread_1.insuffisant >= 0:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()

                else:
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Votre Solde : " + str(thread_1.soldeAvant) + "€", None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name) + " à 2€", None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    
                    
                    fenetre.blit(texte("Nouveau Solde : " + str(thread_1.soldeApres) + "€", None, 20, "#000000"), (355,125))
                    fenetre.blit(texte_etoiles, (355, 135))
                    fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                    fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()


            if bouton_iceTea.etat == True:
                ########### GET ITEM ###########
                item = distributeur3.getItem("Ice Tea")
                            
                ########## BUY ITEM ############

                if thread_1.insuffisant >= 0:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()

                else:
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Votre Solde : " + str(thread_1.soldeAvant) + "€", None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name) + " à 2€", None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    
                    
                    fenetre.blit(texte("Nouveau Solde : " + str(thread_1.soldeApres) + "€", None, 20, "#000000"), (355,125))
                    fenetre.blit(texte_etoiles, (355, 135))
                    fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                    fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()

        if thread_1.soldeInsuffisant >= 0:
            fenetre.blit(screen, (355,85))
            fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
            fenetre.blit(texte_etoiles, (355, 95))
            pygame.display.flip()

        pygame.display.update()

        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 191 or event.pos[0] <= 30 or event.pos[1] >= 82 or event.pos[1] <= 0) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0:
                bouton_retour.select()
                bouton_quitter.etat = False
                bouton_retour.etat = True
                bouton_continuer.etat = False
                selecteurNiveau()
                distributeurNiveau3 = False
                

            ##### BOUTON COCA ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_coca.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 327 and event.pos[1] >= 296:
                bouton_evian.etat = False
                bouton_sprite.etat = False
                bouton_iceTea.etat = False
                bouton_coca.select()
                thread_1.envoieSerialDistributeur3Coca()
                bouton_coca.etat = True
                pygame.time.wait(50)
            
            
            ###### BOUTON EVIAN ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_evian.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 365 and event.pos[1] >= 334:
                bouton_sprite.etat = False
                bouton_iceTea.etat = False
                bouton_coca.etat = False
                bouton_evian.select()
                thread_1.envoieSerialDistributeur3Evian()
                bouton_evian.etat = True
                pygame.time.wait(300)

            ###### BOUTON SPRITE ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_sprite.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 404 and event.pos[1] >= 373:
                bouton_iceTea.etat = False
                bouton_coca.etat = False
                bouton_evian.etat = False
                bouton_sprite.select()
                thread_1.envoieSerialDistributeur3Sprite()
                bouton_sprite.etat = True
                pygame.time.wait(300)

            ####### BOUTON ICE TEA ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_iceTea.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 442 and event.pos[1] >= 411:
                bouton_coca.etat = False
                bouton_evian.etat = False
                bouton_sprite.etat = False
                bouton_iceTea.select()
                thread_1.envoieSerialDistributeur3IceTea()
                bouton_iceTea.etat = True
                pygame.time.wait(300)
            
            ####### BOUTON CONTINUER (NON FONCTIONNEL) ######
            """ """if int(thread_1.soldeAvant) < int(thread_1.soldeApres) and distributeur3.compteur >= 1:
                if event.type == MOUSEMOTION and event.pos[0] <= 211 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 211 or event.pos[0] <= 50 or event.pos[1] >= 630 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = False
                    distributeurNiveau3 = False
                    selecteurNiveau()""" """
                    


            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 511 or event.pos[0] <= 350 or event.pos[1] >= 570 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500:
                bouton_suivant.select()
                aideD3 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 970 or event.pos[0] <= 900 or event.pos[1] >= 80 or event.pos[1] <= 10) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10:
                bouton_aide.select()
                aideD3 = True """


##################################################################################################
#                                                                                                #
#                                   Niveau 1_1 Hotel                                             #
#                                                                                                #
##################################################################################################
  
    while hotelNiveau1_1 == True:
        thread_1.data = ""
        fenetre.blit(fenetre_hotelNiveau1_1.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (30, -10))
        

        if thread_1.indexNiveauHotel1_1 >= 0: #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
            porteNH1_1.verouille = 0
            thread_1.choixNiveauSerial = ""
            

        if porteNH1_1.verouille == 1:
            fenetre.blit(porteNH1_1.imageFerme, (0,0))
            thread_1.choixNiveauSerial = "v"
        if porteNH1_1.verouille == 0:
            fenetre.blit(porteNH1_1.imageOuverte, (0,0))
            fenetre.blit(bouton_continuer.imageLoad, (50, 560))
            thread_1.choixNiveauSerial = ""
        

        fenetre.blit(testAide.imageLoad, (450,200))

        if aideH1 == True:
            testAide.affichePanneau()
            fenetre.blit(police_aide.render("HÔTEL NIVEAU 1", True, (242, 200, 105)),(580, 230))
            fenetre.blit(police_aide.render("Vous devez vous rendre à votre hôtel mais", True, (242, 200, 105)),(480, 290))
            fenetre.blit(police_aide.render("pour cela il va falloir passer par les ", True, (242, 200, 105)),(480, 320))
            fenetre.blit(police_aide.render("transports en commun.", True, (242, 200, 105)),(480, 350))
            fenetre.blit(police_aide.render("Il vous faudra utiliser 3 voyages,", True, (242, 200, 105)),(480, 410))
            fenetre.blit(police_aide.render("mais il ne vous en reste que 2 sur votre carte", True, (242, 200, 105)),(480, 440))
            fenetre.blit(police_aide.render("de métro et vous n’avez pas d’argent pour la", True, (242, 200, 105)),(480, 470))
            fenetre.blit(police_aide.render("recharger mais ce n’est pas", True, (242, 200, 105)),(480, 500))
            fenetre.blit(police_aide.render("ça qui va vous arrêter.", True, (242, 200, 105)),(480, 530))
            fenetre.blit(bouton_suivant.imageLoad, (740,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aideH1 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (900, 10))

        pygame.display.update()
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON POUR RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 191 or event.pos[0] <= 30 or event.pos[1] >= 82 or event.pos[1] <= 0) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0:
                bouton_retour.select()
                bouton_quitter.etat = False
                bouton_retour.etat = True
                thread_1.compteurMetro = 0
                bouton_continuer.etat = False
                selecteurNiveau()
                hotelNiveau1_1 = False
        
            ###### BOUTON POUR CONTINUER QUE SI LA PORTE EST OUVERTE #####
            if porteNH1_1.verouille == 0:
                if event.type == MOUSEMOTION and event.pos[0] <= 211 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 211 or event.pos[0] <= 50 or event.pos[1] >= 630 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    thread_1.compteurMetro = 0
                    bouton_continuer.etat = False
                    hotelNiveau1_1 = False
                    hotelNiveau1_2 = True

            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 901 and event.pos[0] >= 740 and event.pos[1] <= 570 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 901 or event.pos[0] <= 740 or event.pos[1] >= 570 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 901 and event.pos[0] >= 740 and event.pos[1] <= 570 and event.pos[1] >= 500:
                bouton_suivant.select()
                aideH1 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 970 or event.pos[0] <= 900 or event.pos[1] >= 80 or event.pos[1] <= 10) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10:
                bouton_aide.select()
                aideH1 = True


##################################################################################################
#                                                                                                #
#                                   Niveau 1_2 Hotel                                             #
#                                                                                                #
##################################################################################################

    while hotelNiveau1_2 == True:
        thread_1.data = ""
        fenetre.blit(fenetre_hotelNiveau1_2.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (30, -10))
        fenetre.blit(testAide.imageLoad, (450,200))

        
        if thread_1.indexNiveauHotel1_2 >= 0: #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
            porteNH1_2.verouille = 0
            thread_1.choixNiveauSerial = ""

        if porteNH1_2.verouille == 1:
            fenetre.blit(porteNH1_2.imageFerme, (0,0))
            thread_1.choixNiveauSerial = "v"
        if porteNH1_2.verouille == 0:
            fenetre.blit(porteNH1_2.imageOuverte, (0,0))
            fenetre.blit(bouton_continuer.imageLoad, (50, 560))
            thread_1.choixNiveauSerial = ""
        

        if aideH1 == True:
            testAide.affichePanneau()
            fenetre.blit(bouton_suivant.imageLoad, (740,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aideH1 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (900, 10))

        pygame.display.update()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON POUR RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 191 or event.pos[0] <= 30 or event.pos[1] >= 82 or event.pos[1] <= 0) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0:
                bouton_retour.select()
                thread_1.compteurMetro = 0
                bouton_quitter.etat = False
                bouton_retour.etat = True
                selecteurNiveau()
                hotelNiveau1_2 = False
        
            ###### BOUTON POUR CONTINUER QUE SI LA PORTE EST OUVERTE #####
            if porteNH1_2.verouille == 0:
                if event.type == MOUSEMOTION and event.pos[0] <= 211 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 211 or event.pos[0] <= 50 or event.pos[1] >= 630 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    thread_1.compteurMetro = 0
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = False
                    hotelNiveau1_2 = False
                    hotelNiveau1_3 = True

            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 901 and event.pos[0] >= 740 and event.pos[1] <= 570 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 901 or event.pos[0] <= 740 or event.pos[1] >= 570 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 901 and event.pos[0] >= 740 and event.pos[1] <= 570 and event.pos[1] >= 500:
                bouton_suivant.select()
                aideH1 = False

            ###### BOUTON AIDE ######
            if event.type == MOUSEMOTION and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 970 or event.pos[0] <= 900 or event.pos[1] >= 80 or event.pos[1] <= 10) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10:
                bouton_aide.select()
                aideH1 = True


##################################################################################################
#                                                                                                #
#                                   Niveau 1_3 Hotel                                             #
#                                                                                                #
##################################################################################################

    while hotelNiveau1_3 == True:
        thread_1.data = ""
        fenetre.blit(fenetre_hotelNiveau1_3.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (30, -10))
        

        if thread_1.indexNiveauHotel1_3 >= 0: #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
            porteNH1_3.verouille = 0
            thread_1.choixNiveauSerial = ""

        if porteNH1_3.verouille == 1:
            fenetre.blit(porteNH1_3.imageFerme, (0,0))
            thread_1.choixNiveauSerial = "v"
        if porteNH1_3.verouille == 0:
            fenetre.blit(porteNH1_3.imageOuverte, (0,0))
            fenetre.blit(bouton_continuer.imageLoad, (50, 560))
            thread_1.choixNiveauSerial = ""
        

        fenetre.blit(testAide.imageLoad, (450,200))

        if aideH1 == True:
            testAide.affichePanneau()
            fenetre.blit(bouton_suivant.imageLoad, (740,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aideH1 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (900, 10))

        pygame.display.update()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON POUR RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 191 or event.pos[0] <= 30 or event.pos[1] >= 82 or event.pos[1] <= 0) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0:
                bouton_retour.select()
                thread_1.compteurMetro = 0
                bouton_quitter.etat = False
                bouton_retour.etat = True
                bouton_continuer.etat = False
                selecteurNiveau()
                hotelNiveau1 = False
        
            ###### BOUTON POUR CONTINUER QUE SI LA PORTE EST OUVERTE #####
            if porteNH1_3.verouille == 0:
                if event.type == MOUSEMOTION and event.pos[0] <= 211 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 211 or event.pos[0] <= 50 or event.pos[1] >= 630 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    thread_1.compteurMetro = 0
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = False
                    hotelNiveau2 = True
                    hotelNiveau1_3 = False

            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 901 and event.pos[0] >= 740 and event.pos[1] <= 570 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 901 or event.pos[0] <= 740 or event.pos[1] >= 570 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 901 and event.pos[0] >= 740 and event.pos[1] <= 570 and event.pos[1] >= 500:
                bouton_suivant.select()
                aideH1 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 970 or event.pos[0] <= 900 or event.pos[1] >= 80 or event.pos[1] <= 10) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10:
                bouton_aide.select()
                aideH1 = True

    
##################################################################################################
#                                                                                                #
#                                       Niveau 2 Hotel                                           #
#                                                                                                #
##################################################################################################

    while hotelNiveau2 == True:
        thread_1.data = ""
        thread_1.choixNiveauSerial = "f"
        fenetre.blit(fenetre_hotelNiveau2.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (30, -10))
        fenetre.blit(testAide.imageLoad, (60,200))

        if aideH2 == True:
            testAide.affichePanneau()
            fenetre.blit(police_aide.render("HÔTEL NIVEAU 2", True, (242, 200, 105)),(200, 230))
            fenetre.blit(police_aide.render("Vous vous trouvez à l’hôtel. À la réception,", True, (242, 200, 105)),(100, 290))
            fenetre.blit(police_aide.render("on vous donne un badge pour la porte 237.", True, (242, 200, 105)),(100, 320))
            fenetre.blit(police_aide.render("Cependant, cette chambre ne vous inspire", True, (242, 200, 105)),(100, 380))
            fenetre.blit(police_aide.render("pas confiance et la chambre d’en face semble ", True, (242, 200, 105)),(100, 410))
            fenetre.blit(police_aide.render("inoccupée. Essayez plutôt de dormir dans la ", True, (242, 200, 105)),(100, 440))
            fenetre.blit(police_aide.render("chambre 243.", True, (242, 200, 105)),(100, 470))
            fenetre.blit(bouton_suivant.imageLoad, (350,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aideH2 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (900, 10))
        if porteNH2.verouille == 1:
            fenetre.blit(porteNH2.imageFerme, (0,0))
        if porteNH2.verouille == 0:
            fenetre.blit(porteNH2.imageOuverte, (0,0))
            fenetre.blit(bouton_continuer.imageLoad, (50, 560))
        if thread_1.indexNiveauHotel2 >= 0: #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
            porteNH2.verouille = 0

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON POUR RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 191 or event.pos[0] <= 30 or event.pos[1] >= 82 or event.pos[1] <= 0) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0:
                bouton_retour.select()
                bouton_quitter.etat = False
                bouton_retour.etat = True
                bouton_continuer.etat = False
                selecteurNiveau()
                hotelNiveau2 = False
            
            ###### BOUTON POUR CONTINUER QUE SI LA PORTE EST OUVERTE #####
            if porteNH2.verouille == 0:
                if event.type == MOUSEMOTION and event.pos[0] <= 211 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 211 or event.pos[0] <= 50 or event.pos[1] >= 630 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = False
                    hotelNiveau2 = False
                    hotelNiveau3 = True

            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 511 or event.pos[0] <= 350 or event.pos[1] >= 570 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500:
                bouton_suivant.select()
                aideH2 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 970 or event.pos[0] <= 900 or event.pos[1] >= 80 or event.pos[1] <= 10) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10:
                bouton_aide.select()
                aideH2 = True



##################################################################################################
#                                                                                                #
#                                       Niveau 3 Hotel                                           #
#                                                                                                #
##################################################################################################

    while hotelNiveau3 == True:
        thread_1.data = ""
        thread_1.choixNiveauSerial = "g"
        fenetre.blit(fenetre_hotelNiveau3.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (30, -10))
        fenetre.blit(testAide.imageLoad, (60,200))

        if aideH3 == True:
            testAide.affichePanneau()
            fenetre.blit(police_aide.render("HÔTEL NIVEAU 3", True, (242, 200, 105)),(200, 230))
            fenetre.blit(police_aide.render("Vous avez envie de retourner dormir dans", True, (242, 200, 105)),(100, 290))
            fenetre.blit(police_aide.render("la chambre 243 une semaine plus tard.", True, (242, 200, 105)),(100, 320))
            fenetre.blit(police_aide.render("Heureusement vous avez oublié de rendre", True, (242, 200, 105)),(100, 380))
            fenetre.blit(police_aide.render("votre badge, essayer de trouver un moyen", True, (242, 200, 105)),(100, 410))
            fenetre.blit(police_aide.render("pour que la carte soit valide.", True, (242, 200, 105)),(100, 440))
            fenetre.blit(bouton_suivant.imageLoad, (350,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aideH3 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (900, 10))
        if porteNH3.verouille == 1:
            fenetre.blit(porteNH3.imageFerme, (0,0))
        if porteNH3.verouille == 0:
            fenetre.blit(porteNH3.imageOuverte, (0,0))
            fenetre.blit(bouton_continuer.imageLoad, (50, 560))
        if thread_1.indexNiveauHotel3 >= 0: #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
            porteNH3.verouille = 0

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON POUR RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 191 or event.pos[0] <= 30 or event.pos[1] >= 82 or event.pos[1] <= 0) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 191 and event.pos[0] >= 30 and event.pos[1] <= 82 and event.pos[1] >= 0:
                bouton_retour.select()
                bouton_quitter.etat = False
                bouton_retour.etat = True
                bouton_continuer.etat = False
                selecteurNiveau()
                hotelNiveau3 = False
            
            ###### BOUTON POUR CONTINUER QUE SI LA PORTE EST OUVERTE #####
            if porteNH3.verouille == 0:
                if event.type == MOUSEMOTION and event.pos[0] <= 211 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 211 or event.pos[0] <= 50 or event.pos[1] >= 630 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 50 and event.pos[1] <= 630 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = True
                    hotelNiveau3 = False
                    selecteurNiveau() #Comme c'est le dernier niveau on retombe sur la sélection de menu """""""A CHANGER SI CE N'EST PLUS LE DERNIER NIVEAU"""""""""
                    bouton_continuer.etat = False #Pour rénitialiser le bouton continuer entre les niveaux
            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 511 or event.pos[0] <= 350 or event.pos[1] >= 570 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 511 and event.pos[0] >= 350 and event.pos[1] <= 570 and event.pos[1] >= 500:
                bouton_suivant.select()
                aideH3 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 970 or event.pos[0] <= 900 or event.pos[1] >= 80 or event.pos[1] <= 10) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 970 and event.pos[0] >= 900 and event.pos[1] <= 80 and event.pos[1] >= 10:
                bouton_aide.select()
                aideH3 = True





################################# Fonction menu principale selection des niveaux  ##############################################


def selecteurNiveau(): #
    """
    Premiere interface : menu principal qui permet de sélectionner un niveau
    """

    gameStart = True

    fenetre_selection = Terrain("image/scene/sceneIntro.jpg")
    bouton_porte = Bouton("image/boutons/boutonPorte.png", "image/boutons/boutonPorteHoover.png", "image/boutons/boutonPorteSelect.png")
    bouton_distributeur = Bouton("image/boutons/boutonDistributeur.png", "image/boutons/boutonDistributeurHoover.png", "image/boutons/boutonDistributeurSelect.png")
    bouton_hotel = Bouton("image/boutons/boutonHotel.png", "image/boutons/boutonHotelHoover.png", "image/boutons/boutonHotelSelect.png")
    bouton_quitter = Bouton("image/boutons/boutonQuitter.png", "image/boutons/boutonQuitterHoover.png", "image/boutons/boutonQuitter.png")
    panneauPorte = PanneauNiveau("image/presqueRien.png", "image/panneauNiveau.png")
    panneauDistributeur = PanneauNiveau("image/presqueRien.png", "image/panneauNiveau.png")
    panneauHotel = PanneauNiveau("image/presqueRien.png", "image/panneauNiveau.png")

    bouton_Niveau1 = Bouton("image/boutons/boutonNiveau1.png", "image/boutons/boutonNiveau1Hoover.png", "image/boutons/boutonNiveau1.png")
    bouton_Niveau2 = Bouton("image/boutons/boutonNiveau2.png", "image/boutons/boutonNiveau2Hoover.png", "image/boutons/boutonNiveau2.png")
    bouton_Niveau3 = Bouton("image/boutons/boutonNiveau3.png", "image/boutons/boutonNiveau3Hoover.png", "image/boutons/boutonNiveau3.png")
    bouton_Niveau4 = Bouton("image/boutons/boutonNiveau4.png", "image/boutons/boutonNiveau4Hoover.png", "image/boutons/boutonNiveau4.png")
    bouton_Niveau5 = Bouton("image/boutons/boutonNiveau5.png", "image/boutons/boutonNiveau5Hoover.png", "image/boutons/boutonNiveau5.png")

    while gameStart == True:
        thread_1.choixNiveauSerial = ""
        fenetre = pygame.display.set_mode((1000, 661))
        fenetre.blit(fenetre_selection.fond,(0,0))
        fenetre.blit(bouton_porte.imageLoad,(100,255))
        fenetre.blit(bouton_distributeur.imageLoad,(100, 375))
        fenetre.blit(bouton_hotel.imageLoad, (100, 495))
        fenetre.blit(bouton_quitter.imageLoad, (40, 40))
        fenetre.blit(panneauPorte.imageLoad, (460,210))
        fenetre.blit(panneauDistributeur.imageLoad, (460,210))
        fenetre.blit(panneauHotel.imageLoad, (460,210))
        


        if bouton_porte.etat == True:
            panneauPorte.affichePanneau()
            panneauDistributeur.reinitPanneau()
            panneauHotel.reinitPanneau()
            fenetre.blit(bouton_Niveau1.imageLoad, (500,260))
            fenetre.blit(bouton_Niveau2.imageLoad, (720,260))
            fenetre.blit(bouton_Niveau3.imageLoad, (500,370))
            fenetre.blit(bouton_Niveau4.imageLoad, (720,370))
        if bouton_distributeur.etat == True:
            panneauPorte.reinitPanneau()
            panneauDistributeur.affichePanneau()
            panneauHotel.reinitPanneau()
            fenetre.blit(bouton_Niveau1.imageLoad, (500,260))
            fenetre.blit(bouton_Niveau2.imageLoad, (720,260))
            """fenetre.blit(bouton_Niveau3.imageLoad, (500,370))""" #DISTRRIBUTEUR 3 NON FONCTIONNEL
        if bouton_hotel.etat == True:
            panneauPorte.reinitPanneau()
            panneauDistributeur.reinitPanneau()
            panneauHotel.affichePanneau()
            fenetre.blit(bouton_Niveau1.imageLoad, (500,260))
            fenetre.blit(bouton_Niveau2.imageLoad, (720,260))
            fenetre.blit(bouton_Niveau3.imageLoad, (500,370))

        pygame.display.update()

        for event in pygame.event.get():
            ###### BOUTON POUR LA PORTE #####
            if event.type == MOUSEMOTION and event.pos[0] <= 320 and event.pos[0] >= 100 and event.pos[1] <= 335 and event.pos[1] >= 255 and bouton_porte.etat == False:
                bouton_porte.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 320 or event.pos[0] <= 100 or event.pos[1] >= 335 or event.pos[1] <= 255) and bouton_porte.etat == False:
                bouton_porte.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 320 and event.pos[0] >= 100 and event.pos[1] <= 335 and event.pos[1] >= 255:
                bouton_porte.select()
                bouton_porte.etat = True
                bouton_distributeur.etat = False
                bouton_hotel.etat = False
                bouton_quitter.etat = False

            if bouton_porte.etat == True:
                #Porte Niveau 1
                if event.type == MOUSEMOTION and event.pos[0] <= 681 and event.pos[0] >= 500 and event.pos[1] <= 330 and event.pos[1] >= 260:
                    bouton_Niveau1.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 681 or event.pos[0] <= 500 or event.pos[1] >= 330 or event.pos[1] <= 260):
                    bouton_Niveau1.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 681 and event.pos[0] >= 500 and event.pos[1] <= 330 and event.pos[1] >= 260:
                    bouclePrincipale(True, False, False, False, False, False, False, False, False, False)
                    bouton_porte.etat = False
                    gameStart = False
                #Porte Niveau 2
                if event.type == MOUSEMOTION and event.pos[0] <= 901 and event.pos[0] >= 720 and event.pos[1] <= 330 and event.pos[1] >= 260:
                    bouton_Niveau2.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 901 or event.pos[0] <= 720 or event.pos[1] >= 330 or event.pos[1] <= 260):
                    bouton_Niveau2.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 901 and event.pos[0] >= 720 and event.pos[1] <= 330 and event.pos[1] >= 260:
                    bouclePrincipale(False, True, False, False, False, False, False, False, False, False)
                    bouton_porte.etat = False
                    gameStart = False
                #Porte Niveau 3
                if event.type == MOUSEMOTION and event.pos[0] <= 681 and event.pos[0] >= 500 and event.pos[1] <= 440 and event.pos[1] >= 370:
                    bouton_Niveau3.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 681 or event.pos[0] <= 500 or event.pos[1] >= 440 or event.pos[1] <= 370):
                    bouton_Niveau3.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 681 and event.pos[0] >= 500 and event.pos[1] <= 440 and event.pos[1] >= 370:
                    bouclePrincipale(False, False, True, False, False, False, False, False, False, False)
                    bouton_porte.etat = False
                    gameStart = False
                #Porte Niveau 4  
                if event.type == MOUSEMOTION and event.pos[0] <= 901 and event.pos[0] >= 720 and event.pos[1] <= 440 and event.pos[1] >= 370:
                    bouton_Niveau4.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 901 or event.pos[0] <= 720 or event.pos[1] >= 440 or event.pos[1] <= 370):
                    bouton_Niveau4.reinit() 
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 901 and event.pos[0] >= 720 and event.pos[1] <= 440 and event.pos[1] >= 370:
                    bouclePrincipale(False, False, False, True, False, False, False, False, False, False)
                    bouton_porte.etat = False
                    gameStart = False

            ###### BOUTON POUR LE DISTRIBUTEUR ######
            if event.type == MOUSEMOTION and event.pos[0] <= 320 and event.pos[0] >= 100 and event.pos[1] <= 455 and event.pos[1] >= 375 and bouton_distributeur.etat == False:
                bouton_distributeur.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 320 or event.pos[0] <= 100 or event.pos[1] >= 455 or event.pos[1] <= 375) and bouton_distributeur.etat == False:
                bouton_distributeur.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 320 and event.pos[0] >= 100 and event.pos[1] <= 455 and event.pos[1] >= 375:
                bouton_distributeur.select()
                bouton_porte.etat = False
                bouton_distributeur.etat = True
                bouton_hotel.etat = False
                bouton_quitter.etat = False
            

            if bouton_distributeur.etat == True:
                #distributeur Niveau 1
                if event.type == MOUSEMOTION and event.pos[0] <= 681 and event.pos[0] >= 500 and event.pos[1] <= 330 and event.pos[1] >= 245:
                    bouton_Niveau1.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 681 or event.pos[0] <= 500 or event.pos[1] >= 330 or event.pos[1] <= 245):
                    bouton_Niveau1.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 681 and event.pos[0] >= 500 and event.pos[1] <= 330 and event.pos[1] >= 245:
                    bouclePrincipale(False, False, False, False, True, False, False, False, False, False)
                    bouton_distributeur.etat = False
                    gameStart = False

                #distributeur Niveau 2
                if event.type == MOUSEMOTION and event.pos[0] <= 901 and event.pos[0] >= 720 and event.pos[1] <= 330 and event.pos[1] >= 245:
                    bouton_Niveau2.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 901 or event.pos[0] <= 720 or event.pos[1] >= 330 or event.pos[1] <= 245):
                    bouton_Niveau2.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 901 and event.pos[0] >= 720 and event.pos[1] <= 330 and event.pos[1] >= 245:
                    bouclePrincipale(False, False, False, False, False, True, False, False, False, False)
                    bouton_distributeur.etat = False
                    gameStart = False

                """ #distributeur Niveau 3 
                if event.type == MOUSEMOTION and event.pos[0] <= 681 and event.pos[0] >= 500 and event.pos[1] <= 440 and event.pos[1] >= 370:
                    bouton_Niveau3.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 681 or event.pos[0] <= 500 or event.pos[1] >= 440 or event.pos[1] <= 370):
                    bouton_Niveau3.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 681 and event.pos[0] >= 500 and event.pos[1] <= 440 and event.pos[1] >= 370:
                    bouclePrincipale(False, False, False, False, False, False, True, False, False, False)
                    bouton_distributeur.etat = False
                    gameStart = False """ #DISTRIBUTEUR 3 NON FONCTIONNEL


            ###### BOUTON POUR L'HOTEL ######
            if event.type == MOUSEMOTION and event.pos[0] <= 320 and event.pos[0] >= 100 and event.pos[1] <= 575 and event.pos[1] >= 495 and bouton_hotel.etat == False:
                bouton_hotel.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 320 or event.pos[0] <= 100 or event.pos[1] >= 575 or event.pos[1] <= 495) and bouton_hotel.etat == False:
                bouton_hotel.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 320 and event.pos[0] >= 100 and event.pos[1] <= 575 and event.pos[1] >= 495:
                bouton_hotel.select()
                bouton_porte.etat = False
                bouton_distributeur.etat = False
                bouton_hotel.etat = True
                bouton_quitter.etat = False
            
            if bouton_hotel.etat == True:
                
                #Hotel Niveau 1
                if event.type == MOUSEMOTION and event.pos[0] <= 681 and event.pos[0] >= 500 and event.pos[1] <= 330 and event.pos[1] >= 245:
                    bouton_Niveau1.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 681 or event.pos[0] <= 500 or event.pos[1] >= 330 or event.pos[1] <= 245):
                    bouton_Niveau1.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 681 and event.pos[0] >= 500 and event.pos[1] <= 330 and event.pos[1] >= 245:
                    bouclePrincipale(False, False, False, False, False, False, False, True, False, False)
                    bouton_hotel.etat = False
                    gameStart = False

                #Hotel Niveau 2
                if event.type == MOUSEMOTION and event.pos[0] <= 901 and event.pos[0] >= 720 and event.pos[1] <= 330 and event.pos[1] >= 245:
                    bouton_Niveau2.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 901 or event.pos[0] <= 720 or event.pos[1] >= 330 or event.pos[1] <= 245):
                    bouton_Niveau2.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 901 and event.pos[0] >= 720 and event.pos[1] <= 330 and event.pos[1] >= 245:
                    bouclePrincipale(False, False, False, False, False, False, False, False, True, False)
                    bouton_hotel.etat = False
                    gameStart = False

                #Hotel Niveau 3
                if event.type == MOUSEMOTION and event.pos[0] <= 681 and event.pos[0] >= 500 and event.pos[1] <= 440 and event.pos[1] >= 370:
                    bouton_Niveau3.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 681 or event.pos[0] <= 500 or event.pos[1] >= 440 or event.pos[1] <= 370):
                    bouton_Niveau3.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 681 and event.pos[0] >= 500 and event.pos[1] <= 440 and event.pos[1] >= 370:
                    bouclePrincipale(False, False, False, False, False, False, False, False, False, True)
                    bouton_hotel.etat = False
                    gameStart = False


            ###### BOUTON POUR QUITTER ######
            if event.type == MOUSEMOTION and event.pos[0] <= 120 and event.pos[0] >= 40 and event.pos[1] <= 120 and event.pos[1] >= 40 and bouton_quitter.etat == False:
                bouton_quitter.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 120 or event.pos[0] <= 40 or event.pos[1] >= 120 or event.pos[1] <= 40) and bouton_quitter.etat == False:
                bouton_quitter.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 120 and event.pos[0] >= 40 and event.pos[1] <= 120 and event.pos[1] >= 40:
                bouton_quitter.select()
                bouton_porte.etat = False
                bouton_distributeur.etat = False
                bouton_hotel.etat = False
                bouton_quitter.etat = True
            if bouton_quitter.etat == True:
                gameStart = False
                pygame.quit()
                thread_1.var = False


################### FENETRE INTRO JEU   ####################################

def intro():
    gameIntro = True

    fenetre_intro = Terrain("image/scene/intro.jpg")
    bouton_suivant = Bouton("image/boutons/boutonSuivant2.png", "image/boutons/boutonSuivant2Hoover.png", "image/boutons/boutonSuivant2.png")

    while gameIntro == True:
        fenetre = pygame.display.set_mode((1000, 661))
        fenetre.blit(fenetre_intro.fond,(0,0))
        fenetre.blit(bouton_suivant.imageLoad,(720,480))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1 : #On appuie sur 1(&) pour choisir le niveau 1
                            selecteurNiveau()
                            gameIntro = False
                        if event.key == pygame.K_a: #q en azerty pour quitter
                            gameIntro = False
                            pygame.quit()
                            thread_1.var = False
            if event.type == MOUSEMOTION and event.pos[0] <= 881 and event.pos[0] >= 720 and event.pos[1] <= 550 and event.pos[1] >= 480:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 881 or event.pos[0] <= 720 or event.pos[1] >= 550 or event.pos[1] <= 480):
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 881 and event.pos[0] >= 720 and event.pos[1] <= 550 and event.pos[1] >= 480:
                bouton_suivant.select()
                selecteurNiveau()
                gameIntro = False

############ Création du thread #############################

thread_1 = Recevoir()

############## Fonction pour gérer les bouton tkinter ###############

def Start():
    app.destroy()
    thread_1.start()
    intro()

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
    if variable.get() == "5":
        thread_1.nbSerialPort = "5"
    if variable.get() == "6":
        thread_1.nbSerialPort = "6"
    if variable.get() == "7":
        thread_1.nbSerialPort = "7"
    if variable.get() == "8":
        thread_1.nbSerialPort = "8"
    if variable.get() == "9":
        thread_1.nbSerialPort = "9"

def fctderoulant2(*args):
    if variable2.get() == "Windows":
        thread_1.environnementSerial = "COM"
    if variable2.get() == "Linux":
        thread_1.environnementSerial = "/dev/pts/"


#################  FENETRE TKINTER  #########################

OptionList = ["Numéro du port","0","1","2","3","4","5","6","7","8","9"]
OptionList2 = ["Système","Windows", "Linux"]

app = tk.Tk()
app.title("Hack this Mifare Configuration")

app.geometry('866x631')

canvas = Canvas(app, width = 866, height = 380)
canvas.pack()


## Zone blanche ou sont positionner les boutons
zoneOnglet = Frame(app, bg = 'white', width = 800, height = 200)
zoneOnglet.pack_propagate(0) #Evite que la frame ne s'adapte aux boutons
zoneOnglet.pack()

onglet = ttk.Notebook(zoneOnglet)
onglet.pack()

zoneSelection = Frame(onglet, bg = 'white', width = 800, height = 200)
zoneSelection.pack_propagate(0) #Evite que la frame ne s'adapte aux boutons
zoneSelection.pack()


zoneTouches = Frame(onglet, bg = 'white', width = 800, height = 200)
zoneTouches.pack()

onglet.add(zoneSelection, text='Config')
onglet.add(zoneTouches, text='Aide')

imagefond = PhotoImage(file="image/scene/imageConfig.gif")
canvas.create_image(0,0,anchor=NW, image=imagefond)


## Zone de texte pour Config ##

texteDeroulant1 = tk.Label(zoneSelection, bg = 'white', text = "Système d'exploitation", font=('Helvetica', 11))
texteDeroulant1.place(x = 190 , y = 45)

texteDeroulant1 = tk.Label(zoneSelection, bg = 'white', text = "Numéro de port", font=('Helvetica', 11))
texteDeroulant1.place(x = 190 , y = 85)

## Zone de texte pour l'aide ##

texteDeroulant1 = tk.Label(zoneTouches, bg = 'white', text = "Liste des ports pour les différents systèmes d'exploitation :", font=('Helvetica', 11))
texteDeroulant1.place(x = 30 , y = 45)

texteDeroulant1 = tk.Label(zoneTouches, bg = 'white', text = "Windows : Gestionnaire de périphériques -> Ports COM", font=('Helvetica', 11))
texteDeroulant1.place(x = 80 , y = 85)

texteDeroulant1 = tk.Label(zoneTouches, bg = 'white', text = "Linux : Dans le terminal -> ", font=('Helvetica', 11))
texteDeroulant1.place(x = 80 , y = 125)

texteDeroulant1 = tk.Label(zoneTouches, bg = 'white', text = "ls /dev/pts", font=('Courier', 11))
texteDeroulant1.place(x = 260 , y = 125)

## Menu déroulant 1 ##

variable = tk.StringVar(app)
variable.set(OptionList[0])
opt = tk.OptionMenu(zoneSelection, variable, *OptionList)
opt.config(width=15, font=('Helvetica', 12))
opt.place(x = 400, y = 80)
variable.trace("w", fctderoulant1) #application de la fonction pour le menu déroulant 1

## Menu déroulant 2 ##

variable2 = tk.StringVar(app)
variable2.set(OptionList2[0])
opt2 = tk.OptionMenu(zoneSelection, variable2, *OptionList2)
opt2.config(width=15, font=('Helvetica', 12))
opt2.place(x = 400, y = 40)
variable2.trace("w", fctderoulant2) #application de la fonction pour le menu déroulant 2


## Bouton Quitter ##

bouton_quitter = Button(app, text="Quit", command=sys.exit, width=15)  #Bouton quitter
bouton_quitter.place(x = 600, y = 600)

## Bouton Start ##

bouton_start = Button(app, text="Start", command=Start, width=15)   #Bouton Start
bouton_start.place(x = 730, y = 600)

######################  LANCEMENT DU JEU  ################################

app.mainloop()