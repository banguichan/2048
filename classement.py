

def fichier_vers_liste(nom_fichier, separateur = " "):
    """
    Entrée : une chaîne de caractères correspondante au nom d'un fichier
    Sortie : la liste des lignes du fichier, chaque ligne étant donnée sous forme de la liste de ses mots (séparés par un espace par défaut)
    """
    L = []
    try :
       with open(nom_fichier, "r") as f:    # permet d'ouvrir un fichier et de le fermer automatiquement
            for ligne in f:                 # parcour du fichier ligne par ligne
#                L.append(ligne)             # ajoute a une certaine ligne
                L.append(ligne.split(separateur)) #le split permet de separe dans une liste les mots
    except FileNotFoundError:               # au cas où le fichier n'existe pas (et dans ce cas, la liste reste vide et revient à créer un fichier vide)
        pass
    return L


def creer_fichier(Score, nom_fichier, separateur=","):
    with open(nom_fichier, "w") as F:
        for i in range(len(Score)):
            F.write(str(Score[i]))  # Écrit l'élément de Score
            if i < len(Score) - 1:
                F.write(separateur)  # Ajoute le séparateur s'il ne s'agit pas du dernier élément
        F.write("\n")  # Ajoute un saut de ligne pour terminer la ligne


def scinder_liste(Score):
    return Score[:len(Score)//2] , Score[len(Score)//2:]   



def fusionner_listes_triees_recursif (Score1, Score2):
    # on s'assure que les listes données en entrée sont bien triées (sinon on renvoit un message d'erreur) :
    assert Score1 == sorted(Score1) and Score2 == sorted(Score2), "Les listes données en arguments de la fonction de fusion de listes doivent être données déjà triées"
    if Score1 == []:
        return Score2
    elif Score2 == []:
        return Score1
    elif Score1[0] < Score2[0]:
        return [Score1[0]] + fusionner_listes_triees_recursif(Score1[1:], Score2)
    else:
        return [Score2[0]] + fusionner_listes_triees_recursif(Score1, Score2[1:]) #on fusionne les listes trier par recursivite


def tri_fusion(Score):
    if len(Score) <= 1: # cas si il n y a que 1 element ou 0
        return Score
    else:           #on coupe la liste et fusionne grace au fonction precedente
        Score1, Score2 = scinder_liste(Score)
        return fusionner_listes_triees_recursif(tri_fusion(Score1), tri_fusion(Score2))

def liste_trier(Score):
    Scores=[]
    for i in range (len(tri_fusion(Score))):#on retourne la liste pour avoir d abbord le plus grand score
        Scores = tri_fusion(Score)[::-1]
        
    return Scores








# TESTS
def score_append(Score, nom_fichier, separateur=" "):
    
    L_donnees=[]
    print("Liste des données du fichier :", L_donnees)
    for i in range(len(Score)): #on met dans la liste L_donnees la liste trier sous forme de texte et non chiffre
        L_donnees.append([str(liste_trier(tri_fusion(Score))[i])])
    creer_fichier(L_donnees, nom_fichier, separateur) #on cree le fichier highscore en appelant la fonction precedente creer fichier
    print("""
    ----- Top 10 score (classement personnel): ------
    rank                          score
    -------------------------------------------------
    """)#permet d afficher a l utilisateur la grille de ses scores
    for i in range (len (L_donnees)):
        print(i+1,".                               ",L_donnees[i])




