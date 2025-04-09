import requests
import json

url = "http://192.168.20.171:8000/orders"  # Opdateret IP

try:
    response = requests.get(url)
    response.raise_for_status()

    # Vis den rå respons for at kontrollere, hvordan dataene ser ud
    raw_data = response.text
    print("Rå respons fra API:")
    print(raw_data[:500])  # Vis kun de første 500 tegn for at få et hurtigt overblik

    # Rens teksten for escape-tegn og fjern ekstra anførselstegn
    clean_data = raw_data.replace('\\"', '"').strip('"')  # Erstat escape-tegn og fjern unødvendige anførselstegn

    try:
        # Forsøg at konvertere den rensede tekst til JSON
        data = json.loads(clean_data)
        print("\n📦 Ordrer fra API:")
        for order in data[:5]:  # Vis de første 5 ordrer
            print(json.dumps(order, indent=4))  # Print ordrerne med pæn formatering
    except json.JSONDecodeError as e:
        print(f"⚠️ Fejl i JSON-dekodning: {e}")

except requests.exceptions.RequestException as e:
    print(f"⚠️ Fejl ved forespørgsel: {e}")