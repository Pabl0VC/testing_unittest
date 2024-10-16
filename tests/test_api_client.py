import unittest
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTest(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        """
        Prueba el método get_location para asegurarse de que devuelve los datos esperados.
        Usamos el decorador @patch para simular la respuesta del método requests.get
        y evitar hacer una llamada real a la API.
        """
        # Simulamos una respuesta con código de estado 200
        mock_get.return_value.status_code = 200
        
        # Simulamos la respuesta JSON de la API. Aquí estamos creando un diccionario que imita la estructura del JSON que recibiríamos de la API.
        mock_get.return_value.json.return_value = {
            "countryName": "United States of America",
            "regionName": "California",
            "cityName": "Mountain View",
            "currency": {"name": "US Dollar"}
        }

        # Llamamos a la función get_location con la IP '8.8.8.8' y verificamos
        # si el resultado es igual a lo que hemos simulado en la respuesta de la API.
        result = get_location("8.8.8.8")

        # Verifica que los valores devueltos por get_location coincidan con los simulados
        self.assertEqual(result.get("pais"), "United States of America")
        self.assertEqual(result.get("region"), "California")
        self.assertEqual(result.get("ciudad"), "Mountain View")
        self.assertEqual(result.get("moneda"), "US Dollar")
