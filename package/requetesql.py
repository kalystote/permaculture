import sqlite3

def affichercontenubdd():
    connection = sqlite3.connect("./plantes.db")
    cursor = connection.cursor()    
    cursor.execute("SELECT * FROM plantes")
    plantedelabdd = cursor.fetchall()
    #return plantedelabdd[0][1], plantedelabdd[1][1], plantedelabdd[2][1]
    for indexNom in range(len(plantedelabdd)):
        print("le nom de la plante est ", plantedelabdd[indexNom][1], " et sa taille est de ", str(plantedelabdd[indexNom][2]), ' cm\n')
        print("le type de sol pour cette plante est le suivant : ", plantedelabdd[indexNom][3], '\n')
    """ [(1, 'lavande', 40, 'terreau ou pleine terre'), (2, 'romarin', 30, 'pleine terre'), (3, 'Tomates Roma', 70, 'pleine terre'), (4, 'clematite', 15, 'en pot ou pleine terre')]
    """
