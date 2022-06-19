import sqlite3

def affichercontenubdd():
    connection = sqlite3.connect("../plantes.db")
    cursor = connection.cursor()    
    cursor.execute("SELECT * FROM plantes")
    plantedelabdd = cursor.fetchall()
    return plantedelabdd
    
