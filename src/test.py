
# CODIGO QUE VA A IR A PRODUCCION
def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total

# PRUEBAS DE CODIGO
# Que pasa si la lista está vacia
def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0

# Que pasa si existe un producto
def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebook", "price": 5
        }
    ]
    assert calculate_total(products) == 5

# Que pasa si existen multiples productos
def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "Book", "price": 10
        },
        {
            "name": "Pen", "price": 2
        }
    ]
    assert calculate_total(products) == 12

# Garantiza que las pruebas se ejecuten solo si el archivo se ejecuta directamente, no cuando se importa.
if __name__ == "__main__":
     test_calculate_total_with_empty_list()
     test_calculate_total_with_single_product()
     test_calculate_total_with_multiple_product()