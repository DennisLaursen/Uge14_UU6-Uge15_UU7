import pandas as pd
import os


# --- Transformer staffs.csv ---
def transform_staffs(df: pd.DataFrame) -> pd.DataFrame:
    # Ændre kolonnenavne til små bogstaver og fjern evt. mellemrum
    df.columns = [col.lower().strip() for col in df.columns]

    # Aktiv: konverter fra 0/1 til boolean (False/True)
    df['active'] = df['active'].astype(bool)

    # Rens e-mails: fjern mellemrum og ændre til små bogstaver
    df['email'] = df['email'].str.replace(' ', '', regex=False).str.lower() #regex=False gør at Python behandler mailadressen som en almindelig tekststreng

    # Manglende manager_id: sæt til 0 (kan tolkes som "ingen leder" eller "er leder")
    df['manager_id'] = df['manager_id'].fillna(0).astype(int)

    # Slå for- og efternavn sammen til 'name' og fjern de gamle kolonner
    full_name = df['name'].str.strip() + ' ' + df['last_name'].str.strip()
    df = df.drop(columns=['name', 'last_name'])

    # Generér unik nøgle-id
    df = df.reset_index(drop=True)
    df.insert(0, 'id', df.index + 1)  # Simpelt ID (1, 2, 3...)

    # Indsæt 'name' mellem 'id' og 'email'
    email_index = df.columns.get_loc('email')
    df.insert(email_index, 'name', full_name)

    return df


# --- Transformer stores.csv ---
def transform_stores(df: pd.DataFrame) -> pd.DataFrame:
    # Ændre kolonnenavne til små bogstaver og fjern mellemrum
    df.columns = [col.lower().strip() for col in df.columns]

    # Rens e-mails: fjern mellemrum og ændre til små bogstaver
    df['email'] = df['email'].str.replace(' ', '', regex=False).str.lower() #regex=False gør at Python behandler mailadressen som en almindelig tekststreng

    # Vi bruger store_name som nøgle-id, og som sekundær nøgle i staffs.csv

    return df


if __name__ == "__main__":
    # Dynamisk sti til 'Data CSV'-mappen
    base_path = os.path.join(os.path.dirname(__file__), '..', 'Data CSV')

    # --- Staffs ---
    staffs_path = os.path.join(base_path, 'staffs.csv')
    df_staffs = pd.read_csv(staffs_path)
    df_staffs_trans = transform_staffs(df_staffs)
    df_staffs_trans.to_csv(os.path.join(base_path, 'staffs_transformed.csv'), index=False)

    # --- Stores ---
    stores_path = os.path.join(base_path, 'stores.csv')
    df_stores = pd.read_csv(stores_path)
    df_stores_trans = transform_stores(df_stores)
    df_stores_trans.to_csv(os.path.join(base_path, 'stores_transformed.csv'), index=False)

    print("CSV-data er transformeret og gemt.")