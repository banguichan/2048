import msvcrt
from grille import *
from saisie import *
from classement import *
from pile import *


class Partie:

    def __init__ (self):
        self.grille=Grille()
        self.historique=Pile()
        
        

    def partie (self):
        print("""
             BIENVENUE SUR LE JEU 2048 
Les regles du jeu sont simples, votre but et d additionner
les cases pour debloquer la case de valeur 2048 
Pour aller vers le haut il vous suffit d appuyer sur z
vers le bas s, vers la gauche q et vers la droite d 
Pour arreter la partie il vous suffit de presser sur le bouton e
vous allez pouvoir sauvegarder la partie en cours ou arreter la partie 
et votre score serra trier dans le classement
Pour revenir au mouvement precedent presser le bouton r
                BONNE PARTIE A VOUS

      """)
            
        if continuer():
            self.grille=charge("last_games.bk")

        else:
            self.grille.ajouter()
            self.grille.ajouter()
        car="z"
        retour=0
        while self.grille.partie_gagne()==False and self.grille.partie_perdu()==False and car!="e":
            
            G=self.grille
            G.afficher()
            

            
            car = saisir_caractere()
            if car=="z":
                sauvegarde(self.grille,"last_games.bk")
                self.grille.mouv_haut()
                self.grille.ajouter()
            elif car=="s":
                sauvegarde(self.grille,"last_games.bk")
                self.grille.mouv_bas()
                self.grille.ajouter()
            elif car=="q":
                sauvegarde(self.grille,"last_games.bk")
                self.grille.mouv_gauche()
                self.grille.ajouter()
            elif car=="d":
                sauvegarde(self.grille,"last_games.bk")
                self.grille.mouv_droit()
                self.grille.ajouter()
            elif car=="r" and retour>=10:
                self.grille=charge("last_games.bk")
                retour=0
            elif car=="e":
                sauv=str(input("voulez vous sauvegarder la partie oui ou non : "))
                while sauv!="oui" and sauv!="non":
                    sauv=str(input("voulez vous sauvegarder la partie oui ou non : "))
                if sauv=="oui":
                    sauvegarde(self.grille,"last_games.bk")
            else:
                pass
            
            
            retour=retour+1
        
            
            
            








        
