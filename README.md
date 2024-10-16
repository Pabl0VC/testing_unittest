# Guía para la Organización de Pruebas en Python

> **Nota**: Todo lo mencionado en esta guía se puede ver en detalle en el proyecto correspondiente. Asegúrate de revisar los archivos de pruebas en el repositorio para ver implementaciones concretas.

## 1. **Organización de las Pruebas**

### a. **Usar un Directorio Separado para las Pruebas**
Es una buena práctica colocar todas las pruebas en un directorio llamado `tests/` en la raíz del proyecto. Esto ayuda a mantener las pruebas separadas del código fuente.

    my_project/

        ├── src/

        │   ├── module1.py

        │   └── module2.py

        ├── tests/

        │   ├── test_module1.py

        │   └── test_module2.py

        └── ...

### b. **Mismo Esquema que el Código Fuente**
La estructura del directorio `tests/` debe reflejar la estructura del código fuente. Por ejemplo, si tienes un archivo `module1.py` en tu código fuente, las pruebas correspondientes deberían estar en `tests/test_module1.py`.

### c. **Agrupar Pruebas en Clases**
Utiliza **clases** para agrupar pruebas relacionadas. Cada clase debería agrupar pruebas de un módulo o una funcionalidad específica. De esta forma, puedes aprovechar métodos como `setUp` y `tearDown` para inicializar o limpiar datos entre las pruebas.

```python
import unittest

class CalculatorTests(unittest.TestCase):
   def setUp(self):
       # Código para preparar el entorno de pruebas
       pass

   def tearDown(self):
       # Código para limpiar después de las pruebas
       pass

   def test_add(self):
       # Prueba para la función de suma
       pass

   def test_subtract(self):
       # Prueba para la función de resta
       pass
```

## 2. **Nombrar las Pruebas**

### a. **Nombrar Archivos de Pruebas**

Los archivos de pruebas deben seguir la convención de nombrarlos con el prefijo `test_` para que puedan ser detectados automáticamente por los frameworks de pruebas como **unittest** o **pytest**.

```bash
test_module1.py

test_module2.py
```

### b. **Nombrar Métodos de Prueba**
Los métodos de prueba deben comenzar con `test_`, seguido de una descripción clara de lo que están probando. Esto asegura que las pruebas sean descubiertas automáticamente y hace que su propósito sea evidente. Utiliza nombres descriptivos para los métodos, que reflejen claramente el comportamiento que se está probando.

```python
class CalculatorTests(unittest.TestCase):
   def test_addition_with_positive_numbers(self):
       # Prueba suma con números positivos
       pass

   def test_division_by_zero_raises_error(self):
       # Prueba que la división por cero arroje un error
       pass
```
### c. **Descripciones Claras**
Asegúrate de que los nombres de las pruebas describan el comportamiento esperado, como qué función estás probando y en qué condiciones. Evita nombres genéricos como test_1, test_case o test_function.

## 3. **Separar las Pruebas por Tipos**

### a. **Pruebas Unitarias**
Las pruebas unitarias deben centrarse en probar unidades individuales de funcionalidad (funciones o métodos). Deben ser rápidas y no depender de recursos externos (como bases de datos o APIs).

### b. **Pruebas de Integración**
En archivos separados o bajo una estructura diferente, incluye pruebas de integración que prueben cómo las diferentes partes del sistema interactúan entre sí.

    tests/

        ├── unit/

        │   ├── test_module1.py

        │   └── test_module2.py

        ├── integration/

        │   ├── test_integration_module1_module2.py

## 4. **Utilizar Métodos de Configuración y Limpieza**
Cuando varias pruebas comparten datos o configuraciones, utiliza métodos como `setUp`, `tearDown`, `setUpClass` y `tearDownClass` de unittest o los equivalentes de pytest para reducir la repetición de código.

```python
class DatabaseTests(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
       # Código para configurar recursos una sola vez antes de todas las pruebas
       pass

   @classmethod
   def tearDownClass(cls):
       # Código para liberar los recursos una vez después de todas las pruebas
       pass

   def setUp(self):
       # Código que se ejecuta antes de cada prueba individual
       pass

   def tearDown(self):
       # Código que se ejecuta después de cada prueba individual
       pass
```

## 5. **Usar Nombres Descriptivos para las Clases de Prueba**
Al igual que los métodos de prueba, las clases de prueba también deben tener nombres descriptivos. Los nombres deben indicar qué clase o funcionalidad están probando.

```python
class UserAuthenticationTests(unittest.TestCase):
   def test_login_with_valid_credentials(self):
       # Prueba de inicio de sesión con credenciales válidas
       pass
```

## 6. **Documentación y Comentarios**
Incluir comentarios breves o docstrings en las pruebas puede ayudar a aclarar lo que se está probando y por qué. Esto es especialmente útil si la prueba tiene una lógica compleja o si estás probando un caso límite específico.

```python
class MathOperationsTests(unittest.TestCase):
   def test_square_root_of_negative_number_raises_error(self):
       """Debe generar un ValueError cuando se intenta calcular la raíz cuadrada de un número negativo"""
       with self.assertRaises(ValueError):
           math.sqrt(-1)
```

## 7. **Evitar Dependencias entre Pruebas**
Cada prueba debe ser independiente y no debe depender de los resultados o el estado de otras pruebas. Esto garantiza que puedan ejecutarse de forma aislada, en cualquier orden.

## 8. **Ejecutar Pruebas Automáticamente**
Utiliza herramientas como `pytest` o `unittest` para ejecutar las pruebas de forma automática y generar informes. Puedes integrarlas en un sistema de integración continua (CI) como Travis CI o GitHub Actions.

## 9. **Uso de Frameworks de Prueba**

- **unittest**: Es el framework de pruebas estándar en Python y tiene una buena integración con la línea de comandos.

- **pytest**: Proporciona una sintaxis más simple y muchas características adicionales, como fixtures y el descubrimiento automático de pruebas.

# Conclusión
Una buena organización y una convención de nombres adecuada hacen que tus pruebas sean más mantenibles y fáciles de entender. Siguiendo estas prácticas, te asegurarás de que tus pruebas sean eficaces y fáciles de trabajar a largo plazo.