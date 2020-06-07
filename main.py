import pygame
import serial
import tkinter as tk
import time
from tkinter import ttk
from PIL import Image, ImageTk
from threading import Thread
from pygame.locals import *
from classe import *

pygame.init()
pygame.display.set_caption("Hack this Mifare")



############ Fonctions de la boucle des niveaux  #####################


def bouclePrincipale(boolp1, boolp2, boold1):


####### CREATION DES FONDS ############################

    bouton_quitter = Bouton("image/boutonQuitter.png", "image/boutonQuitterHoover.png", "image/boutonQuitterSelect.png")
    bouton_continuer = Bouton("image/boutonContinuer.png", "image/boutonContinuerHoover.png", "image/boutonContinuerSelect.png")
    bouton_retour = Bouton("image/boutonRetour.png", "image/boutonRetourHoover.png", "image/boutonRetourSelect.png")
    bouton_suivant = Bouton("image/boutonSuivant.png", "image/boutonSuivantHoover.png", "image/boutonSuivantSelect.png")
    bouton_aide = Bouton("image/boutonAide.png", "image/boutonAideHoover.png", "image/boutonAideSelect.png")
    testAide = PanneauNiveau("image/presqueRien.png", "image/texteAide.png")

    fenetre_porteNiveau1 = Terrain("image/scene.jpg")
    fenetre_porteNiveau2 = Terrain("image/scene2.png")
    fenetre_distribNiveau1 = Terrain("image/sceneDistrib1.jpg")
    screen = pygame.image.load("image/screenDistrib1.jpg")

    bouton_coca = Bouton("image/boutonCoca.png", "image/boutonCocac.png", "image/boutonCocaSelect.png")
    bouton_evian = Bouton("image/boutonEvian.png", "image/boutonEvian.png", "image/boutonEvianSelect.png")
    bouton_sprite = Bouton("image/boutonSprite.png", "image/boutonSprite.png", "image/boutonSpriteSelect.png")
    bouton_iceTea = Bouton("image/boutonIceTea.png", "image/boutonIceTea.png", "image/boutonIceTeaSelect.png")


######## CREATION DU TEXTE #############

    texte_coca = texte("Coca", None, 20, "#000000")
    texte_evian = texte("Evian", None, 20, "#000000")
    texte_sprite = texte("Sprite", None, 20, "#000000")
    texte_iceTea = texte("Ice Tea", None, 20, "#000000")
    texte_bienvenue = texte("Bienvenue sur le distributeur !", None, 20, "#000000")
    texte_Objets_Dispo = texte("Objets Disponibles :", None, 20, "#000000")
    texte_Cartes = texte("Veuillez poser votre carte", None, 20, "#000000")
    texte_Selection_Objets = texte("Sélectionnez une boisson", None, 20, "#000000")
    texte_Pas_Bras_Pas_De_Chocolat = texte("Vous ne pouvez pas acheter cet objet. Insérez plus de pièces.", None, 20, "#000000")
    texte_etoiles = texte("***************", None, 20, "#000000")

########### CREATION DU DISTRIBUTEUR #################

    machine = Distributeur()
    item1 = Item('Coca',  2,  2)
    item2 = Item('Evian', 1,  1)
    item3 = Item('Ice Tea',  1.5,  3)
    item4 = Item('Sprite',  2, 1)
    machine.addItem(item1)
    machine.addItem(item2)
    machine.addItem(item3)
    machine.addItem(item4)

####### CREATION DE LA PORTE #########################

    porteN1 = Porte("image/porteOuverte.png","image/porteFerme.png",1)
    porteN2 = Porte("image/porteOuverte2.png","image/porteFerme2.png",1)


####### Création de la fenêtre ########################

    fenetre = pygame.display.set_mode((1000, 661))
    pygame.key.set_repeat(10, 30)

