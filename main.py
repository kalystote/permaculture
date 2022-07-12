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
from package import *

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
        fonctions.ajoutplante()
    elif reponsemenu == "2":
        fonctions.affichageplante()
    elif reponsemenu == "3":
        requetesql.maj_bdd(fonctions.tamponplantes)
    elif reponsemenu == "4":
        print(requetesql.affichercontenubdd())
    elif reponsemenu == "Q":
        break

# fin de programme main
