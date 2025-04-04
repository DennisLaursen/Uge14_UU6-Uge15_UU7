# Importerer de nødvendige biblioteker
import pandas as pd
import os

# Definerer en funktion for at udtrække data fra CSV-filerne
# Denne funktion tager en relativ sti som input og returnerer en DataFrame
def extract_csv(path: str):
    return pd.read_csv(path)

# Definerer en funktion til at hente og returnere DataFrames
def get_dataframes():
    dataframe_staffs = extract_csv("Data CSV/staffs.csv") # DataFrame for medarbejdere
    dataframe_stores = extract_csv("Data CSV/stores.csv") # DataFrame for butikker
    return dataframe_stores, dataframe_staffs # Returnerer begge DataFrames

# Hvis scriptet køres direkte, kan vi kalde funktionen
if __name__ == "__main__":
    dataframe_stores, dataframe_staffs = get_dataframes() # Henter DataFrames
    print(dataframe_staffs.head()) # Udskriver de første 5 rækker af medarbejder DataFrame
    print(dataframe_stores.head()) # Udskriver de første 5 rækker af butik DataFrame