################ BOUCLE DES NIVEAUX #######################
    porteNiveau1 = boolp1
    porteNiveau2 = boolp2
    aide1 = True
    aide2 = True
    distributeurNiveau1 = boold1

    while porteNiveau1 == True:
        thread_1.data = ""
        fenetre.blit(fenetre_porteNiveau1.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (20, 20))
        fenetre.blit(testAide.imageLoad, (60,200))


        if aide1 == True:
            testAide.affichePanneau()
            fenetre.blit(bouton_suivant.imageLoad, (300,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aide1 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (260, 560))
        if porteN1.verouille == 1:
            fenetre.blit(porteN1.imageFerme, (0,0))
        if porteN1.verouille == 0:
            fenetre.blit(porteN1.imageOuverte, (0,0))
            fenetre.blit(bouton_continuer.imageLoad, (20, 560))
        if thread_1.data == "ouvre": #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
            porteN1.verouille = 0

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON POUR RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 233 and event.pos[0] >= 20 and event.pos[1] <= 101 and event.pos[1] >= 20 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 233 or event.pos[0] <= 20 or event.pos[1] >= 101 or event.pos[1] <= 20) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 20 and event.pos[1] <= 101 and event.pos[1] >= 20:
                bouton_retour.select()
                bouton_quitter.etat = False
                bouton_retour.etat = True
                bouton_continuer.etat = False
                selecteurNiveau()
                porteNiveau1 = False
                porteNiveau2 = False
            
            ###### BOUTON POUR CONTINUER QUE SI LA PORTE EST OUVERTE #####
            if porteN1.verouille == 0:
                if event.type == MOUSEMOTION and event.pos[0] <= 233 and event.pos[0] >= 20 and event.pos[1] <= 641 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 233 or event.pos[0] <= 20 or event.pos[1] >= 641 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 20 and event.pos[1] <= 641 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = True
                    porteNiveau1 = False
                    porteNiveau2 = True
                    bouton_continuer.etat = False #Pour rénitialiser le bouton continuer entre les niveaux
            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 513 and event.pos[0] >= 300 and event.pos[1] <= 581 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 513 or event.pos[0] <= 300 or event.pos[1] >= 581 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 513 and event.pos[0] >= 300 and event.pos[1] <= 581 and event.pos[1] >= 500:
                bouton_suivant.select()
                aide1 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 473 and event.pos[0] >= 260 and event.pos[1] <= 641 and event.pos[1] >= 560 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 473 or event.pos[0] <= 260 or event.pos[1] >= 641 or event.pos[1] <= 560) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 473 and event.pos[0] >= 260 and event.pos[1] <= 641 and event.pos[1] >= 560:
                bouton_aide.select()
                aide1 = True

            ########  TOUCHE DU CLAVIER POUR LES TEST ############
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:    #ancien code qui ouvrait la porte avec p
                    porteN1.verouille = 0
                if event.key == pygame.K_c and porteN1.verouille == 0:  #Permet de continuer seulement si la porte a été ouverte
                    porteNiveau1 = False
                    porteNiveau2 = True
                if event.key == pygame.K_r :  #Retourne à la selection de niveau
                    selecteurNiveau()
                    porteNiveau1 = False
                    porteNiveau2 = False
                if event.key == pygame.K_a: #qwerty de base il faut appuyer sur q pour un azerty Permet de quitter
                    porteNiveau1 = False
                    pygame.quit()
                    thread_1.var = False


    while porteNiveau2 == True:
        thread_1.data = ""
        fenetre.blit(fenetre_porteNiveau2.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (20, 20))
        fenetre.blit(testAide.imageLoad, (450,200))

        if aide2 == True:
            testAide.affichePanneau()
            fenetre.blit(bouton_suivant.imageLoad, (700,500))
            fenetre.blit(bouton_aide.imageLoad, (3000,5000))
        if aide2 == False:
            testAide.reinitPanneau()
            fenetre.blit(bouton_suivant.imageLoad, (3000,5000))
            fenetre.blit(bouton_aide.imageLoad, (260, 560))
        if porteN2.verouille == 1:
            fenetre.blit(porteN2.imageFerme, (0,0))
        if porteN2.verouille == 0:
            fenetre.blit(porteN2.imageOuverte, (0,0))
            fenetre.blit(bouton_continuer.imageLoad, (20, 560))
        if thread_1.data == "ouvre2": #permet d'ouvrir la porte quand on recoit le code ouvrir par le port série
            porteN2.verouille = 0


        pygame.display.update()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON POUR RETOUR #####
            if event.type == MOUSEMOTION and event.pos[0] <= 233 and event.pos[0] >= 20 and event.pos[1] <= 101 and event.pos[1] >= 20 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 233 or event.pos[0] <= 20 or event.pos[1] >= 101 or event.pos[1] <= 20) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 20 and event.pos[1] <= 101 and event.pos[1] >= 20:
                bouton_retour.select()
                bouton_quitter.etat = False
                bouton_retour.etat = True
                bouton_continuer.etat = False
                selecteurNiveau()
                porteNiveau1 = False
                porteNiveau2 = False
           
            ###### BOUTON POUR CONTINUER QUE SI LA PORTE EST OUVERTE #####
            if porteN2.verouille == 0:
                if event.type == MOUSEMOTION and event.pos[0] <= 233 and event.pos[0] >= 20 and event.pos[1] <= 641 and event.pos[1] >= 560 and bouton_continuer.etat == False:
                    bouton_continuer.hoover()
                if event.type == MOUSEMOTION and (event.pos[0] >= 233 or event.pos[0] <= 20 or event.pos[1] >= 641 or event.pos[1] <= 560) and bouton_continuer.etat == False:
                    bouton_continuer.reinit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 20 and event.pos[1] <= 641 and event.pos[1] >= 560:
                    bouton_continuer.select()
                    bouton_quitter.etat = False
                    bouton_retour.etat = False
                    bouton_continuer.etat = True
                    selecteurNiveau() #Comme c'est le dernier niveau on retombe sur la sélection de menu """""""A CHANGER SI CE N'EST PLUS LE DERNIER NIVEAU"""""""""
                    porteNiveau1 = False
                    porteNiveau2 = False

            ####### BOUTON SUIVANT DANS L'AIDE  #######
            if event.type == MOUSEMOTION and event.pos[0] <= 913 and event.pos[0] >= 700 and event.pos[1] <= 581 and event.pos[1] >= 500 and bouton_suivant.etat == False:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 913 or event.pos[0] <= 700 or event.pos[1] >= 581 or event.pos[1] <= 500) and bouton_suivant.etat == False:
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 913 and event.pos[0] >= 700 and event.pos[1] <= 581 and event.pos[1] >= 500:
                bouton_suivant.select()
                aide2 = False

            ###### BOUTON AIDE ######

            if event.type == MOUSEMOTION and event.pos[0] <= 473 and event.pos[0] >= 260 and event.pos[1] <= 641 and event.pos[1] >= 560 and bouton_aide.etat == False:
                bouton_aide.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 473 or event.pos[0] <= 260 or event.pos[1] >= 641 or event.pos[1] <= 560) and bouton_aide.etat == False:
                bouton_aide.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 473 and event.pos[0] >= 260 and event.pos[1] <= 641 and event.pos[1] >= 560:
                bouton_aide.select()
                aide2 = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:    #ancien code qui ouvrait la porte avec p
                    porteN2.verouille = 0
                if event.key == pygame.K_c and porteN2.verouille == 0 : #Permet de continuer seulement si la porte a été ouverte
                    selecteurNiveau() #Comme c'est le dernier niveau on retombe sur la sélection de menu """""""A CHANGER SI CE N'EST PLUS LE DERNIER NIVEAU"""""""""
                    porteNiveau1 = False
                    porteNiveau2 = False
                if event.key == pygame.K_r :  #Retourne à la selection de niveau
                    selecteurNiveau()
                    porteNiveau1 = False
                    porteNiveau2 = False
                if event.key == pygame.K_a: #qwerty de base il faut appuyer sur q pour un azerty
                    porteNiveau2 = False
                    pygame.quit()
                    thread_1.var = False


    while distributeurNiveau1 == True:
        thread_1.data = ""

        fenetre.blit(fenetre_distribNiveau1.fond,(0,0))
        fenetre.blit(bouton_retour.imageLoad, (20, 20))
        fenetre.blit(bouton_coca.imageLoad, (0, 0))
        fenetre.blit(bouton_evian.imageLoad, (0, 0))
        fenetre.blit(bouton_sprite.imageLoad, (0, 0))
        fenetre.blit(bouton_iceTea.imageLoad, (0, 0))
        fenetre.blit(testAide.imageLoad, (60,200))
        fenetre.blit(texte_bienvenue, (355, 85))
        fenetre.blit(texte_etoiles, (355, 95))
        fenetre.blit(texte_Cartes, (355, 105))
        fenetre.blit(texte_etoiles, (355, 115))

        try:
            machine.solde = int(thread_1.data)
        except ValueError:
            pass

        if machine.solde >= 0:

            fenetre.blit(texte_Selection_Objets, (355, 125))
            fenetre.blit(texte_etoiles, (355, 135))
            pygame.display.flip()

            if bouton_coca.etat == True:
                ########### GET ITEM ###########
                item = machine.getItem("Coca")
                            
                ########## BUY ITEM ############

                if machine.solde < item.price:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    bouton_coca.etat = False

                else:
                    machine.solde -= item.price
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name), None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Argent restant : " + str(machine.solde), None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    ######### CHECK REFUND #########
                    if machine.solde > 0:
                        fenetre.blit(texte(str(machine.solde) + "€ rendu.", None, 20, "#000000"), (355,125))
                        fenetre.blit(texte_etoiles, (355, 135))
                        fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                        fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    bouton_coca.etat = False


            if bouton_evian.etat == True:
                ########### GET ITEM ###########
                item = machine.getItem("Evian")
                            
                ########## BUY ITEM ############

                if machine.solde < item.price:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    bouton_evian.etat = False

                else:
                    machine.solde -= item.price
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name), None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Argent restant : " + str(machine.solde), None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    ######### CHECK REFUND #########
                    if machine.solde > 0:
                        fenetre.blit(texte(str(machine.solde) + "€ rendu.", None, 20, "#000000"), (355,125))
                        fenetre.blit(texte_etoiles, (355, 135))
                        fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                        fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    bouton_evian.etat = False


            if bouton_sprite.etat == True:
                ########### GET ITEM ###########
                item = machine.getItem("Sprite")
                            
                ########## BUY ITEM ############

                if machine.solde < item.price:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    bouton_sprite.etat = False

                else:
                    machine.solde -= item.price
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name), None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Argent restant : " + str(machine.solde), None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    ######### CHECK REFUND #########
                    if machine.solde > 0:
                        fenetre.blit(texte(str(machine.solde) + "€ rendu.", None, 20, "#000000"), (355,125))
                        fenetre.blit(texte_etoiles, (355, 135))
                        fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                        fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    bouton_sprite.etat = False


            if bouton_iceTea.etat == True:
                ########### GET ITEM ###########
                item = machine.getItem("Ice Tea")
                            
                ########## BUY ITEM ############

                if machine.solde < item.price:
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte_Pas_Bras_Pas_De_Chocolat, (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    bouton_iceTea.etat = False

                else:
                    machine.solde -= item.price
                    item.buyFromStock()
                    fenetre.blit(screen, (355,85))
                    fenetre.blit(texte("Vous avez acheté : " + str(item.name), None, 20, "#000000"), (355,85))
                    fenetre.blit(texte_etoiles, (355, 95))
                    fenetre.blit(texte("Argent restant : " + str(machine.solde), None, 20, "#000000"), (355,105))
                    fenetre.blit(texte_etoiles, (355, 115))

                    ######### CHECK REFUND #########
                    if machine.solde > 0:
                        fenetre.blit(texte(str(machine.solde) + "€ rendu.", None, 20, "#000000"), (355,125))
                        fenetre.blit(texte_etoiles, (355, 135))
                        fenetre.blit(texte("Bonne Journée !", None, 20, "#000000"), (355,145))
                        fenetre.blit(texte_etoiles, (355, 155))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    bouton_iceTea.etat = False

        pygame.display.update()




        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            ###### BOUTON POUR QUITTER #####
            if event.type == MOUSEMOTION and event.pos[0] <= 233 and event.pos[0] >= 20 and event.pos[1] <= 101 and event.pos[1] >= 20 and bouton_quitter.etat == False:
                bouton_retour.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 233 or event.pos[0] <= 20 or event.pos[1] >= 101 or event.pos[1] <= 20) and bouton_quitter.etat == False:
                bouton_retour.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 233 and event.pos[0] >= 20 and event.pos[1] <= 101 and event.pos[1] >= 20:
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
                bouton_coca.select()
                bouton_coca.etat = True

                
            ###### BOUTON EVIAN ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_evian.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 365 and event.pos[1] >= 334:
                bouton_evian.select()
                bouton_evian.etat = True

            ###### BOUTON SPRITE ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_sprite.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 404 and event.pos[1] >= 373:
                bouton_sprite.select()
                bouton_sprite.etat = True

            ####### BOUTON ICE TEA ######
            if event.type == MOUSEBUTTONUP and event.button == 1:
                bouton_iceTea.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 642 and event.pos[0] >= 585 and event.pos[1] <= 442 and event.pos[1] >= 411:
                bouton_iceTea.select()
                bouton_iceTea.etat = True




