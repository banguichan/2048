from grille import *

class Pile:


    def __init__(self):
        self.memoire=[]
    
    def __est_vide__(self):
        return self.memoire == []
    
    def __depiler__(self):
        if not(self.__est_vide__()):
            return self.memoire.pop()
        
    
    def __empiler__(self, a):
        return self.memoire.append(a)
    
    def __str__(self):
        s=""
        for i in range(len(self.memoire)):
            s=s+str(self.memoire[i])+"\n"
        return s
    
    
        
        
    

    def sauvegarder(self, fichier):
        # Sauvegarde la pile dans un fichier externe
        with open(fichier, 'w') as f:
            for element in self.memoire:
                f.write(str(element) + '\n')

    def charger(self, fichier):
        # Charge la pile depuis un fichier externe
        with open(fichier, 'r') as f:
            lines = f.readlines()
            
            self.memoire = [int(line.strip()) for line in lines]
    



def grille_avec_zero(G):
    Grille_entier=Grille()
    for i in range (G.taille):
        for j in range(G.taille):
            if G.valeur[i][j]==".":
                Grille_entier.valeur[i][j]=0
    return Grille_entier




def grille_en_pile(G):
    P=Pile()
    for i in range (G.taille):
        for j in range (G.taille):
            P.__empiler__(G.valeur[i][j])
    return P

def retourner_pile(P):
    Q=Pile()
    while not (P.__est_vide__()):
        Q.__empiler__(P.__depiler__())
    return Q



def pile_en_grille(P):
    Q=retourner_pile(P)
    
    
    G=Grille()
    for i in range (G.taille):
        for j in range (G.taille):
            
            G.valeur[i][j]=Q.__depiler__()
    return G












def sauvegarde(G,fichier):
    P=grille_en_pile((G))
    P.sauvegarder("last_games.bk")


def charge(fichier):
    P=Pile()
    P.charger("last_games.bk")
    G=pile_en_grille(P)
    return G










        



    

    














        





    



    








    
    



        







    








    
    



        











    
    
        
        
        


    


    

    
