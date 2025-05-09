from random import randint 

class Grille:

    



    def __init__(self):

        self.taille=4                                                               #Les dimentions de la grille sont determiné par cet attribut
        self.valeur=[]
        for i in range (self.taille):
            self.valeur.append([])
            for j in range (self.taille):
                self.valeur[i].append(0)
        self.objectif=2048                                                          #L'objectif de la partie est défini par cet attribut
        self.score = 0 


    
    def deux_ou_quatre(self):                #Cette méthode permet de déterminer si un 2 ou un 4 va apparaitre dans la grille
        ajo=0
        n=randint(1,5)                       
        if n==5:                             #Si le nombre tiré au hasard par la fonction randint est 5, on ajoute 4 à la grille. Etant donné que les nombres pouvant etre tirés au sort vont de 1 à 5, on a 20% de chance qu'un 4 apparaisse
            ajo=4
        else:
            ajo=2
        return ajo
    
    def ajouter(self):
        
        i=randint(0,self.taille-1)           # On tire deux nombres au hasard ne dépassant pas la taille de la grille
        j=randint(0,self.taille-1)
        while self.valeur[i][j]!=0:        # On effectue le tirage à nouveau si les deux nombres en question ne correspondent pas à la longeur et la largeur d'un emplacement vide
            i=randint(0,self.taille-1)
            j=randint(0,self.taille-1)
        self.valeur [i][j]= self.deux_ou_quatre()     #Un fois qu'un emplacement vide a été tiré au sort, on ajoute le nombre 2 ou 4
        

    




        



        
            



    
 

    
    def afficher(self):
        for i in range(self.taille):
            print()
            print(" ---------"*self.taille)          #On met autant de barre horizontal que la taille de la largeur de la grille
            for j in range(3):
                print()
                for k in range (self.taille):
                    if j==1:
                        if self.valeur [i][k]==0:                                             #au milieu de chaque case, on affiche le numéro correspondant à la case
                            print ("|{:^8}|".format("."),end="") 
                        else: 
                            print ("|{:^8}|".format(self.valeur [i][k]),end="") 

                             
                    else:
                        print ("|        |",end="")                        #si nous ne somme pas au milieu de la case, l'affichage est le meme mais sans le numéro
        print()
        print(" ---------"*self.taille)                  # On rajoute une barre horizontale pour fermer la grille en bas  


    def dep_haut(self):                               #On définit d'abord le déplacement des valeurs
        for i in range (self.taille):                 #on parcours la grille colonne par colonne
            j=1
            while j<self.taille:                     #équivalent d'une boucle range 
                aux=j                                #aux correspond au numéro des lignes que nous parcourons
                while self.valeur[aux-1][i]==0 and aux>0:         #On déplace vers le haut les éléments d'une colonne, ligne par ligne en commencant par placer sur la premiere ligne les éléments si situant sur la deuxième ligne
                
                    self.valeur [aux-1][i]= self.valeur [aux][i]     
                    self.valeur [aux][i]=0                         #Après avoir monté la valeur correspondante, on met un "." dans la case dans laquelle le numéro était auparavant
                    aux=aux-1                                        #Apres avoir passé un élément dans la case superieur, cette action nous invite à répéter la meme opération si on peut mettre le numéro dans une case supérieur 
                j=j+1                                 #on incrémente j de cette manière afin de pouvoir passer plusieus fois sur les memes colonnes
        
        
    def fus_haut(self):                              #Cette méthode permet de faire fusionner les valeurs lors d'un déplacement vers le haut
        for i in range (1,self.taille):
            for j in range (self.taille):
                if self.valeur[i][j]==self.valeur[i-1][j]!=0:         #Si une ligne ainsi que la ligne du dessus ont la même valeur sur une  même colonne, on fait fusionner les valeurs
                    self.valeur[i-1][j]=self.valeur[i][j]*2             #Les valeurs fusionnent 
                    self.valeur [i][j]=0                             #On replace la case du bas de la fusion par un "."
                    self.score = self.score+self.valeur[i-1][j]*2  
        


    def dep_bas(self):                                           ##Les opérations sont similaires pour le deplacement vers le bas 
        for i in range (self.taille):
            j=self.taille-2
            while j>=0:
                aux=j
                while aux+1<self.taille and self.valeur[aux+1][i]==0:
                
                    self.valeur [aux+1][i]= self.valeur [aux][i]
                    self.valeur [aux][i]=0
                    aux=aux+1
                j=j-1
        return self.valeur

    def fus_bas(self):                              
        for i in range (self.taille):
            j=self.taille-1
            while j>0:
                if self.valeur[j][i]==self.valeur[j-1][i]!=0:
                    self.valeur[j][i]=self.valeur[j][i]*2
                    self.valeur [j-1][i]=0
                    self.score = self.score + self.valeur[j][i]*2  
                j=j-1
        return self.valeur
    

    def dep_gauche(self):
        for i in range(self.taille):
            j=1
            while j<self.taille:
                aux=j
                while aux>0 and self.valeur[i][aux-1]==0:
                
                    self.valeur [i][aux-1]= self.valeur [i][aux]
                    self.valeur [i][aux]=0
                    aux=aux-1
                j=j+1
        return self.valeur
    

    def fus_gauche(self):
        for i in range (1,self.taille):
            for j in range (self.taille):
                if self.valeur[j][i]==self.valeur[j][i-1]!=0:
                    self.valeur[j][i-1]=self.valeur[j][i]*2
                    self.valeur [j][i]=0
                    self.score=self.score+self.valeur[j][i-1]*2  
        return self.valeur
    
    def dep_droit(self):
        for i in range (self.taille):
            j=self.taille-2
            while j>=0:
                aux=j
                while aux+1<self.taille and self.valeur[i][aux+1]==0:
                
                    self.valeur [i][aux+1]= self.valeur [i][aux]
                    self.valeur [i][aux]=0
                    aux=aux+1
                j=j-1
        return self.valeur
    
    def fus_droit(self):
        for i in range (self.taille):
            j=self.taille-1
            while j>0:
                if self.valeur[i][j]==self.valeur[i][j-1]!=0:
                    self.valeur[i][j]=self.valeur[i][j]*2
                    self.valeur [i][j-1]=0
                    self.score=self.score+self.valeur[i][j]*2  
                j=j-1
        return self.valeur
    


    def mouv_droit(self):            #On combine les méthodes crées précedemnt pour créer des méthodes qui combinent les mouvements
        self.dep_droit()             #On déplace d'abord les éléments
        self.fus_droit()             #On fusionne les éléments
        self.dep_droit()             #On les déplace à nouveau si nécéssaire
        return self.valeur

    




        


    




            

        


 
    

    def mouv_haut(self):
        self.dep_haut()
        self.fus_haut()
        self.dep_haut()
        return self.valeur
    
    def mouv_bas(self):
        self.dep_bas()
        self.fus_bas()
        self.dep_bas()
        return self.valeur
    
    def mouv_gauche(self):
        self.dep_gauche()
        self.fus_gauche()
        self.dep_gauche()
        return self.valeur
    

    
    

    def partie_gagne(self):                       
        for i in range (self.taille):              #On parcours la grille
            for j in range (self.taille):
                if self.valeur[i][j]==self.objectif:      #Si l'un des éléments est l'objectif on propose au joueur de continuer ou non la partie
                    print ("Bravo vous avez atteint", self.objectif)
                    a=str(input("Voulez vous continuer la partie ? (oui ou non): "))
                    while a!="oui" and a!="non":         #Si je joueur n'a pas saisi oui ou non, le code lui demande ressaisir jusqu'à ce l'utilisateur saisisse oui ou non
                        a=str(input("Voulez vous continuer la partie ? (oui ou non): "))
                    if a=="oui":
                        self.objectif = self.objectif*2                  #Si l'utilisateur écrit "oui" , on double l'objectif 
                        return False                                    #La fonction retourne faux car la partie n'est pas terminé 
                    else:
                        return True                                     #Si l'utilisateur écrit "non", on retourne True car la partie est terminé
        return False                                                    #La fonction retourne False par défaut quand l'objectif n'est pas accompli car la partie n'est pas terminé
                    
                    
                    



                    
                
         
    
    def partie_perdu(self):
        for i in range (self.taille):
            for j in range (self.taille):              #On parcours la liste
                if self.valeur[i][j]==0:             #Si l'une des cases ne contient pas de valeur, on retourne False car la partie continue
                    return False
                else:
                    if self.valeur==self.mouv_haut and self.valeur==self.mouv_droit:
                        return True
        return  False                                  #  Sinon on retourne True car la partie est terminé
    

    
    

    



    








    














    
                





    
                






    
    



    




        




                

                

        

        
        
        




                
        