############ Fonction menu principale selection des niveaux  #############################


def selecteurNiveau(): #
    """
    Premiere interface : menu principal qui permet de sélectionner un niveau
    """

    gameStart = True

    fenetre_selection = Terrain("image/sceneIntro.jpg")
    bouton_porte = Bouton("image/boutonPorte.png", "image/boutonPorteHoover.png", "image/boutonPorteSelect.png")
    bouton_distributeur = Bouton("image/boutonDistributeur.png", "image/boutonDistributeurHoover.png", "image/boutonDistributeurSelect.png")
    bouton_hotel = Bouton("image/boutonHotel.png", "image/boutonHotelHoover.png", "image/boutonHotelSelect.png")
    bouton_quitter = Bouton("image/boutonQuitter.png", "image/boutonQuitterHoover.png", "image/boutonQuitterSelect.png")
    panneauPorte = PanneauNiveau("image/presqueRien.png", "image/niveauPorte.png")
    panneauDistributeur = PanneauNiveau("image/presqueRien.png", "image/niveauDistributeur.png")
    panneauHotel = PanneauNiveau("image/presqueRien.png", "image/niveauHotel.png")

    while gameStart == True:
        fenetre = pygame.display.set_mode((1000, 661))
        fenetre.blit(fenetre_selection.fond,(0,0))
        fenetre.blit(bouton_porte.imageLoad,(200,255))
        fenetre.blit(bouton_distributeur.imageLoad,(200, 355))
        fenetre.blit(bouton_hotel.imageLoad, (200, 455))
        fenetre.blit(bouton_quitter.imageLoad, (200, 555))
        fenetre.blit(panneauPorte.imageLoad, (475,200))
        fenetre.blit(panneauDistributeur.imageLoad, (475,200))
        fenetre.blit(panneauHotel.imageLoad, (475,200))
        pygame.display.update()


        if bouton_porte.etat == True:
            panneauPorte.affichePanneau()
            panneauDistributeur.reinitPanneau()
            panneauHotel.reinitPanneau()
        if bouton_distributeur.etat == True:
            panneauPorte.reinitPanneau()
            panneauDistributeur.affichePanneau()
            panneauHotel.reinitPanneau()
        if bouton_hotel.etat == True:
            panneauPorte.reinitPanneau()
            panneauDistributeur.reinitPanneau()
            panneauHotel.affichePanneau()


        for event in pygame.event.get():
            ###### BOUTON POUR LA PORTE #####
            if event.type == MOUSEMOTION and event.pos[0] <= 413 and event.pos[0] >= 200 and event.pos[1] <= 336 and event.pos[1] >= 255 and bouton_porte.etat == False:
                bouton_porte.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 413 or event.pos[0] <= 200 or event.pos[1] >= 336 or event.pos[1] <= 255) and bouton_porte.etat == False:
                bouton_porte.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 413 and event.pos[0] >= 200 and event.pos[1] <= 336 and event.pos[1] >= 255:
                bouton_porte.select()
                bouton_porte.etat = True
                bouton_distributeur.etat = False
                bouton_hotel.etat = False
                bouton_quitter.etat = False

            if bouton_porte.etat == True:
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 700 and event.pos[0] >= 525 and event.pos[1] <= 320 and event.pos[1] >= 245:
                    bouclePrincipale(True,False, False)
                    bouton_porte.etat = False
                    gameStart = False
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 905 and event.pos[0] >= 730 and event.pos[1] <= 320 and event.pos[1] >= 245:
                    bouclePrincipale(False,True,False)
                    bouton_porte.etat = False
                    gameStart = False

            ###### BOUTON POUR LE DISTRIBUTEUR ######
            if event.type == MOUSEMOTION and event.pos[0] <= 413 and event.pos[0] >= 200 and event.pos[1] <= 436 and event.pos[1] >= 355 and bouton_distributeur.etat == False:
                bouton_distributeur.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 413 or event.pos[0] <= 200 or event.pos[1] >= 436 or event.pos[1] <= 355) and bouton_distributeur.etat == False:
                bouton_distributeur.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 413 and event.pos[0] >= 200 and event.pos[1] <= 436 and event.pos[1] >= 355:
                bouton_distributeur.select()
                bouton_porte.etat = False
                bouton_distributeur.etat = True
                bouton_hotel.etat = False
                bouton_quitter.etat = False

            if bouton_distributeur.etat == True:
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 700 and event.pos[0] >= 525 and event.pos[1] <= 320 and event.pos[1] >= 245:
                    bouclePrincipale(False,False,True)
                    bouton_distributeur.etat = False
                    gameStart = False


            ###### BOUTON POUR L'HOTEL ######
            if event.type == MOUSEMOTION and event.pos[0] <= 413 and event.pos[0] >= 200 and event.pos[1] <= 536 and event.pos[1] >= 455 and bouton_hotel.etat == False:
                bouton_hotel.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 413 or event.pos[0] <= 200 or event.pos[1] >= 536 or event.pos[1] <= 455) and bouton_hotel.etat == False:
                bouton_hotel.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 413 and event.pos[0] >= 200 and event.pos[1] <= 536 and event.pos[1] >= 455:
                bouton_hotel.select()
                bouton_porte.etat = False
                bouton_distributeur.etat = False
                bouton_hotel.etat = True
                bouton_quitter.etat = False

            ###### BOUTON POUR QUITTER ######
            if event.type == MOUSEMOTION and event.pos[0] <= 413 and event.pos[0] >= 200 and event.pos[1] <= 636 and event.pos[1] >= 555 and bouton_quitter.etat == False:
                bouton_quitter.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 413 or event.pos[0] <= 200 or event.pos[1] >= 636 or event.pos[1] <= 555) and bouton_quitter.etat == False:
                bouton_quitter.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 413 and event.pos[0] >= 200 and event.pos[1] <= 636 and event.pos[1] >= 555:
                bouton_quitter.select()
                bouton_porte.etat = False
                bouton_distributeur.etat = False
                bouton_hotel.etat = False
                bouton_quitter.etat = True
            if bouton_quitter.etat == True:
                
                gameStart = False
                pygame.quit()
                thread_1.var = False

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

