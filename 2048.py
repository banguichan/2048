
from grille import *
from classement import *
from partie import *
from saisie import *
from pile import*
#importation de tout les fichiers utile pour le deroulement du jeu


game=Partie() #on definie la classe Partie par game
game.partie()#on execute la fonction partie de la classe Partie
while rejouer(): #tant que l utilisateur dit qu il veut rejouer on recommence une partie
    game.partie()
print ("Bien joué votre score est de {}" .format(game.grille.score)) #affiche le score qui vient d etre effectuer 
Score=[] #permet de cree la liste permettant le classement 
Score.append(game.grille.score)
score_append(liste_trier(Score), "Highscore.txt")#on met les score existant trier dans Highscore un fichier texte








