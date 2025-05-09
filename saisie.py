import msvcrt
from pile import*
    

# saisie de caractere en ligne 
def saisie_caractere_en_ligne_windows():
    """
    Fonction de détection windows et de récupération d'une touche clavier frappée
    """
    while True:
        if msvcrt.kbhit():      # Récupération d'une saisie, sinon getch permet de lire en permanence le clavier
            ch = msvcrt.getch() # Permets de lire le caractère qui a ete saisie 
            return ch


def saisir(L_choix):
    """
    Fonction de saisie en ligne d'un caractère figurant dans la liste des choix autorisés
    Attention : ne permet de saisir qu'un seul caractère, sans appuyer sur entrée
    """
    while True:
        caractere_saisi = saisie_caractere_en_ligne_windows().decode()  #retourne un type byte
        try:
            assert caractere_saisi in L_choix    #Possibilité de rajoute des assert si nécessaires                         
            break
        except ValueError:
            pass
        except AssertionError:
            pass
        #Vérifie les erreurs
    return caractere_saisi



def saisir_caractere():


    liste_caracteres_autorises = ["e", "q", "s","d","z","r"]    #Caractère prit en compte 
    char = saisir(liste_caracteres_autorises)
    #Permets d'enregistrer quel mouvement faire suite a l execution dans saisi 
    #e permet de sortir du programme pour terminer la partie pour ne pas etre bloque (e pour end)
    while char != "e":
        if char == "z":
            return"z"
        elif char == "q":
            return"q"
        elif char == "d":
            return"d"
        elif char == "s":
            return"s"
        elif char=="r":
            return"r"
        else:
            pass
        char = saisir(liste_caracteres_autorises)
    print("Vous avez saisi 'e', fin de partie ")
    return "e"

def rejouer(): #demande au joueur s'il souhaite refaire une partie
    rejouer =str(input("Voulez vous rejouer une partie ? (veuillez saisir oui ou non): "))
    while rejouer!="oui" and rejouer!="non":
        rejouer = str(input("veuillez saisir oui ou non : "))
    if rejouer=="oui":
        return True
    elif rejouer=="non":
        return False
        

def continuer():#demande au joueuer si il souhaite continuer
    continuer=str(input("Voulez vous continuer la partie (saisir oui ou non): "))
    while continuer!="oui" and continuer!="non":
        continuer=str(input("veuillez saisir oui ou non"))
        if continuer=="oui":
            return True
        elif continuer=="non":
            return False
        
