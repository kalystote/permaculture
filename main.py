"""
- créer un tampon pour les nouvelles plantes
- ouvrir la bdd
- ajouter la/les plantes
- fin d'ajout ? (15 max?)
- mise à jour bdd
- fermer bdd

"""

import sqlite3
import package
from package import requetesql

connection = sqlite3.connect("./plantes.db")
cursor = connection.cursor()
tamponplantes = []


def maj_bdd():
    """ajout à la bdd"""
    cursor.executemany("""
    INSERT INTO plantes (nom, taille, typedesol) VALUES (?, ?, ?)""", tamponplantes)
    connection.commit()

class Plante:
    """création structure pour bdd de plantes"""
    def __init__(self):
        self.nom = ""
        self.taille = 0
        self.typesol = ""
        self.arrosage = ""
        self.associations = ""
        self.Datesemis = ""
        self.Temperaturegermination = ""

    "création méthode d'ajout d'un nom de plante"

Planteajoutee = Plante()

def ajoutplante():
    reponse="O"
    while reponse == "O":
        Planteajoutee.nom = input("Quel est le nom de la plante ? ")
        Planteajoutee.taille = input("Quelle est sa taille ? " )
        Planteajoutee.typesol = input("Dans quel type de sol peut-on la planter ? ")
        tamponplantes.append((Planteajoutee.nom, Planteajoutee.taille, Planteajoutee.typesol))
        reponse = input("Faut-il ajouter des plantes (O/N) ? ")

    

def affichageplante():
    #print("le nom de la plante est ", Planteajoutee.nom, " et sa taille est de ", str(Planteajoutee.taille), '\n')
    #print("le type de sol pour cette plante est le suivant : ", Planteajoutee.typesol, '\n')
    print("Les plantes encodées jusqu'à présent sont les suivantes :\n")
    for indexNom in range(len(tamponplantes)):
        print("le nom de la plante est ", tamponplantes[indexNom][0], " et sa taille est de ", str(tamponplantes[indexNom][1]), ' cm\n')
        print("le type de sol pour cette plante est le suivant : ", tamponplantes[indexNom][2], '\n')


'Créer une variable pour le menu (sortir de l appli ou pas)'
reponsemenu=""

"""menu principal"""

while reponsemenu != "Q":
    """ajouter une plante"""
    print("1 ajouter une plante")
    """afficher la plante ajoutée"""
    print("2 afficher la plante ajoutée")
    """mettre à jour la base de donnée"""
    print("3 mettre à jour la base de donnée")
    """afficher le contenu de la base de donnée"""
    print("4 Afficher le contenu de la base de donnée")
    """quitter"""
    print("Q Quitter")
    reponsemenu = input("Quel est votre choix ? ")
    if reponsemenu == "1":
        ajoutplante()
    elif reponsemenu == "2":
        affichageplante()
    elif reponsemenu == "3":
        maj_bdd()
    elif reponsemenu == "4":
        print(requetesql.affichercontenubdd())
    elif reponsemenu == "Q":
        break

# fin de programme main
connection.close()