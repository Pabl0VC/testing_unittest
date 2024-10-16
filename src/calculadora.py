# DOCTEST
def suma(a, b):
    """
    Suma dos números.
    
    >>> suma(2, 3)
    5
    >>> suma(-1, 1)
    0
    >>> suma(0, 0)
    0
    """
    return a + b

def resta(a, b):
    """
    Resta el segundo número del primero.
    
    >>> resta(5, 3)
    2
    >>> resta(10, 20)
    -10
    >>> resta(0, 0)
    0
    """
    return a - b

def multiplicacion(a, b):
    """
    Multiplica dos números.
    
    >>> multiplicacion(2, 3)
    6
    >>> multiplicacion(-1, 5)
    -5
    >>> multiplicacion(0, 10)
    0
    """
    return a * b

def division(a, b):
    """
    Divide el primer número por el segundo. 
    Nota: No permite división por cero.
    
    >>> division(10, 2)
    5.0
    >>> division(5, 2)
    2.5
    >>> division(9, 3)
    3.0
    """
    return a / b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
