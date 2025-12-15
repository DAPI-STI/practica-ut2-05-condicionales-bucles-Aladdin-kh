"""
Ejercicio 1:
Clasifica un número como positivo, negativo o cero.
"""

def sign(n: int) -> str:
    """
    Devuelve:
    - "positivo" si n > 0
    - "negativo" si n < 0
    - "cero" si n == 0
    """
    if n == 0:
        print("cero")
    elif n >= 1:
        print("positivo")
    elif n < 0:
        print("negativo")
    raise NotImplementedError("Implementa sign(n)")