################### FENETRE INTRO JEU   ####################################

def intro():
    gameIntro = True

    fenetre_intro = Terrain("image/intro.png")
    bouton_suivant = Bouton("image/boutonSuivant.png", "image/boutonSuivantHoover.png", "image/boutonSuivantSelect.png")

    while gameIntro == True:
        fenetre = pygame.display.set_mode((1000, 661))
        fenetre.blit(fenetre_intro.fond,(0,0))
        fenetre.blit(bouton_suivant.imageLoad,(700,530))
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
            if event.type == MOUSEMOTION and event.pos[0] <= 913 and event.pos[0] >= 700 and event.pos[1] <= 611 and event.pos[1] >= 530:
                bouton_suivant.hoover()
            if event.type == MOUSEMOTION and (event.pos[0] >= 913 or event.pos[0] <= 700 or event.pos[1] >= 611 or event.pos[1] <= 530):
                bouton_suivant.reinit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] <= 913 and event.pos[0] >= 700 and event.pos[1] <= 611 and event.pos[1] >= 530:
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
    if variable3.get() == "5":
        #thread_1.nbSerialPort = "4"
        print("")
    if variable3.get() == "6":
        #thread_1.nbSerialPort = "4"
        print("")
    if variable3.get() == "7":
        #thread_1.nbSerialPort = "4"
        print("")
    if variable3.get() == "8":
        #thread_1.nbSerialPort = "4"
        print("")
    if variable3.get() == "9":
        #thread_1.nbSerialPort = "4"
        print("")


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
onglet.add(zoneTouches, text='Les touches du clavier')

