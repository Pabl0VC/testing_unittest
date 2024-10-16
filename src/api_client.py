import requests

def get_location(ip):
    url = f'https://freeipapi.com/api/json/{ip}'
    
    # Hace la solicitud
    response = requests.get(url)
    
    # Levanta una excepción si el status code es 4xx o 5xx
    #response.raise_for_status()
    
    # Convierte la respuesta JSON en un diccionario
    data = response.json()
    
    # Retorna un diccionario con los datos de interés
    return {
        "pais": data["countryName"],
        "region": data["regionName"],
        "ciudad": data["cityName"],
        "moneda": data["currency"]["name"]
    }

if __name__ == "__main__":
    # Prueba manual con una IP específica
    print(get_location("8.8.8.8"))
