# Esempio di calcolo del fattoriale in modo ricorsivo
def factorial(n):
    """
    Calcola il fattoriale di n in modo ricorsivo.
    
    Args:
    - n: Numero intero non negativo
    
    Returns:
    - Fattoriale di n
    """
    # Caso base: se n è 0 o 1, il fattoriale è 1
    if n == 0 or n == 1:
        return 1
    else:
        # Passo ricorsivo: n * fattoriale di (n-1)
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120


# Esempio di calcolo della sequenza di Fibonacci in modo ricorsivo
def fibonacci(n):
    """
    Calcola l'n-esimo numero di Fibonacci in modo ricorsivo.
    
    Args:
    - n: Numero intero non negativo
    
    Returns:
    - n-esimo numero di Fibonacci
    """
    # Caso base: se n è 0 o 1, restituisce n
    if n <= 1:
        return n
    else:
        # Passo ricorsivo: somma dei due numeri di Fibonacci precedenti
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))  # Output: 34


# Esempio di somma dei numeri fino a n in modo ricorsivo
def sum_recursive(n):
    """
    Calcola la somma dei primi n numeri in modo ricorsivo.
    
    Args:
    - n: Numero intero non negativo
    
    Returns:
    - Somma dei primi n numeri
    """
    # Caso base: se n è 0, restituisce 0
    if n == 0:
        return 0
    else:
        # Passo ricorsivo: n + somma dei numeri fino a (n-1)
        return n + sum_recursive(n - 1)

print(sum_recursive(3))  # Output: 6