imagefond = PhotoImage(file="image/imageConfig.gif")
canvas.create_image(0,0,anchor=NW, image=imagefond)


## Zone de texte pour Config ##

texteDeroulant1 = tk.Label(zoneSelection, bg = 'white', text = "Système d'exploitation", font=('Helvetica', 11))
texteDeroulant1.place(x = 190 , y = 45)

texteDeroulant1 = tk.Label(zoneSelection, bg = 'white', text = "Numéro de port", font=('Helvetica', 11))
texteDeroulant1.place(x = 190 , y = 85)

texteDeroulant1 = tk.Label(zoneSelection, bg = 'white', text = "Numéro de port du lecteur", font=('Helvetica', 11))
texteDeroulant1.place(x = 190 , y = 125)

## Zone de texte pour les touches du clavier ##

texteDeroulant1 = tk.Label(zoneTouches, bg = 'white', text = "Q pour quitter", font=('Helvetica', 11))
texteDeroulant1.place(x = 360 , y = 45)

texteDeroulant1 = tk.Label(zoneTouches, bg = 'white', text = "R pour retourner à la sélection de niveau", font=('Helvetica', 11))
texteDeroulant1.place(x = 280 , y = 85)

texteDeroulant1 = tk.Label(zoneTouches, bg = 'white', text = "C pour continuer une fois la porte ouverte", font=('Helvetica', 11))
texteDeroulant1.place(x = 275 , y = 125)

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

## Menu déroulant 2 ##

variable3 = tk.StringVar(app)
variable3.set(OptionList[0])
opt3 = tk.OptionMenu(zoneSelection, variable3, *OptionList)
opt3.config(width=15, font=('Helvetica', 12))
opt3.place(x = 400, y = 120)
variable2.trace("w", fctderoulant3) #application de la fonction pour le menu déroulant 2


## Bouton Quitter ##

bouton_quitter = Button(app, text="Quit", command=quit, width=15)  #Bouton quitter
bouton_quitter.place(x = 600, y = 600)

## Bouton Start ##

bouton_start = Button(app, text="Start", command=Start, width=15)   #Bouton Start
bouton_start.place(x = 730, y = 600)

######################  LANCEMENT DU JEU  ################################

app.mainloop()
