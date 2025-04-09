# Importerer de nødvendige biblioteker
import mysql.connector
from mysql.connector import Error

tables = ["brands", "categories", "products", "stocks"] #Definerer tabellerne vi vil hente data fra

try: # Opretter forbindelse til MySQL-databasen
    conn = mysql.connector.connect(
        host="192.168.20.171",
        port=3306,
        user="curseist",
        password="curseword",
        database="productdb"
    )

    if conn.is_connected(): # Tjekker om forbindelsen er oprettet
        print("✅ Forbindelse oprettet til 'productdb'\n")
        cursor = conn.cursor()

        for table in tables: # Itererer gennem tabellerne
            print(f"\n📦 Indhold af tabellen '{table}':")
            cursor.execute(f"SELECT * FROM {table} LIMIT 5") # Henter de første 5 rækker fra tabellen
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]

            print(" | ".join(columns)) # Udskriver kolonnenavne
            print("-" * 50) # Udskriver en separator
            for row in rows:
                print(" | ".join(str(item) for item in row)) # Udskriver rækkerne
            print("-" * 50)

        cursor.close()

# Hvis login til databasen mislykkes, udskriv fejlmeddelelse
except Error as e:
    print(f"⚠️ Fejl: {e}")

#Tjekker om forbindelsen er lukket og lukker den hvis det ikke er tilfældet
finally:
    if conn.is_connected():
        conn.close()
        print("\n🔌 Forbindelsen er lukket igen.")
