# Hent data fra SQL database og gem i Pandas DataFrame

# Importerer de nødvendige biblioteker
import pandas as pd
import mysql.connector

#Log ind på database serveren
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="productdb"
)

#Mycursor er "nøglen" til at kunne "komme ind" og interagere med databasen
mycursor = mydb.cursor()

#Viser alle tabeller i databasen "prouctdb"
mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)

mycursor.close() #Lukker forbindelsen til databasen